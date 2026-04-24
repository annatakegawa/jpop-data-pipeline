from abc import ABC, abstractmethod


class BaseSource(ABC):
    """
    Abstract base class for all data sources.

    Defines the interface that all sources must implement.
    """

    @abstractmethod
    def fetch_groups(self):
        """Return raw group data"""
        pass

    @abstractmethod
    def fetch_idols(self):
        """Return raw idol data"""
        pass
