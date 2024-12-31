import pytest
from pythongame.characters import Character
from pythongame.inventory import Item

def test_add_item():
    hero = Character(name="Hero", hp=100, attack_power=20, defense=10, language="en")
    potion = Item("Health Potion", "potion", {"hp": 20})
    hero.add_item(potion)
    assert len(hero.inventory) == 1
    assert hero.inventory[0].name == "Health Potion"

def test_use_item():
    hero = Character(name="Hero", hp=80, attack_power=20, defense=10, language="en")
    potion = Item("Health Potion", "potion", {"hp": 20})
    hero.add_item(potion)
    hero.use_item("Health Potion")
    assert hero.hp == 100  # HP should not exceed 100
    assert len(hero.inventory) == 0  # Item should be removed from inventory
