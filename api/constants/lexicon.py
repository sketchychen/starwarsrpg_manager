from types import (
    Characteristic,
    Item,
    Skill,
    Stat,
    Talent,
)

SOAK_VALUE: Stat = { 'key': 'soak_value', 'name': 'Soak Value', }
FORCE_RATING: Stat = { 'key': 'force_rating', 'name': 'Force Rating', }
WOUNDS: Stat = { 'key': 'wounds', 'name': 'Wounds', }
STRAIN: Stat = { 'key': 'strain', 'name': 'Strain', }
DEFENSE: Stat = { 'key': 'defense', 'name': 'Defense', }

THRESHOLD: Stat = { 'key': 'threshold', 'name': 'Threshold', }
CURRENT: Stat = { 'key': 'current', 'name': 'Current', }
RANGED: Stat = { 'key': 'ranged', 'name': 'Ranged', }
MELEE: Stat = { 'key': 'melee', 'name': 'Melee', }


BRAWN: Characteristic = { 'key': 'brawn', 'name': 'Brawn', 'abbr': 'Br', }
AGILITY: Characteristic = { 'key': 'agility', 'name': 'Agility', 'abbr': 'Ag', }
INTELLECT: Characteristic = { 'key': 'intellect', 'name': 'Intellect', 'abbr': 'Int', }
CUNNING: Characteristic = { 'key': 'cunning', 'name': 'Cunning', 'abbr': 'Cun', }
WILLPOWER: Characteristic = { 'key': 'willpower', 'name': 'Willpower', 'abbr': 'Will', }
PRESENCE: Characteristic = { 'key': 'presence', 'name': 'Presence', 'abbr': 'Pr', }


