from typing import Tuple, TypedDict


class ItemType(TypedDict):
    name: str
    rarity: int
    encumbrance: int
    price: int
    description: str


class SkillType(TypedDict):
    name: str
    stat: str


class TalentType(TypedDict):
    name: str
    is_active: bool
    is_force: bool
    description: str


class TalentNodeType(TypedDict):
    """
    Each talent tree has 20 nonunique talents and an arbitrary set of paths.
    The 20 talents are represented by a tuple of length 20 as such:
                    [00]-[01]-[02]-[03]
                    [04]-[05]-[06]-[07]
                    [08]-[09]-[10]-[11]
                    [12]-[13]-[14]-[15]
                    [16]-[17]-[18]-[19]

    Elements 0-3 represent talents that cost 5XP
    Elements 4-7 represent talents that cost 10XP
    Elements 8-11 represent talents that cost 15XP
    Elements 12-15 represent talents that cost 20XP
    Elements 16-19 represent talents that cost 25XP

    Each element index serves as the node_id of each talent "node" in a tree.
    Each node may have a set of unlockable neighbors,
        represented by tuple of max length 3
        as horizontal edges are bidirectional
        while vertical edges are not--they are unidirectional.

    An example of a graph layout, dict keys representing tuple indeces:
        {
            0: { payload: TalentType, edges: () },
            1: { payload: TalentType, edges: (5,) }
            ..
            14: { payload: TalentType, edges: (13, 15, 18) }
            ...
            19: { payload: TalentType, edges: (18,) }
        }

    Each element value is a fixed dict type TalentNodeType.

    When creating the graph of a talent tree, follow this type format:
        Tuple[
            TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
            TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
            TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
            TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
            TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
        ]
    """
    payload: TalentType
    edges: Tuple[int, ...]


class AbilityType(TypedDict):
    name: str
    rank: int
    description: str
