# combat.py
class Combat:
    def __init__(self, hero, enemy, translations):
        self.hero = hero
        self.enemy = enemy
        self.translations = translations

    def start(self):
        print(self.translations["battle_start"].format(hero=self.hero.name, enemy=self.enemy.name))
        while self.hero.hp > 0 and self.enemy.hp > 0:
            # Le héros attaque l'ennemi
            self.hero.attack(self.enemy)
        
            # Vérification si l'ennemi est vaincu
            if self.enemy.hp <= 0:
                print(self.translations["win_message"].format(character=self.hero.name, enemy=self.enemy.name))
                self.hero.gain_experience(self.enemy.exp_value)
                return {"status": "win"}
        
            # Si l'ennemi est encore en vie, il attaque le héros
            self.enemy.attack(self.hero)
                    
            # Affichage des points de vie restants
            print(self.translations["hp_left"].format(character=self.hero.name, hp=self.hero.hp))
            print(self.translations["hp_left"].format(character=self.enemy.name, hp=self.enemy.hp))
    
        
            # Vérification si le héros est vaincu
            if self.hero.hp <= 0:
                print(self.translations["lose_message"].format(character=self.hero.name, enemy=self.enemy.name))
                return {"status": "lose"}

        # Si la boucle se termine sans victoire/défaite immédiate, on retourne le résultat
        return "combat continues"
