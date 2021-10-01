from .custom_types import Skill
from . import stats

ASTROGATION: Skill = {
    'name': 'Astrogation',
    'stat': stats.INTELLECT,
}
ATHLETICS: Skill = {
    'name': 'Athletics',
    'stat': stats.BRAWN,
}
BRAWL: Skill = {
    'name': 'BRAWL',
    'stat': stats.BRAWN,
}
CHARM: Skill = {
    'name': 'Charm',
    'stat': stats.PRESENCE,
}
COERCION: Skill = {
    'name': 'Coercion',
    'stat': stats.WILLPOWER,
}
COMPUTERS: Skill = {
    'name': 'Computers',
    'stat': stats.INTELLECT,
}
COOL: Skill = {
    'name': 'Cool',
    'stat': stats.PRESENCE,
}
COORDINATION: Skill = {
    'name': 'Coordination',
    'stat': stats.AGILITY,
}
CORE_WORLDS: Skill = {
    'name': 'Core Worlds',
    'stat': stats.INTELLECT,
}
EDUCATION: Skill = {
    'name': 'Education',
    'stat': stats.INTELLECT,
}
DECEPTION: Skill = {
    'name': 'Deception',
    'stat': stats.CUNNING,
}
DISCIPLINE: Skill = {
    'name': 'Discipline',
    'stat': stats.WILLPOWER,
}
GUNNERY: Skill = {
    'name': 'Gunnery',
    'stat': stats.AGILITY,
}
LEADERSHIP: Skill = {
    'name': 'Leadership',
    'stat': stats.PRESENCE,
}
LIGHTSABER: Skill = {
    'name': 'Lightsaber',
    'stat': stats.BRAWN,
}
LORE: Skill = {
    'name': 'Lore',
    'stat': stats.INTELLECT,
}
MECHANICS: Skill = {
    'name': 'Mechanics',
    'stat': stats.INTELLECT,
}
MEDICINE: Skill = {
    'name': 'Medicine',
    'stat': stats.INTELLECT,
}
MELEE: Skill = {
    'name': 'MELEE',
    'stat': stats.BRAWN,
}
NEGOTIATION: Skill = {
    'name': 'Negotiation',
    'stat': stats.PRESENCE,
}
OUTER_RIM: Skill = {
    'name': 'Outer Rim',
    'stat': stats.INTELLECT,
}
PERCEPTION: Skill = {
    'name': 'Perception',
    'stat': stats.CUNNING,
}
PILOTING_PLANETARY: Skill = {
    'name': 'Piloting - Planetary',
    'stat': stats.AGILITY,
}
PILOTING_SPACE: Skill = {
    'name': 'Piloting - Space',
    'stat': stats.AGILITY,
}
RANGED_HEAVY: Skill = {
    'name': 'Ranged - Heavy',
    'stat': stats.AGILITY,
}
RANGED_LIGHT: Skill = {
    'name': 'Ranged - Light',
    'stat': stats.AGILITY,
}
RESILIENCE: Skill = {
    'name': 'Resilience',
    'stat': stats.BRAWN,
}
SKULDUGGERY: Skill = {
    'name': 'Skulduggery',
    'stat': stats.CUNNING,
}
STEALTH: Skill = {
    'name': 'Stealth',
    'stat': stats.AGILITY,
}
STREETWISE: Skill = {
    'name': 'Streetwise',
    'stat': stats.CUNNING,
}
SURVIVAL: Skill = {
    'name': 'Survival',
    'stat': stats.CUNNING,
}
UNDERWORLD: Skill = {
    'name': 'Underworld',
    'stat': stats.INTELLECT,
}
VIGILIANCE: Skill = {
    'name': 'Vigilance',
    'stat': stats.WILLPOWER,
}
WARFARE: Skill = {
    'name': 'Warfare',
    'stat': stats.INTELLECT,
}
XENOLOGY: Skill = {
    'name': 'Xenology',
    'stat': stats.INTELLECT,
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

SKILLS_DICT = {
    x['name']: {
        'career': False,
        'rank': 0,
    }
    for x
    in SKILLS_ALL
}