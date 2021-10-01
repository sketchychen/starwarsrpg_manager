from . import skills
from . import talents

NAME = 'name'
SKILLS = 'skills'
SPECIALIZATIONS = 'specializations'


# CAREER = {
#     NAME: '',
#     SKILLS: (
#         skills.SKILL,
#     ),
# }

'''

'''

CAREERS = {
    'Ace': (
        skills.ASTROGATION, skills.COOL,
        skills.GUNNERY, skills.MECHANICS,
        skills.PERCEPTION, skills.PILOTING_PLANETARY,
        skills.PILOTING_SPACE, skills.RANGED_LIGHT,
    ),
    'Consular': (
        skills.COOL, skills.DISCIPLINE,
        skills.EDUCATION, skills.LORE,
        skills.LEADERSHIP, skills.NEGOTIATION,
    ),
    'Engineer': (
        skills.ATHLETICS, skills.COMPUTERS,
        skills.EDUCATION, skills.MECHANICS,
        skills.PERCEPTION, skills.PILOTING_SPACE,
        skills.RANGED_LIGHT, skills.VIGILIANCE,
    ),
    'Smuggler': (
        skills.COORDINATION, skills.DECEPTION,
        skills.UNDERWORLD, skills.PERCEPTION,
        skills.PILOTING_SPACE, skills.SKULDUGGERY,
        skills.STREETWISE, skills.VIGILIANCE,
    ),
    'Spy': (
        skills.COMPUTERS, skills.COOL,
        skills.COORDINATION, skills.DECEPTION,
        skills.WARFARE, skills.PERCEPTION,
        skills.SKULDUGGERY, skills.STEALTH,
    ),
}

SPECIALIZATIONS = {
    'Hotshot': (  # Ace
        skills.COOL, skills.COORDINATION,
        skills.PILOTING_PLANETARY, skills.PILOTING_SPACE,
    ),
    'Arbiter': (  # Consular
        skills.XENOLOGY, skills.LIGHTSABER,
        skills.NEGOTIATION, skills.PERCEPTION,
    ),
    'Teacher': (  # Consular
        skills.EDUCATION, skills.LORE,
        skills.LEADERSHIP, skills.PERCEPTION,
    ),
    'Saboteur': (  # Engineer
        skills.COORDINATION, skills.MECHANICS,
        skills.SKULDUGGERY, skills.SABOTEUR,
    ),
    'Gunslinger': (  # Smuggler
        skills.COERCION, skills.COOL,
        skills.OUTER_RIM, skills.RANGED_LIGHT,
    ),
    'Courier': (  # Spy
        skills.ATHLETICS, skills.DECEPTION,
        skills.STREETWISE, skills.VIGILIANCE,
    ),
}
