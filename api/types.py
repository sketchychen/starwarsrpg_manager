from typing import (
    NamedTuple,
    TypedDict,
)


class Characteristic(TypedDict):
    key: str
    name: str
    abbr: str


class Item(TypedDict):
    name: str
    rarity: int
    encumbrance: int
    price: int
    description: str


class Skill(TypedDict):
    key: str
    name: str
    characteristic_key: str


class Stat(TypedDict):
    key: str
    name: str


class Talent(TypedDict):
    name: str
    is_active: bool
    is_force: bool
    description: str
