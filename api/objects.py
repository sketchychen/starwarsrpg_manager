class Item:
    def __init__(self, name, rarity, encumbrance, price, description):
        self.name = name
        self.rarity = rarity
        self.encumbrance = encumbrance
        self.price = price
        self.description = description

    def __str__():
        return (
            f"{self.name}----\n"
            f"Rarity: {self.rarity}\n"
            f"Encumbrance: {self.encumbrance}\n"
            f"Price: {self.price}\n"
            f"{self.description}\n\n"
        )


class Talent:
    def __init__(self, name, is_active, is_force, description):
        self.name = name
        self.is_active = is_active
        self.is_force = is_force
        self.description = description
