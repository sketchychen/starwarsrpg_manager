ASTROGATION = ('astrogation', 'Astrogation', INTELLECT)
ATHLETICS = ('athletics', 'Athletics', BRAWN)
CHARM = ('charm', 'Charm', PRESENCE)
COERCION = ('coercion', 'Coercion', WILLPOWER)
COMPUTERS = ('computers', 'Computers', INTELLECT)
COOL = ('cool', 'Cool', PRESENCE)
COORDINATION = ('coordination', 'Coordination', AGILITY)
DECEPTION = ('deception', 'Deception', CUNNING)
DISCIPLINE = ('discipline', 'Discipline' WILLPOWER)
LEADERSHIP = ('leadership', 'Leadership', PRESENCE)
MECHANICS = ('mechanics', 'Mechanics', INTELLECT)
MEDICINE = ('medicine', 'Medicine', INTELLECT)
NEGOTIATION = ('negotiation', 'Negotiation', PRESENCE)
PERCEPTION = ('perception', 'Perception', CUNNING)
PILOTING_PLANETARY = ('piloting_planetary', 'Piloting - Planetary', AGILITY)
PILOTING_SPACE = ('piloting_space', 'Piloting - Space', AGILITY)
RESILIENCE = ('resilience', 'Resilience', BRAWN)
SKULDUGGERY = ('skulduggery', 'Skulduggery', CUNNING)
STEALTH = ('stealth', 'Stealth', AGILITY)
STREETWISE = ('streetwise', 'Streetwise', CUNNING)
SURVIVAL = ('survival', 'Survival', CUNNING)
VIGILIANCE = ('vigilance', 'Vigilance', WILLPOWER)

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

BRAWL = ('brawl', 'BRAWL', BRAWN)
GUNNERY = ('gunnery', 'Gunnery', AGILITY)
LIGHTSABER = ('lightsaber', 'Lightsaber', BRAWN)
MELEE = ('melee', 'MELEE', BRAWN)
RANGED_LIGHT = ('ranged_light', 'Ranged - Light', AGILITY)
RANGED_HEAVY = ('ranged_heavy', 'Ranged - Heavy', AGILITY)

SKILLS_COMBAT = (
    BRAWL, GUNNERY, LIGHTSABER, MELEE,
    RANGED_LIGHT, RANGED_HEAVY,
)

CORE_WORLDS = ('core_worlds', 'Core Worlds', INTELLECT)
EDUCATION = ('education', 'Education', INTELLECT)
LORE = ('lore', 'Lore', INTELLECT)
OUTER_RIM = ('outer_rim', 'Outer Rim', INTELLECT)
UNDERWORLD = ('underworld', 'Underworld', INTELLECT)
WARFARE = ('warfare', 'Warfare', INTELLECT)
XENOLOGY = ('xenology', 'Xenology', INTELLECT)

SKILLS_KNOWLEDGE = (
    CORE_WORLDS, EDUCATION, LORE, OUTER_RIM, UNDERWORLD, WARFARE, XENOLOGY
)

SKILLS_ALL = SKILLS_GENERAL + SKILLS_COMBAT + SKILLS_KNOWLEDGE

SKILLS_DICT = {
    x[0]: {
        'career': False,
        'rank': 0,
    }
    for x
    in SKILLS_ALL
}
