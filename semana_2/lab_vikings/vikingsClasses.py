
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength 

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        return
            

# Viking        
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name 
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receiveDamage(self,damage):
        self.health -= damage       
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


import random

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        Vikingo = random.choice(self.vikingArmy)
        Sajon = random.choice(self.saxonArmy)
        daño = Sajon.receiveDamage(Vikingo.attack())
        if "has died" in daño:
            self.saxonArmy.remove(Sajon)
        return daño

    def saxonAttack(self):
        Sajon = random.choice(self.saxonArmy)
        Vikingo = random.choice(self.vikingArmy)
        daño = Vikingo.receiveDamage(Sajon.attack())
        if "has died" in daño:
            self.vikingArmy.remove(Vikingo)
        return daño

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."