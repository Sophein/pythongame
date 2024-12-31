# main.py
import sys
import os


# Ajouter le répertoire parent de 'main.py' au chemin d'accès
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pythongame.game import Game


def get_user_language():
    """Demander à l'utilisateur de choisir une langue."""
    while True:
        language = input("Choose your language (en/fr): ").strip().lower()
        if language in ["en", "fr"]:
            return language
        else:
            print("Invalid choice. Please choose 'en' for English or 'fr' for French.")


if __name__ == "__main__":
    # Demander à l'utilisateur de choisir une langue
    language = get_user_language()
    
    # Passer la langue au jeu et démarrer
    game = Game(language)
    game.start()
