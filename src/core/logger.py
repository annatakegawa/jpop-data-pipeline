import logging


class Logger:
    """
    Centralized logging utility for the application.
    """

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)

            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
            )
            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def debug(self, message: str):
        self.logger.debug(message)
