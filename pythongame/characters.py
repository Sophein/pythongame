from .translations import load_translations

class Character:
    def __init__(self, name, hp, attack_power, defense, character_type="", language="en"):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = 1
        self.experience = 0
        self.character_type = character_type
        self.inventory = []  # Inventory starts empty
        self.language = language  # Stock the chosen language
        self.translations = load_translations(self.language)  # Charge les traductions en fonction de la langue

    def is_alive(self):
        """Check if the character is still alive."""
        return self.hp > 0

    def attack(self, target):
        """Calculate damage and apply it to the target."""
        target.take_damage(self.attack_power)  # L'attaque est directement passée à la méthode take_damage
        return self.attack_power  # Retourne l'attaque brute

    def take_damage(self, damage):
        """Reduce hp by the damage taken."""
        # Calcul des dégâts après prise en compte de la défense
        damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.hp -= max(0, damage)  # Applique les dégâts
        self.hp = max(0, self.hp)  # Empêche les HP de devenir négatifs

    def set_experience(self, exp):
        """Permet de définir l'expérience du personnage."""
        self.experience = exp

    def calculate_experience_to_next_level(self):
        """Calculate the experience needed for the next level."""
        return  100 * (self.level ** 1.1)

    def gain_experience(self, exp):
        """Gain experience and level up if threshold is reached."""
        self.experience += exp
        print(self.translations["gain_exp_message"].format(character=self.name, exp=exp))
        # Utiliser experience_to_next_level pour obtenir le seuil
        while self.experience >= self.calculate_experience_to_next_level():
            self.experience -= self.calculate_experience_to_next_level()  # Réduire l'expérience après le niveau up
            self.level_up()

    def level_up(self):
        """Level up the character and increase stats."""
        self.level += 1
        self.hp += 10  # Increase HP on level up
        self.attack_power += 1  # Increase attack power on level up
        self.defense += 1  # Increase defense on level up
        print(self.translations["level_up_info"].format(character=self.name, level=self.level))
        self.allocate_points()

    def allocate_points(self):
        """Allow the player to allocate a stat point."""
        print(self.translations["level_up_message"].format(character=self.name))
        print(self.translations["select_stats"].format())
        print(self.translations["stats_choice_1"].format())
        print(self.translations["stats_choice_2"].format())
        print(self.translations["stats_choice_3"].format())

        # Get the player's choice
        choice = input(self.translations["select_stats"].format())

        if choice == "1":
            self.hp += 10
            print(self.translations["points_increased_1"].format(character=self.name))
        elif choice == "2":
            self.attack_power += 2
            print(self.translations["points_increased_2"].format(character=self.name))
        elif choice == "3":
            self.defense += 2
            print(self.translations["points_increased_3"].format(character=self.name))
        else:
            print("Invalid choice, no stat was increased.")
        print(self.translations["stats_info"].format(character=self.name, hp=self.hp, attack_power=self.attack_power, defense=self.defense))
    
    def add_item(self, item):
        """Add an item to the inventory if there is space."""
        if len(self.inventory) < 5:
            self.inventory.append(item)
            print(self.translations["item_added"].format(character=self.name, item=item))
        else:
            print(self.translations["inventory_full"].format(character=self.name))

    def use_item(self, item_name):
        """Use an item from the inventory."""
        item_found = None
        for item in self.inventory:
            if item.name == item_name:
                item_found = item
            break

        if item_found:
                self.apply_effect(item_found.effect)
                self.inventory.remove(item_found)
                print(self.translations["item_used"].format(character=self.name, item=item_name))
        else:
                print(self.translations["item_not_found"].format(item=item_name))

    def apply_effect(self, effect):
        """Apply the effect of an item."""
        for stat, value in effect.items():
            if stat == "hp":
                self.hp = min(self.hp + value, 100)  # HP cannot exceed 100
            elif stat == "attack_power":
                self.attack_power += value
            elif stat == "defense":
                self.defense += value

class DPS(Character):
    def __init__(self, name, hp, attack_power, defense, language="en"):
        super().__init__(name, hp, attack_power, defense, character_type="dps", language=language)
        
    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.take_damage(damage)

class Tank(Character):
    def __init__(self, name, hp, attack_power, defense, damage_reduction, language="en"):
        super().__init__(name, hp, attack_power, defense, character_type="tank", language=language)
        self.damage_reduction = damage_reduction

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, attack_power, defense, magic_attack, language="en"):
        super().__init__(name, hp, attack_power, defense, character_type="mage", language=language)
        self.magic_attack = magic_attack

    def attack(self, target):
        damage = max(0, self.magic_attack - target.defense)
        target.take_damage(damage)

class Enemy:
    def __init__(self, name, attack_power, defense, hp, exp_value):
        self.name = name
        self.attack_power = attack_power
        self.defense = defense
        self.hp = hp
        self.exp_value = exp_value

    def attack(self, target):
        """Calculate damage and apply it to the target."""
        target.take_damage(self.attack_power)  # L'attaque est directement passée à la méthode take_damage
        return self.attack_power  # Retourne l'attaque brute

    def take_damage(self, damage):
        """Reduce hp by the damage taken."""
        # Calcul des dégâts après prise en compte de la défense
        damage = max(0, damage - self.defense)  # Réduction des dégâts par la défense
        self.hp -= max(0, damage)  # Applique les dégâts
        self.hp = max(0, self.hp)  # Empêche les HP de devenir négatifs
