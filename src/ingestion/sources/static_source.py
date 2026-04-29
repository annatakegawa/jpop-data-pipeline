from src.ingestion.sources.base_source import BaseSource


class StaticSource(BaseSource):
    """
    Static/mock data source for initial development and testing.
    """

    def fetch_groups(self):
        return [
            {
                "group_name": "Snow Man",
                "agency_name": "STARTO",
                "debut_date": "2020-01-22",
            },
            {
                "group_name": "SixTONES",
                "agency_name": "STARTO",
                "debut_date": "2020-01-22",
            },
            {
                "group_name": "M!LK",
                "agency_name": "EBiDAN",
                "debut_date": "2014-11-24",
            },
        ]

    def fetch_idols(self):
        return []  # implement later
