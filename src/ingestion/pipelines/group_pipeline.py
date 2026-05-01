from src.core.database import Database, DatabaseError
from src.core.logger import Logger
from src.ingestion.sources.base_source import BaseSource
from src.ingestion.sources.static_source import StaticSource
from src.ingestion.transformers.group_transformer import GroupTransformer
from src.ingestion.loaders.group_loader import GroupLoader
from src.ingestion.loaders.agency_loader import AgencyLoader


class GroupPipeline:
    """
    Pipeline for processing group-level data. This class will orchestrate
    the fetching, transforming, and loading of group data into the database.
    """

    def __init__(self, source: BaseSource):
        self.logger = Logger(self.__class__.__name__)

        self.db = Database()
        self.db.connect()

        self.source = source
        self.transformer = GroupTransformer()

        self.agency_loader = AgencyLoader(self.db, self.logger)
        self.group_loader = GroupLoader(self.db, self.logger)

    def run(self):
        self.logger.info("Starting group ingestion pipeline...")

        # Step 1: Fetch raw group data
        raw_groups = self.source.fetch_groups() or []

        # Step 2: Transform and insert group data into database
        for raw in raw_groups:
            try:
                # Normalize raw data
                group = self.transformer.normalize(raw)

                # Resolve agency -> agency id
                agency_id = self.agency_loader.get_or_create(
                    group["agency_name"]
                )
                group["agency_id"] = agency_id
                del group["agency_name"]

                # Upsert group
                group_id = self.group_loader.upsert(group)

                self.logger.info(
                    f"Loaded group: {group['group_name']} (ID: {group_id})")

            except Exception as e:
                if isinstance(e, DatabaseError):
                    self.logger.error(
                        f"Database error while processing group '{raw['group_name']}': {e}"
                    )
                    raise

                self.logger.error(
                    f"Failed to process group '{raw['group_name']}': {e}")

        self.logger.info("Finished group ingestion pipeline.")


if __name__ == "__main__":
    pipeline = GroupPipeline(StaticSource())
    pipeline.run()
