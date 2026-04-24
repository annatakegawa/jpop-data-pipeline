from ingestion.sources.base_source import BaseSource


class StaticSource(BaseSource):
    """
    Static/mock data source for initial development and testing.
    """

    def fetch_groups(self):
        return [
            {
                "name": "Snow Man",
                "agency": "STARTO",
                "debut_date": "2020-01-22",
            },
            {
                "name": "SixTONES",
                "agency": "STARTO",
                "debut_date": "2020-01-22",
            },
            {
                "name": "M!LK",
                "agency": "EBiDAN",
                "debut_date": "2014-11-24",
            },
        ]

    def fetch_idols(self):
        return []  # implement later
