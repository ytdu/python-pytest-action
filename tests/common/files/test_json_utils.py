import json
from app.common.files import json_utils


def test_dump_places(tmpdir):
    tmp_file = tmpdir.join('tmp.json')
    jsons = [
        {'k': 'B', 'v': 98},
        {'k': 'A', 'v': 97},
        {'k': 'ABC', 'v': 979899},
        {'k': 'C', 'v': 99},
    ]
    json_utils.dump_jsons(jsons, tmp_file, sort_key='k')
    res = []
    with open(tmp_file) as f:
        for line in f:
            js = json.loads(line)
            res.append(js)
    sorted_jsons = sorted(jsons, key=lambda x: x['k'])
    assert res == sorted_jsons
