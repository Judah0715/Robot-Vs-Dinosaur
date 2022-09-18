from weapon import Weapon

class Robot:
    def __init__(self, name,):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Laser cannon", 50)

    def attack_dino(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur} with {self.weapon.name} for {self.weapon.attack_power} damage. New health is {dinosaur.health}.")
