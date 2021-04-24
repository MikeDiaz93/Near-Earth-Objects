"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.

    # @params(self=object, designation = str, name = str, diameter = float, hazardous = False)
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.

        self.designation = info["designation"]
        self.name = info["name"] if info["name"] else None
        self.diameter = float(info["diameter"] if info["diameter"] else 'nan')
        self.hazardous = info["hazardous"] == 'Y'

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object.
        # return f'Full name of the NEO {self.designation}, {self.name}'
        return (self.designation + " (" + self.name + ") ")

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        # return f"A NearEarthObject ..."
        # return f"A NearEarthObject: designation:{self.designation}, name:{self.name}, has a diameter of :{self.diameter}, hazardous: {self.hazardous}"
        if self.hazardous:
            aux = ""
        else:
            aux = "not "
        return f"NEO 2020 FK ({self.name}) has a diameter of {self.diameter} km and is {aux}potentially hazardous."
        # return "NEO {fullname} has a diameter of {diameter:.3f} km and [is/is not] potentially hazardous."
        # return "At {time_str}, '{neo.fullname}' approaches Earth at a distance of {distance:.2f} au and a velocity of {velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")

    def serialize(self):
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.

        self._designation = info["designation"]
        self.time = cd_to_datetime(info["time"])
        self.distance = float(info["distance"])
        self.velocity = float(info["velocity"])
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        # return f'Full name designation {self._designation}, name {self.name}, time{str_time_variable}'
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        # return f"A CloseApproach time{self.time}, distance{self.distance}, velocity{self.velocity}, neo{self.ne}"
        # return "At {time_str}, '{neo.fullname}' approaches Earth at a distance of {distance:.2f} au and a velocity of {velocity:.2f} km/s."
        return f"On {datetime_to_str(self.time)}, '2020 FK ({self.neo.name})' approaches Earth at a distance of {self.distance} au and a velocity of {self.velocity} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize(self):
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity
        }


# if __name__ == '__main__':
#    j = {"designation": "Neo", "name": "Algo",
#         "diameter": 3.4, "hazardous": 'Y'}
#    objeto = NearEarthObject(**j)
#    i = {"designation": "Neo", "tiempo": "2020-01-01 12:30",
#         "distancia": 0.45, "velocidad": 56.78}
