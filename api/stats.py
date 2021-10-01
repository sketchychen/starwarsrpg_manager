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
    stats.SOAK_VALUE: 0,
    stats.FORCE_RATING: 0,
    stats.WOUNDS: {
        stats.THRESHOLD: 0,
        stats.CURRENT: 0,
    },
    stats.STRAIN: {
        stats.THRESHOLD: 0,
        stats.CURRENT: 0,
    },
    stats.DEFENSE: {
        stats.RANGED: 0,
        stats.MELEE: 0,
    },
    stats.BRAWN: 0,
    stats.AGILITY: 0,
    stats.INTELLECT: 0,
    stats.CUNNING: 0,
    stats.WILLPOWER: 0,
    stats.PRESENCE: 0,
}