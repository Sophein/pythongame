# tests/test_combat.py
import pytest
from pythongame.characters import Character, Enemy
from pythongame.combat import Combat

translations = {
    "hp_left": "{character} has {hp} HP left.",
    "battle_start": "{hero} combat {enemy} !",
    "win_message": "{character} has defeated {enemy}!",
    "lose_message": "{character} has been defeated by {enemy}!"
}

def test_combat_hero_wins():
    character = Character(name="Hero", hp=100, attack_power=50, defense=10, language="en")
    enemy = Enemy(name="Goblin", hp=30, attack_power=5, defense=5, exp_value=50)
    combat = Combat(character, enemy, translations)
    result = combat.start()
    assert result["status"] == "win"

def test_combat_enemy_wins():
    character = Character(name="Hero", hp=30, attack_power=10, defense=5, language="en")
    enemy = Enemy(name="Goblin", hp=50, attack_power=20, defense=5, exp_value=50)
    combat = Combat(character, enemy, translations)
    result = combat.start()
    assert result["status"] == "lose"
