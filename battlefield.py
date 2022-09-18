from robot import Robot
from dinosaur import Dinosaur

dinosaur_one = Dinosaur("Rex The Mess", 100)
robot_one = Robot("The Mean Machine")
class Battlefield:

    def __init__(self):
        self.run_game()


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print("")
        print("Greetings, and welcome to Robot Vs. Dinosaur. The coolest robo dino fight ever!")
        print("")
        

    def battle_phase(self):
        while dinosaur_one.health > 0 and robot_one.health > 0:
            robot_one.choose_weapon()
            robot_one.attack(dinosaur_one)
            dinosaur_one.attack(robot_one)
            if robot_one.health == 0 or dinosaur_one.health == 0:
                break


    def display_winner(self):
        if robot_one.health <= 0:
            print(f"Just like that {self.name} crumbles to bolts and screws. {dinosaur_one} Wins the battle!")
        elif dinosaur_one.health <= 0:
            print(f"The big lumb of meat was no match for tough metal {robot_one.name} Wins!")

