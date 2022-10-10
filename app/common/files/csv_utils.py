import csv


def load_to_dicts(filename):
    res = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        res.extend(reader)
    return res
