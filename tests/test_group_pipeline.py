from __future__ import annotations
from ingestion.sources.static_source import StaticSource
from ingestion.pipelines.group_pipeline import GroupPipeline

from datetime import date
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


class DummyLogger:
    """
    Test logger that captures log messages in memory for assertions.
    """

    def __init__(self, name: str):
        self.name = name
        self.info_messages = []
        self.debug_messages = []
        self.error_messages = []

    def info(self, message: str):
        self.info_messages.append(message)

    def debug(self, message: str):
        self.debug_messages.append(message)

    def error(self, message: str):
        self.error_messages.append(message)


class MockDatabase:
    """
    Mock database that simulates basic insert and query operations for testing.
    """

    def __init__(self):
        self.engine = object()
        self.agency_ids = {}
        self.next_agency_id = 1
        self.groups = []
        self.executions = []

    def connect(self):
        return self

    def execute(self, query, params=None):
        sql = str(query).lower()
        payload = params or {}
        self.executions.append((sql, payload.copy()))

        if "insert into agencies" in sql:
            agency_name = payload["agency_name"]
            agency_id = self.agency_ids.get(agency_name)
            if agency_id is None:
                agency_id = self.next_agency_id
                self.agency_ids[agency_name] = agency_id
                self.next_agency_id += 1
            return [(agency_id,)]

        if "insert into groups" in sql:
            self.groups.append(payload.copy())
            return [(len(self.groups),)]

        raise AssertionError(f"Unexpected query: {query}")


class TestGroupPipeline:
    """
    End-to-end tests for the GroupPipeline using a static data source and a mock database.
    """

    def test_group_pipeline_loads_static_groups_end_to_end(self, monkeypatch):
        fake_db = MockDatabase()

        monkeypatch.setattr(
            "ingestion.pipelines.group_pipeline.Database", lambda: fake_db)
        monkeypatch.setattr(
            "ingestion.pipelines.group_pipeline.Logger", DummyLogger)

        pipeline = GroupPipeline(StaticSource())
        pipeline.run()

        assert fake_db.agency_ids == {"STARTO": 1, "EBiDAN": 2}
        assert [group["group_name"] for group in fake_db.groups] == [
            "Snow Man",
            "SixTONES",
            "M!LK",
        ]
        assert [group["agency_id"] for group in fake_db.groups] == [1, 1, 2]
        assert [group["debut_date"] for group in fake_db.groups] == [
            date(2020, 1, 22),
            date(2020, 1, 22),
            date(2014, 11, 24),
        ]
        assert pipeline.logger.error_messages == []
        assert pipeline.logger.info_messages[0] == "Starting group ingestion pipeline..."
        assert pipeline.logger.info_messages[-1] == "Finished group ingestion pipeline."

    def test_group_pipeline_is_idempotent_across_runs(self, monkeypatch):
        fake_db = MockDatabase()

        monkeypatch.setattr(
            "ingestion.pipelines.group_pipeline.Database", lambda: fake_db)
        monkeypatch.setattr(
            "ingestion.pipelines.group_pipeline.Logger", DummyLogger)

        pipeline = GroupPipeline(StaticSource())
        pipeline.run()
        pipeline.run()

        assert fake_db.agency_ids == {"STARTO": 1, "EBiDAN": 2}
        assert len(fake_db.groups) == 6
        assert [group["group_name"] for group in fake_db.groups] == [
            "Snow Man",
            "SixTONES",
            "M!LK",
            "Snow Man",
            "SixTONES",
            "M!LK",
        ]
        assert [group["agency_id"]
                for group in fake_db.groups] == [1, 1, 2, 1, 1, 2]
        assert pipeline.logger.error_messages == []


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
