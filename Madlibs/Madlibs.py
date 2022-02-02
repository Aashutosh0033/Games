#Madlibs : A word game where one player prompts another for a list of words to substitute for a blank in a story


class A1:
    def func(self):
        self.wd1 = input("Adjective: ")
        self.wd2 = input("Adjective: ")
        self.wd3 = input("Type of bird: ")
        self.wd4 = input("Room in house: ")
        self.wd5 = input("Verb(past   tense): ")
        self.wd6 = input("Verb: ")
        self.wd7 = input("Relative's name: ")
        self.wd8 = input("Noun: ")
        self.wd9 = input("A liquid: ")
        self.wd10 = input("Verb ending in 'ing' ")
        self.wd11 = input("Part of the body(plural)")
        self.wd12 = input("Plural noun: ")
        self.wd13 = input("Verb ending in 'ing': ")
        self.wd14 = input("Noun: ")

    def display( self):
        print(f"It was a {self.wd1}, cold November day. I woke up to the {self.wd2} smell of {self.wd3} roasting in the {self.wd4} downstairs.I "
        f"{self.wd5} down the stairs to see if I could help {self.wd6} the dinner. My mom said \"See if {self.wd7} needs a fresh {self.wd8}. "
        f"{self.wd9}.\" So I carried a tray of glasses full of {self.wd10} into the {self.wd11} room. When I got there I couldn't believe"
        f"my {self.wd12}! There were {self.wd13} {self.wd14} on the ")





if __name__ == '__main__':

    obj = A1()
    obj.func()
    obj.display()


