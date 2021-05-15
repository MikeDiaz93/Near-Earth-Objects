from extract import *
from collections import defaultdict


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of
        NEOs and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link
        them together - after it's done, the `.approaches` attribute of
        each NEO has a collection of that NEO's close approaches, and the
        `.neo` attribute of each close approach references the appropriate
        NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
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
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation,
        or `None`.
        """

        return self.collection_1.get(designation, None)

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """

        return self.collection_2.get(name, None)

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection
        of filters.

        This generates a stream of `CloseApproach` objects that match all
        of the provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which
        isn't guaranteed to be sorted meaninfully, although is often sorted
        by time.

        :param filters: A collection of filters capturing user-specified
        criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            if all(f(approach) for f in filters):
                yield approach
