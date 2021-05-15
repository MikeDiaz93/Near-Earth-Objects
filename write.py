import csv
import json


def write_to_csv(results, filename):
    """
    Write an iterable of CloseApproach objects to a CSV file.

            Parameters:

                    results (tuple): An iterable of CloseApproach objects.
                    filename (str): A Path-like object pointing to where
                                the data should be saved.

            Returns:

                    None
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
    """
    Write an iterable of CloseApproach objects to a JSON file.

            Parameters:

                    results (tuple): An iterable of CloseApproach objects.
                    filename (str): A Path-like object pointing to where
                                the data should be saved.

            Returns:

                    None
    """
    approach_list = list()
    for approach in results:
        app = approach.serialize()
        app["neo"] = approach.neo.serialize()
        approach_list.append(app)

    with open(filename, "w") as f:
        writer = json.dump(approach_list, f)
