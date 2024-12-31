class Item:
    """Represents an item in the game."""
    def __init__(self, name, item_type, effect):
        """
        Initialize an item.
        :param name: Name of the item.
        :param item_type: Type of the item (e.g., "potion", "weapon").
        :param effect: Effect of the item (e.g., {"hp": +20}).
        """
        self.name = name
        self.item_type = item_type
        self.effect = effect

    def __str__(self):
        return f"{self.name} ({self.item_type})"
