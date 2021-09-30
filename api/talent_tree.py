from objects import Talent

"""
Talent Tree is a weird graph.
Objectives:
    Track talent unlocks per character.
    Limitation determined by graph.
    Character can revisit unlocked nodes at no cost to unlock other edges.
    Thus, weight changes based on revisits.

x  vertex/node
|  edge: connection between two nodes
0  weight: cost of using an edge

[a]      [b]      [c]      [d]
          |        |        |
         10       10       10
          |        |        |
[e]--10--[f]      [g]--10--[h]
 |        |        |        |
15       15       15       15
 |        |        |        |
[i]--15--[j]--15--[k]--15--[l]
 |        |        |        |
20       20       20       20
 |        |        |        |
[m]      [n]      [o]--20--[p]

"""

class Node:
    def __init__(self, node_id: int):
        self.id = node_id
        self.edges = {}

    def __str__(self):
        return (
            f"Node {self.id}'s edges their weights:"
            f"{[x.id for x in self.edges]}\n"
        )

    def add_edge(self, node_id, weight: int = 0):
        self.edges[node_id] = weight


class TrackedNode(Node):
    def __init__(
        self,
        node_id: int,
    ):
        Node.__init__(self, node_id)
        self.visited = False

    def mark_as_visited(self, via: int):
        self.visited = True


class TalentNode(TrackedNode):
    def __init__(
        self,
        node_id: int,
        talent: Talent,
    ):
        TrackedNode.__init__(self, node_id)
        self.talent = Talent


class Graph:
    def __init__(self):
        self.nodes = {}
        self.node_count = 0

    def __str__(self):
        return 


class TalentGraph(Graph):
    def __init__():
        self.paths_taken = []

