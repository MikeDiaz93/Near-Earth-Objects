from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """
    A class to represent a Near Earth Object.

    ...

    Attributes
    ----------
    designation
    name
    diameter
    hazardous


    Methods
    -------
    fullname(self)
    serialize(self)

    """

    def __init__(self, **info):
        """
        Constructs all the necessary attributes for the NearEarthObject.

        Parameters
        ----------
        designation: str
        name : str
        diameter: float
        hazardous: Boolean

        """
        self.designation = info["designation"]
        self.name = info["name"] if info["name"] else None
        self.diameter = float(info["diameter"] if info["diameter"] else 'nan')
        self.hazardous = info["hazardous"] == 'Y'
        self.approaches = []

    @property
    def fullname(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        A representation of the full name of this NEO.
        """
        return (self.designation + " (" + self.name + ") ")

    def __str__(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        A string representation of the NEO.
        """
        if self.hazardous:
            aux = ""
        else:
            aux = "not "
        return f"NEO 2020 FK ({self.name}) has a diameter of {self.diameter}"
        "and is {aux}potentially hazardous."

    def __repr__(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        Returns a printable representation of the NEO.
        """
        return (f"NearEarthObject(designation={self.designation!r},"
                "name={self.name!r}," f"diameter={self.diameter:.3f},"
                "hazardous={self.hazardous!r})")

    def serialize(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        A serialization of the attributes of the NEO.
        """
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous
        }


class CloseApproach:
    """
    A class to represent a close approach to Earth by an NEO.

    ...

    Attributes
    ----------
    _designation
    time
    distance
    velocity
    neo

    Methods
    -------
    time_str(self)
    serialize(self)

    """

    def __init__(self, **info):
        """
        Constructs all the necessary attributes for the CloaseApproach
        object.

        Parameters
        ----------
        _designation = str
        time = datetime
        distance = float
        velocity = float
        neo = None

        """
        self._designation = info["designation"]
        self.time = cd_to_datetime(info["time"])
        self.distance = float(info["distance"])
        self.velocity = float(info["velocity"])
        self.neo = None

    @property
    def time_str(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        formatted representation of this `CloseApproach`'s
        approach time.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        A string representation of the CloseApproach.
        """
        return f"On {datetime_to_str(self.time)}, '2020 FK ({self.neo.name})'"
        "approaches Earth at a distance of {self.distance} au"
        "and a velocity of {self.velocity} km/s."

    def __repr__(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        Returns a printable representation of the CloseApproach.
        """
        return (f"CloseApproach(time={self.time_str!r},"
                "distance={self.distance:.2f},"
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize(self):
        """
        Parametes
        ---------
        None

        Return
        ------
        A serialization of the attributes of the CloseApproach.
        """
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity
        }
