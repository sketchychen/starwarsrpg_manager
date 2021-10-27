SOAK_VALUE = 'Soak Value'
FORCE_RATING = 'Force Rating'
WOUNDS = 'Wounds'
STRAIN = 'Strain'
THRESHOLD = 'Threshold'
CURRENT = 'Current'
DEFENSE = 'Defense'
RANGED = 'Ranged'
MELEE = 'Melee'

BRAWN: str = 'Brawn'
AGILITY: str = 'Agility'
INTELLECT: str = 'Intellect'
CUNNING: str = 'Cunning'
WILLPOWER: str = 'Willpower'
PRESENCE: str = 'Presence'

STATS_DICT = {
    SOAK_VALUE: 0,
    FORCE_RATING: 0,
    WOUNDS: {
        THRESHOLD: 0,
        CURRENT: 0,
    },
    STRAIN: {
        THRESHOLD: 0,
        CURRENT: 0,
    },
    DEFENSE: {
        RANGED: 0,
        MELEE: 0,
    },
    BRAWN: 0,
    AGILITY: 0,
    INTELLECT: 0,
    CUNNING: 0,
    WILLPOWER: 0,
    PRESENCE: 0,
}