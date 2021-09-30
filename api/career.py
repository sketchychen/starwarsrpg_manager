from typing import Tuple

class Career:
    def __init__(
        self,
        name: str,
        skills: Tuple[Tuple[str]]
    ):
        self.name = name
        self.skills = skills


class Specialization(Career):
    def __init__(
        self,
        name: str,
        skills: Tuple[Tuple[str]]
    ):
        Career.name = name
        Career.skills = skills