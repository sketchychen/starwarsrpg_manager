import json
import os


def json_to_dict(skills):
    file_path = 'server/data/skills.json'

    with open(file_path, 'r') as file:
        data = file.read()

    obj = json.loads(data)

    for k in skills.keys():
        skills[k].update({
            'career': False,
            'rank': 0,
        })
    return skills


SKILLS_DICT = json_to_dict(obj)
SKILLS_TUPLE = SKILLS_DICT.keys()