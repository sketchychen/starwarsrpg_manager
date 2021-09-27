from . import skills

# CAREER = {
#     'name': '',
#     'skills': (
#         skills,
#         skills,
#         skills,
#         skills,
#         skills,
#         skills,
#         skills,
#         skills,
#     ),
# }

HOTSHOT = {
    'name': 'Hotshot',
    'skills': (
        skills.COOL,
        skills.COORDINATION,
        skills.PILOTING_PLANETARY,
        skills.PILOTING_SPACE,
    ),
}

ACE = {
    'name': 'Ace',
    'skills': (
        skills.ASTROGATION,
        skills.COOL,
        skills.GUNNERY,
        skills.MECHANICS,
        skills.PERCEPTION,
        skills.PILOTING_PLANETARY,
        skills.PILOTING_SPACE,
        skills.RANGED_LIGHT,
    ),
    'specializations': (
        HOTSHOT,
    ),
}

CONSULAR = {
    'name': 'Consular',
    'skills': (
        skills.COOL,
        skills.DISCIPLINE,
        skills.EDUCATION,
        skills.LORE,
        skills.LEADERSHIP,
        skills.NEGOTIATION,
    ),
}

ENGINEER = {
    'name': 'Engineer',
    'skills': (
        skills.ATHLETICS,
        skills.COMPUTERS,
        skills.EDUCATION,
        skills.MECHANICS,
        skills.PERCEPTION,
        skills.PILOTING_SPACE,
        skills.RANGED_LIGHT,
        skills.VIGILIANCE,
    ),
}

SMUGGLER = {
    'name': 'Smuggler',
    'skills': (
        skills.COORDINATION,
        skills.DECEPTION,
        skills.UNDERWORLD,
        skills.PERCEPTION,
        skills.PILOTING_SPACE,
        skills.SKULDUGGERY,
        skills.STREETWISE,
        skills.VIGILIANCE,
    ),
}

SPY = {
    'name': 'Spy',
    'skills': (
        skills.COMPUTERS,
        skills.COOL,
        skills.COORDINATION,
        skills.DECEPTION,
        skills.WARFARE,
        skills.PERCEPTION,
        skills.SKULDUGGERY,
        skills.STEALTH,
    ),
}
