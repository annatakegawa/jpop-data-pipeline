from datetime import datetime


class GroupTransformer:
    """
    Transformer for group-level data. This class will handle cleaning,
    normalization, and any necessary transformations to convert raw group data
    into a standardized format for storage.
    """

    def normalize(self, raw: dict) -> dict:
        """
        Normalizes raw group data.
        """
        return {
            "group_name": raw["group_name"].strip(),
            "agency_name": raw["agency_name"].strip(),
            "debut_date": self._parse_date(raw["debut_date"]),
        }

    def _parse_date(self, date_str: str) -> datetime.date:
        """
        Parses a date string into a date object.
        Assumes the formats "YYYY-MM-DD" or "YYYY/MM/DD".
        """
        formats = ["%Y-%m-%d", "%Y/%m/%d"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue

        raise ValueError(f"'{date_str}' is not in a recognized date format.")
