# Hangman
import random
import time
import list


class Guess():

    def __init__(self):
        self.i = random.randint(0, 8)
        self.word = list.list[self.i]
        self.chance = len(self.word)
    def game(self):
        time.sleep(0.3)
        print("\nLet's start the game.\n")
        print(f"Hint: The word is {self.chance} letters long. It is the name of a car company which sells its cars in India.\n")
        print(f"You have {self.chance+2} chances to guess the letters of the word.")
        a = 0
        for i in range(0, self.chance+2):
            if(a<len(self.word)):
                guess = input(f"Letter no. {a + 1}: ")
                if (guess == self.word[a]):
                    time.sleep(0.3)
                    print("Correct letter!")
                    a += 1
                    self.chance -= 1
                    continue
                else:
                    time.sleep(0.3)
                    print("Wrong letter:(")
                    print(f"You have {self.chance - 1} chances left.")

            else:
                break



        if(a == len(self.word)):
            time.sleep(0.3)
            print("Congratulations!!! You won. The person is saved from hanging.")

        else:
            time.sleep(0.3)
            print("Bad luck:( You lost the game. The person is hanged to death.")









if __name__ == '__main__':
    while True:
        print("\n\n---------->Welcome to Hangman<----------\n")
        print("Rules:\n1.A person is about to be hanged for a fake crime.\n2.You have the opportunity to save the person from "
              "hanging\n3.You have to guess a word correctly.\n4.The word will be displayed with blank spaces and a hint will be"
              " provided.\n5.You get few chances to guess the word which will be mentioned at the time of guessing.\nFor every wrong guess"
              "you loose one chance\n6.Good Luck with "
              "game! Save the person\n")

        print("To start the game press 1 or press 0 to exit")
        option = int(input())
        if(option == 1):
            time.sleep(0.3)
            obj = Guess()
            obj.game()

        elif(option == 0):
            time.sleep(0.3)

            while True:
                print("Are you sure you want to exit? 'y' for yes 'n' for no")
                option2 = input()
                if(option2.lower() == 'y'):
                    exit(0)
                elif(option2.lower() == 'n'):
                    break
                else:
                    print("Invalid option!!! Enter correct option.")

        else:
            time.sleep(0.3)
            print("Invalid option!!! Enter correct option.")

