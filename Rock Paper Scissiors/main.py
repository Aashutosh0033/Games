# Rock Paper Scissors

import random
import time

class Game:
    list = ['r','p','s']
    def __init__(self , char):
        self.char = char
    def playGame(self):
        computer = Game.list[random.randint(0,2)]
        if((self.char == 'r' and computer == 's') or (self.char == 'p' and computer == 'r') or (self.char == 's' and computer == 'p') ):
            time.sleep(0.2)
            print(f"{self.char} X {computer}")
            print("You win!!!")
            input("Press any key to continue...")
        else:
            time.sleep(0.2)
            print(f"{self.char} X {computer}")
            print("Computer wins!!!")
            input("Press any key to continue...")





if __name__ == '__main__':
    while(True):
        time.sleep(0.3)
        print("\n\n----------> Welcome to Rock Paper Scissors <----------\n\n")
        print("Rules:\n1.This game is between the Computer and the Player\n2.Rock wins over scissors but loses to "
              "paper.\n3.Scissors wins over paper.\n")
        print("Press 1 to start the game. press 0 to exit")

        option = (input())
        if(option == '1'):
            time.sleep(0.3)
            print("'r'->rock\n'p'->paper\n's'->scissors")
            option3 = input("Choose your option: ")
            if(option3 == 'r' or option3 == 'p' or option3 == 's'):
                obj = Game(option3)
                obj.playGame()
            else:
                print("Invalid option!!! Choose correct option.")
        elif(option == '0'):
            time.sleep(0.3)
            while(True):
                print("    Are you sure you want to exit? 'y' or 'n")
                option2 = input("    ")
                if(option2.lower() == 'y'):
                    time.sleep(0.3)
                    exit(0)
                elif(option2.lower()=='n'):
                    time.sleep(0.3)
                    break
                else:
                    time.sleep(0.3)
                    print("    Invalid option!!! Enter correct option.")
        else:
            time.sleep(0.3)
            print("Invalid option!!! Enter correct option")


