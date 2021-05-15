import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = list()
    with open(neo_csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            pdes = row[3]
            name = row[4]
            pha = row[7]
            diameter = row[15]
            neo = NearEarthObject(designation=pdes, name=name,
                                  diameter=diameter, hazardous=pha)
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.
    :param neo_csv_path: A path to a JSON file containing data
    about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = list()
    with open(cad_json_path) as f:
        cad = json.load(f)
    for ca in cad['data']:
        des = ca[0]
        cd = ca[3]
        dist = ca[4]
        v_rel = ca[7]
        approach = CloseApproach(designation=des, time=cd, distance=dist,
                                 velocity=v_rel)
        approaches.append(approach)
    return approaches