ASTROGATION: Skill = {
    'key': 'astrogation',
    'name': 'Astrogation',
    'characteristic': INTELLECT['key'],
}
ATHLETICS: Skill = {
    'key': 'athletics',
    'name': 'Athletics',
    'characteristic': BRAWN['key'],
}
BRAWL: Skill = {
    'key': 'brawl',
    'name': 'BRAWL',
    'characteristic': BRAWN['key'],
}
CHARM: Skill = {
    'key': 'charm',
    'name': 'Charm',
    'characteristic': PRESENCE['key'],
}
COERCION: Skill = {
    'key': 'coercion',
    'name': 'Coercion',
    'characteristic': WILLPOWER['key'],
}
COMPUTERS: Skill = {
    'key': 'computers',
    'name': 'Computers',
    'characteristic': INTELLECT['key'],
}
COOL: Skill = {
    'key': 'cool',
    'name': 'Cool',
    'characteristic': PRESENCE['key'],
}
COORDINATION: Skill = {
    'key': 'coordination',
    'name': 'Coordination',
    'characteristic': AGILITY['key'],
}
CORE_WORLDS: Skill = {
    'key': 'core_worlds',
    'name': 'Core Worlds',
    'characteristic': INTELLECT['key'],
}
EDUCATION: Skill = {
    'key': 'education',
    'name': 'Education',
    'characteristic': INTELLECT['key'],
}
DECEPTION: Skill = {
    'key': 'deception',
    'name': 'Deception',
    'characteristic': CUNNING['key'],
}
DISCIPLINE: Skill = {
    'key': 'discipline',
    'name': 'Discipline',
    'characteristic': WILLPOWER['key'],
}
GUNNERY: Skill = {
    'key': 'gunnery',
    'name': 'Gunnery',
    'characteristic': AGILITY['key'],
}
LEADERSHIP: Skill = {
    'key': 'leadership',
    'name': 'Leadership',
    'characteristic': PRESENCE['key'],
}
LIGHTSABER: Skill = {
    'key': 'lightsaber',
    'name': 'Lightsaber',
    'characteristic': BRAWN['key'],
}
LORE: Skill = {
    'key': 'lore',
    'name': 'Lore',
    'characteristic': INTELLECT['key'],
}
MECHANICS: Skill = {
    'key': 'mechanics',
    'name': 'Mechanics',
    'characteristic': INTELLECT['key'],
}
MEDICINE: Skill = {
    'key': 'medicine',
    'name': 'Medicine',
    'characteristic': INTELLECT['key'],
}
MELEE: Skill = {
    'key': 'melee',
    'name': 'MELEE',
    'characteristic': BRAWN['key'],
}
NEGOTIATION: Skill = {
    'key': 'negotiation',
    'name': 'Negotiation',
    'characteristic': PRESENCE['key'],
}
OUTER_RIM: Skill = {
    'key': 'outer_rim',
    'name': 'Outer Rim',
    'characteristic': INTELLECT['key'],
}
PERCEPTION: Skill = {
    'key': 'perception',
    'name': 'Perception',
    'characteristic': CUNNING['key'],
}
PILOTING_PLANETARY: Skill = {
    'key': 'piloting_planetary',
    'name': 'Piloting - Planetary',
    'characteristic': AGILITY['key'],
}
PILOTING_SPACE: Skill = {
    'key': 'piloting_space',
    'name': 'Piloting - Space',
    'characteristic': AGILITY['key'],
}
RANGED_HEAVY: Skill = {
    'key': 'ranged_heavy',
    'name': 'Ranged - Heavy',
    'characteristic': AGILITY['key'],
}
RANGED_LIGHT: Skill = {
    'key': 'ranged_light',
    'name': 'Ranged - Light',
    'characteristic': AGILITY['key'],
}
RESILIENCE: Skill = {
    'key': 'resilience',
    'name': 'Resilience',
    'characteristic': BRAWN['key'],
}
SKULDUGGERY: Skill = {
    'key': 'skulduggery',
    'name': 'Skulduggery',
    'characteristic': CUNNING['key'],
}
STEALTH: Skill = {
    'key': 'stealth',
    'name': 'Stealth',
    'characteristic': AGILITY['key'],
}
STREETWISE: Skill = {
    'key': 'streetwise',
    'name': 'Streetwise',
    'characteristic': CUNNING['key'],
}
SURVIVAL: Skill = {
    'key': 'survival',
    'name': 'Survival',
    'characteristic': CUNNING['key'],
}
UNDERWORLD: Skill = {
    'key': 'underworld',
    'name': 'Underworld',
    'characteristic': INTELLECT['key'],
}
VIGILIANCE: Skill = {
    'key': 'vigilance',
    'name': 'Vigilance',
    'characteristic': WILLPOWER['key'],
}
WARFARE: Skill = {
    'key': 'warfare',
    'name': 'Warfare',
    'characteristic': INTELLECT['key'],
}
XENOLOGY: Skill = {
    'key': 'xenology',
    'name': 'Xenology',
    'characteristic': INTELLECT['key'],
}


SKILLS_GENERAL = (
    ASTROGATION, ATHLETICS,
    CHARM, COERCION, COMPUTERS, COOL, COORDINATION,
    DECEPTION, DISCIPLINE,
    LEADERSHIP,
    MECHANICS, MEDICINE, NEGOTIATION,
    PERCEPTION, PILOTING_PLANETARY, PILOTING_SPACE,
    RESILIENCE,
    SKULDUGGERY, STEALTH, STREETWISE, SURVIVAL,
    VIGILIANCE,
)

SKILLS_COMBAT = (
    BRAWL,
    GUNNERY,
    LIGHTSABER,
    MELEE,
    RANGED_HEAVY, RANGED_LIGHT,
)

SKILLS_KNOWLEDGE = (
    CORE_WORLDS,
    EDUCATION,
    LORE, OUTER_RIM,
    UNDERWORLD,
    WARFARE,
    XENOLOGY,
)

SKILLS_ALL = SKILLS_GENERAL + SKILLS_COMBAT + SKILLS_KNOWLEDGE

SKILLS_DICT_DEFAULTS = {
    x['key']: {
        'career': False,
        'rank': 0,
    }
    for x
    in SKILLS_ALL
}
