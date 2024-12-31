# tests/test_characters.py
import pytest
from pythongame.characters import Character, Enemy

def test_character_take_damage():
    hero = Character(name="Hero", hp=100, attack_power=20, defense=10, language="en")
    hero.take_damage(30)
    assert hero.hp == 80  # 100 - (30 - 10)

def test_character_hp_cannot_be_negative():
    hero = Character(name="Hero", hp=50, attack_power=20, defense=10, language="en")
    hero.take_damage(100)
    assert hero.hp == 0

def test_enemy_take_damage():
    enemy = Enemy(name="Goblin", hp=50, attack_power=15, defense=5, exp_value=50)
    enemy.take_damage(20)
    assert enemy.hp == 35  # 50 - (20 - 5)

def test_enemy_hp_cannot_be_negative():
    enemy = Enemy(name="Goblin", hp=20, attack_power=15, defense=5, exp_value=50)
    enemy.take_damage(50)
    assert enemy.hp == 0

def test_character_level_up_with_point_allocation(monkeypatch):
    # Création d'un personnage avec 0 XP
    hero = Character(name="Hero", hp=100, attack_power=20, defense=10, language="en")

    # Simulation de l'entrée utilisateur pour choisir "1" (augmenter HP)
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # Simuler un gain d'expérience
    hero.gain_experience(150)  # Hero should level up once

    # Tester que le personnage a monté de niveau
    assert hero.level == 2
    assert hero.hp == 120  # HP should increase by 10 + 10 from allocation
    assert hero.attack_power == 21  # Attack power should increase by 1
    assert hero.defense == 11  # Defense should increase by 1
