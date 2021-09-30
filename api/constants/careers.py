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


HOTSHOT = 'hotshot'
ACE = {
    NAME: 'Ace',
    SKILLS: (
        skills.ASTROGATION, skills.COOL,
        skills.GUNNERY, skills.MECHANICS,
        skills.PERCEPTION, skills.PILOTING_PLANETARY,
        skills.PILOTING_SPACE, skills.RANGED_LIGHT,
    ),
    SPECIALIZATIONS: {
        HOTSHOT: {
            NAME: 'Hotshot',
            SKILLS: (
                skills.COOL, skills.COORDINATION,
                skills.PILOTING_PLANETARY, skills.PILOTING_SPACE,
            ),
        },
    },
}


ARBITER = 'arbiter'
TEACHER = 'teacher'
CONSULAR = {
    NAME: 'Consular',
    SKILLS: (
        skills.COOL, skills.DISCIPLINE,
        skills.EDUCATION, skills.LORE,
        skills.LEADERSHIP, skills.NEGOTIATION,
    ),
    SPECIALIZATIONS: {
        ARBITER: {
            NAME: 'Arbiter',
            SKILLS: (
                skills.XENOLOGY, skills.LIGHTSABER,
                skills.NEGOTIATION, skills.PERCEPTION,
            ),
        },
        TEACHER: {
            NAME: 'Teacher',
            SKILLS: (
                skills.EDUCATION, skills.LORE,
                skills.LEADERSHIP, skills.PERCEPTION,
            ),
        },
    },
}

SABOTEUR = 'saboteur'
ENGINEER = {
    NAME: 'Engineer',
    SKILLS: (
        skills.ATHLETICS, skills.COMPUTERS,
        skills.EDUCATION, skills.MECHANICS,
        skills.PERCEPTION, skills.PILOTING_SPACE,
        skills.RANGED_LIGHT, skills.VIGILIANCE,
    ),
    SPECIALIZATIONS: {
        SABOTEUR: {
            NAME: 'Saboteur',
            SKILLS: (
                skills.COORDINATION, skills.MECHANICS,
                skills.SKULDUGGERY, skills.SABOTEUR,
            ),
        },
    },
}


GUNSLINGER = 'gunslinger'
SMUGGLER = {
    NAME: 'Smuggler',
    SKILLS: (
        skills.COORDINATION, skills.DECEPTION,
        skills.UNDERWORLD, skills.PERCEPTION,
        skills.PILOTING_SPACE, skills.SKULDUGGERY,
        skills.STREETWISE, skills.VIGILIANCE,
    ),
    SPECIALIZATIONS: {
        GUNSLINGER: {
            NAME: 'Gunslinger',
            SKILLS: (
                skills.COERCION, skills.COOL,
                skills.OUTER_RIM, skills.RANGED_LIGHT,
            ),
        },
    },
}

COURIER = 'courier'
SPY = {
    NAME: 'Spy',
    SKILLS: (
        skills.COMPUTERS, skills.COOL,
        skills.COORDINATION, skills.DECEPTION,
        skills.WARFARE, skills.PERCEPTION,
        skills.SKULDUGGERY, skills.STEALTH,
    ),
    SPECIALIZATIONS: {
        COURIER: {
            NAME: 'Courier',
            SKILLS: (
                skills.ATHLETICS, skills.DECEPTION,
                skills.STREETWISE, skills.VIGILIANCE,
            ),
        },
    }
}
