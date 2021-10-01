from typing import Tuple

from custom_types import TalentNodeType

class Career:
    def __init__(self, name: str, skills: Tuple[Tuple[str]]):
        self.name = name
        self.skills = skills


class Specialization(Career):
    def __init__(self, parent: Career,
            talent_tree: Tuple[
                TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
                TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
                TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
                TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
                TalentNodeType, TalentNodeType, TalentNodeType, TalentNodeType,
            ],
            **kwargs):
        super(Specialization, self).__init__(**kwargs)
        self.parent = parent
        self.talent_tree = None

        """
        Each talent tree has 20 talents
            and an arbitrary set of paths.
        The 20 talents are represented by
            a tuple of length 20 in the following order:

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
            0: (),
            1: (5,)
            2: (6,)
            ..
            14: (13, 15, 18)
            ...
            19: (15, 18)
        }
        """
        self.talent_tree = talent_tree