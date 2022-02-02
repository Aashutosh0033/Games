# Number Guessing game
import random
import os
import time


class Player:
    def __init__(self, string):
        self.num = random.randint(1, 50)
        self.string = string
        self.count = 3

    def game(self):
        for i in range(1,4):
            gnum = int(input(f"{self.string} guess the number->"))
            if(gnum == self.num):
                time.sleep(0.3)
                print("Correct Guess!")
                break
            else:
                time.sleep(0.3)
                print("Wrong guess :(")
                self.count -=1
                print(f"You have {self.count} guesses left.")

        return self.count






if __name__ == '__main__':
    while True:
        print("\n\n---------->Welcome to the Number Guessing game<----------\n\n")

        print("Rules:\n1.The number is between 1-50.\n2.You get 3 chances. For every wrong guess one of the there will be a penalty of one chance."
              "\n3.The player with more no. of chances wins the game.")

        print("\n\nTo start the game press 1 or press 0 to exit")
        option = int(input(""))
        if(option == 1):
            time.sleep(0.3)
            os.system('cls')
            print("\nLets start the game :)\n")
            obj1 = Player("Player1")
            count1 = obj1.game()
            obj2 = Player("Player2")
            count2 = obj2.game()

            if(count1 == count2):
                time.sleep(0.3)
                print("It's a tie.")
            elif(count1>count2):
                time.sleep(0.3)
                print("***Player 1 wins.***")
            else:
                time.sleep(0.3)
                print("***Player 2 wins.***")

        elif(option == 0):
            time.sleep(0.3)
            os.system('cls')

            print("Are you sure you want to exit? Press 'y for yes or 'n for no")
            option2 = input()
            if(option2.lower() =='y'):
                time.sleep(0.3)
                os.system('cls')
                break
            elif(option2.lower() == 'n'):
                time.sleep(0.3)
                os.system('cls')
                continue
            else:
                time.sleep(0.3)
                os.system('cls')
                print("Invalid option!!! Enter correct option.")
        else:
            time.sleep(0.3)
            os.system('cls')
            print("Invalid option!!! Enter correct option.")









