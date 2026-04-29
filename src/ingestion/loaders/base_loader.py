class BaseLoader:
    """
    Base class for all loaders. Defines common interface and shared functionality.
    """

    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def load(self, data: dict):
        """
        Load data into the database.
        """
        validated = self.validate(data)
        self.logger.debug(f"Validated data: {validated}")
        transformed = self.transform(validated)
        self.logger.debug(f"Transformed data: {transformed}")
        result = self.upsert(transformed)

        return result

    def validate(self, data: dict) -> dict:
        """
        Validate the input data. Should be overridden by subclasses.
        """
        return data

    def transform(self, data: dict) -> dict:
        """
        Transform the data into the format required by the database. Should be overridden by subclasses.
        """
        return data

    def upsert(self, data: dict):
        raise NotImplementedError(
            "Subclasses must implement the upsert method.")
