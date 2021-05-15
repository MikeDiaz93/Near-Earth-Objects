import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each
    output row corresponds to the information in a single close approach
    from the `results` stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data
    should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s',
                  'designation', 'name', 'diameter_km',
                  'potentially_hazardous')
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for approach in results:
            writer.writerow(
                {**approach.serialize(), **approach.neo.serialize()})


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the
    output is a list containing dictionaries, each mapping
    `CloseApproach` attributes to their values and the 'neo'
    key mapping to a dictionary of the associated NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data
    should be saved.
    """
    approach_list = list()
    for approach in results:
        app = approach.serialize()
        app["neo"] = approach.neo.serialize()
        approach_list.append(app)

    with open(filename, "w") as f:
        writer = json.dump(approach_list, f)
