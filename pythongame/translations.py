import json
import os

def load_translations(language):
    # Récupère le chemin absolu du fichier translations.json
    base_path = os.path.dirname(__file__)  # Le répertoire où se trouve le fichier Python
    json_path = os.path.join(base_path, '..', 'translations.json')  # Chemin vers translations.json

    # Ouvre et charge le fichier JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        all_translations = json.load(file)

    # Retourne les traductions pour la langue spécifiée, ou un dictionnaire vide si la langue n'existe pas
    return all_translations.get(language, {})
