import json
import os


file_path = 'server/data/skills.json'

with open(file_path, 'r') as file:
    data = file.read()

obj = json.loads(data)


def prepare_skills(skills):
    for k in skills.keys():
        skills[k].update({
            'career': False,
            'rank': 0,
        })
    return skills

SKILLS_DICT = prepare_skills(obj)
SKILLS_TUPLE = SKILLS_DICT.keys()