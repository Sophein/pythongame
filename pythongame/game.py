# game.py
import json
from pythongame.characters import DPS, Tank, Mage, Enemy
from pythongame.combat import Combat
from pythongame.inventory import Item

class Game:
    def __init__(self, language="en"):
        self.language = language
        self.translations = self.load_translations(language)
    
    def load_translations(self, language):
        """Load translations from the JSON file."""
        import os
        import json
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "translations.json")
        
        with open(file_path, "r") as file:
            translations = json.load(file)
        return translations.get(language, translations["en"])

    def select_hero(self):
        """Prompt the player to select a hero."""
        print(self.translations["select_hero"])
        print(self.translations["hero_choice_1"])
        print(self.translations["hero_choice_2"])
        print(self.translations["hero_choice_3"])
        
        choice = input(self.translations["enter_choice"])
        if choice == '1':
            return DPS(name="Luqman", hp=100, attack_power=35, defense=5, language=self.language)
        elif choice == '2':
            return Tank(name="Yahya", hp=150, attack_power=20, defense=30, damage_reduction=5, language=self.language)
        elif choice == '3':
            return Mage(name="Balqis", hp=80, attack_power=25, defense=15, magic_attack=40, language=self.language)
        else:
            print(self.translations["invalid_choice"])
            return self.select_hero()

    def start(self):
        """Start the game."""
        hero = self.select_hero()
        enemy = Enemy("Goblin", 8, 3, 30, 120)  # Exemple d'ennemi
        combat = Combat(hero, enemy, self.translations)
        combat.start()
    
    def generate_random_item(self):
        """Generate a random item."""
        import random
        items = [
            Item("Health Potion", "potion", {"hp": 20}),
            Item("Strength Elixir", "potion", {"attack_power": 5}),
            Item("Shield", "armor", {"defense": 3}),
        ]
        return random.choice(items)
    
    def handle_combat(self, hero, enemy):
        combat = Combat(hero, enemy, self.translations)
        result = combat.start()
        if result["status"] == "win":
            hero.gain_experience(result["exp"])

    def add_item_to_character(self, character, item):
        character.add_item(item)
        print(self.translations["item_added"].format(item=item["name"]))


