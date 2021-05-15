from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object,
    such as its primary designation (required, unique), IAU name
    (optional), diameter in kilometers (optional - sometimes unknown),
    and whether it's marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied
        to the constructor.
        """
        self.designation = info["designation"]
        self.name = info["name"] if info["name"] else None
        self.diameter = float(info["diameter"] if info["diameter"] else 'nan')
        self.hazardous = info["hazardous"] == 'Y'
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return (self.designation + " (" + self.name + ") ")

    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous:
            aux = ""
        else:
            aux = "not "
        return f"NEO 2020 FK ({self.name}) has a diameter of {self.diameter}"
        "and is {aux}potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation
        of this object."""
        return (f"NearEarthObject(designation={self.designation!r},"
                "name={self.name!r}," f"diameter={self.diameter:.3f},"
                "hazardous={self.hazardous!r})")

    def serialize(self):
        """Return a serialization of the designation, name,
        diameter, and potentially hazardous """
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's
    close approach toEarth, such as the date and time (in UTC)
    of closest approach, the nominal approach distance in astronomical
    units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments
        supplied to the constructor.
        """
        self._designation = info["designation"]
        self.time = cd_to_datetime(info["time"])
        self.distance = float(info["distance"])
        self.velocity = float(info["velocity"])
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s
        approach time.

        The value in `self.time` should be a Python `datetime` object.
        While a `datetime` object has a string representation, the
        default representation includes seconds - significant figures
        that don't exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable
        representations and in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""

        return f"On {datetime_to_str(self.time)}, '2020 FK ({self.neo.name})'"
        "approaches Earth at a distance of {self.distance} au"
        "and a velocity of {self.velocity} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation
        of this object."""
        return (f"CloseApproach(time={self.time_str!r},"
                "distance={self.distance:.2f},"
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize(self):
        """Return a serialization of the datime, distance and velocity"""
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity
        }
