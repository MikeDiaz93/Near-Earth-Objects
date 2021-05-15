from extract import *
from collections import defaultdict


class NEODatabase:
    """
    A class to represent a NeoDatabse object.

    ...

    Attributes
    ----------
    neos
    approaches
    collection_1
    collection_2

    Methods
    -------
    get_neo_by_designation(self, designation)
    get_neo_by_name(self, name)
    query(self, filters=())

    """

    def __init__(self, neos, approaches):
        """
        Constructs all the necessary attributes for the NeoDatabase.

        Parameters
        ----------
        neos: list
        approches: list
        collection_1: dict
        collection_2: dict
        """
        self._neos = neos
        self._approaches = approaches
        self.collection_1 = {neo.designation: neo for neo in self._neos}
        self.collection_2 = {neo.name: neo for neo in self._neos}

        for approach in self._approaches:
            if approach._designation in self.collection_1:
                neo = self.collection_1[approach._designation]
                approach.neo = neo
                neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):
        """
        Find and return an NEO by its primary designation.

        Parameters
        ----------
        designation: str
                The primary designation of the NEO
                to search for.
        Return
        ------
        The NearEarthObject with the desired primary designation,
        or None.
        """

        return self.collection_1.get(designation, None)

    def get_neo_by_name(self, name):
        """
        Find and return an NEO by its name.

        Parameters
        ----------
        name: str
            The name, as a string, of the NEO to search for.

        Return
        ------
        The NearEarthObject with the desired name, or None.
        """

        return self.collection_2.get(name, None)

    def query(self, filters=()):
        """
        Query close approaches to generate those that match a collection
        of filters.

        Parameters
        ---------
        filters: tuple
                A collection of filters capturing user-specified
                criteria.
        Return
        -------
        A stream of matching CloseApproach objects.
        """
        for approach in self._approaches:
            if all(f(approach) for f in filters):
                yield approach
