from constants import characteristics, talents


character = {
    'name': '',
    'species': {},  # ref constants SPECIES
    'career': {},  # ref constants CAREER
    'total_xp': 100,
    'available_xp': 100,
    'stats': {
        'soak_value': 0,
        'force_rating': 0,
        'wounds': {
            'threshold': 0,
            'current': 0,
        },
        'strain': {
            'threshold': 0,
            'current': 0,
        },
        'defense': {
            'ranged': 0,
            'melee': 0,
        },
    },
    'characteristics': {
        characteristic.BRAWN[0]: 0,
        characteristic.AGILITY[0]: 0,
        characteristic.INTELLECT[0]: 0,
        characteristic.CUNNING[0]: 0,
        characteristic.WILLPOWER[0]: 0,
        characteristic.PRESENCE[0]: 0,
    }
    'skills': {  # agg constants SKILLS
        'general': {
            # SKILL[0]: {
            #     'name': SKILL[1],
            #     'characteristic': SKILL[2],
            #     'career': false,
            #     'rank': 0,
            # },
            # lower_snake_case_of_custom_name: {
            #     'name': custom_name,
            #     'characteristic': selected_char,
            #     'career': false,
            #     'rank': 0,
            # },
        },
    },
    'talents': [],  # agg constants TALENT
    'equipment': {
        'weapons': [],  # agg constants & custom ITEM
        'armor': [],  # agg constants & custom ITEM
        'personal': [],  # agg constants & custom ITEM
            # {
            #     'name': '',
            #     'description': '',
            #     'rarity': 1,
            #     'encumbrance': 0,
            #     'price': 0,
            #     'quantity': 1,
            # }
    },
    'notes': '',  # long form string
}