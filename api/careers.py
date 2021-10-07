from . import skills
from . import talents
from .custom_types import TalentType


SKILLS = 'skills'
TALENT_TREE = 'talent_tree'

def talent_node(node_id: str, payload: TalentType, edges: Tuple[int] = ()):
    """
    Each talent tree has 20 talents
        and an arbitrary set of paths.
    The 20 talents are visually represented below

                [ 5_0][ 5_1][ 5_2][ 5_3]
                [10_0][10_1][10_2][10_3]
                [15_0][15_1][15_2][15_3]
                [20_0][20_1][20_2][20_3]
                [25_0][25_1][25_2][25_3]

    where each 'x_y' pair represents XP COST and COLUMN respectively,
    and serves as the node_id of each talent "node" in a tree.

    Each node may have a set of unlockable neighbors,
        represented by tuple of max length 3
        as horizontal edges are bidirectional
        while vertical edges are not--they are unidirectional.

    An example of a graph layout, dict keys representing tuple indeces:
    {
        5_0: {payload: Talent, edges: ()},
        5_1: {payload: Talent, edges: (10_1,)},
        5_2: {payload: Talent, edges: (10_2,)},
        ..
        20_2: {payload: Talent, edges: (20_1, 20_3, 25_2)},
        ...
        25_1: {payload: Talent, edges: (25_0, 25_2)},
    }
    """
    xp_cost, col = node_id.split('_')

    return {'payload': payload, 'edges': edges}


CAREERS = {
    'Ace': {
        SKILLS: (
            skills.ASTROGATION, skills.COOL,
            skills.GUNNERY, skills.MECHANICS,
            skills.PERCEPTION, skills.PILOTING_PLANETARY,
            skills.PILOTING_SPACE, skills.RANGED_LIGHT,
        ),
        'Hotshot': {
            SKILLS: (  # Ace
                skills.COOL, skills.COORDINATION,
                skills.PILOTING_PLANETARY, skills.PILOTING_SPACE,
            ),
            TALENT_TREE: (
                talent_node(talents.SHORTCUT),
                talent_node(talents.HIGH_G_TRAINING, (5,)),
                talent_node(talents.SKILLED_JOCKEY, (6,)),
                talent_node(talents.GRIT, (7,)),
                talent_node(talents.SECOND_CHANCES, (5,)),
                talent_node(talents.GRIT, (4,9)),
                talent_node(talents.SHORTCUT, (7,10)),
                talent_node(talents.HIGH_G_TRAINING, (6,)),
                talent_node(talents.DEAD_TO_RIGHTS, (9,12)),
                talent_node(talents.HIGH_G_TRAINING, (8,10)),
                talent_node(talents.GRIT, (9,)),
            )
        },
    },
    'Consular': {
        SKILLS: (
            skills.COOL, skills.DISCIPLINE,
            skills.EDUCATION, skills.LORE,
            skills.LEADERSHIP, skills.NEGOTIATION,
        ),
        'Arbiter': {
            SKILLS: (  # Consular
                skills.XENOLOGY, skills.LIGHTSABER,
                skills.NEGOTIATION, skills.PERCEPTION,
            ),
        },
            'Teacher': {
            SKILLS: (  # Consular
                skills.EDUCATION, skills.LORE,
                skills.LEADERSHIP, skills.PERCEPTION,
            ),
        },
    },
    'Engineer': {
        SKILLS: (
            skills.ATHLETICS, skills.COMPUTERS,
            skills.EDUCATION, skills.MECHANICS,
            skills.PERCEPTION, skills.PILOTING_SPACE,
            skills.RANGED_LIGHT, skills.VIGILIANCE,
        ),
        'Saboteur': {
            SKILLS: (  # Engineer
                skills.COORDINATION, skills.MECHANICS,
                skills.SKULDUGGERY, skills.SABOTEUR,
            ),
        },
    },
    'Smuggler': {
        SKILLS: (
            skills.COORDINATION, skills.DECEPTION,
            skills.UNDERWORLD, skills.PERCEPTION,
            skills.PILOTING_SPACE, skills.SKULDUGGERY,
            skills.STREETWISE, skills.VIGILIANCE,
        ),
        'Gunslinger': {
            SKILLS: (  # Smuggler
                skills.COERCION, skills.COOL,
                skills.OUTER_RIM, skills.RANGED_LIGHT,
            ),
        },
    },
    'Spy': {
        SKILLS: (
            skills.COMPUTERS, skills.COOL,
            skills.COORDINATION, skills.DECEPTION,
            skills.WARFARE, skills.PERCEPTION,
            skills.SKULDUGGERY, skills.STEALTH,
        ),
        'Courier': {
            SKILLS: (  # Spy
                skills.ATHLETICS, skills.DECEPTION,
                skills.STREETWISE, skills.VIGILIANCE,
            ),
        },
    },
}

