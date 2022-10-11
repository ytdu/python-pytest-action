import json


def load_json_lines(filename):
    res = []
    with open(filename) as f:
        for line in f:
            js = json.loads(line)
            res.append(js)
    return res


def load_id2jsons(filename, key='_id'):
    res = {}
    for js in load_json_lines(filename):
        _id = js[key]
        res[_id] = js
    return res


def dump_jsons(jsons, filename, sort_key=None):
    if sort_key:
        jsons = sorted(jsons, key=lambda x: x[sort_key])
    with open(filename, 'w') as f:
        for js in jsons:
            f.write(json.dumps(js, sort_keys=True) + '\n')
