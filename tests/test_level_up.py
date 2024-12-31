import pytest
from unittest.mock import patch

from pythongame.characters import Character, Enemy
from pythongame.combat import Combat

def test_gain_experience():
    translations = {
        "battle_start": "{hero} is battling {enemy}!",
        "win_message": "{character} has defeated {enemy}!",
        "lose_message": "{character} has been defeated by {enemy}!",
        "level_up": "{character} leveled up! Now level {level}!",
        "hp_left": "{character} has {hp} HP left.",
        "gain_exp_message": "{character} gained {exp} experience points."
    }

    hero = Character(name="Hero", hp=100, attack_power=20, defense=10, language="en")
    hero.experience = 90  # On initialise l'expérience du héros à 90
    enemy = Enemy(name="Goblin", hp=30, attack_power=5, defense=2, exp_value=20)

    # Simuler l'entrée de l'utilisateur pour la sélection du héros
    with patch('builtins.input', return_value='1'):  # Simule un choix de héros
        combat = Combat(hero, enemy, translations)
        result = combat.start()

    # Vérification du résultat du combat
    assert result["status"] == "win"
    
    # Vérification de l'expérience et du niveau
    assert hero.experience == 10  # L'expérience excédentaire après avoir monté de niveau
    assert hero.level == 2  # Le héros devrait être passé au niveau 2
