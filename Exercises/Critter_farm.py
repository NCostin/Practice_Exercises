#Critter Caretaker
#A virtual pet to care for

import random

class Critter(object):
    """A virtual pet"""


    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom


    def __str__(self):
        print(f"\n{self.name} properties are: \n")
        rep = "\nHunger: " + str(self.hunger) + "\n"
        rep += "\nBoredom:" + str(self.boredom) + "\n"

        return rep
        
    @staticmethod
    def randomness():
        return random.randrange(0,20)
        
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def food_quantity():
        print \
        ('''
        1 - Little
        2 - More
        3 - Much more
        ''')
        
        quantity = input("How much food does your critter should get?: ")
        
        if quantity == "1":
            print("Brruppp. Thank you.")
            return 2
        elif quantity == "2":
            print("Brruppp. Thank you.")
            return 4
        elif quantity == "3":
            print("Brruppp. Thank you.")
            return 6
        else:
            print("\nSorry, but", quantity, "isn't a valid choice." )
            return 0



    def play_time():
        print \
         ('''
         1 - Not too long
         2 - A little longer
         3 - I could do this all day
         ''')
            
        time = input("How long do you want to play with your critter?: ")
        
        if time == "1":
            print("Wheee!")
            return 2 
        elif time == "2":
            print("Wheee!")
            return 4
        elif time == "3":
            print("Wheee!")
            return 6
        else:
            print("\nSorry, but", time, "isn't a valid choice." )
            return 0


        
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
        
    def eat(self,food):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        
    def play(self,fun):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    
    crit1 = Critter("John", hunger = Critter.randomness(), boredom = Critter.randomness())
    crit2 = Critter("Andrew",hunger = Critter.randomness(), boredom = Critter.randomness())
    crit3 = Critter("Jack",hunger = Critter.randomness(), boredom = Critter.randomness())
    crit4 = Critter("Mary",hunger = Critter.randomness(), boredom = Critter.randomness())
    crit5 = Critter("Austin",hunger = Critter.randomness(), boredom = Critter.randomness())
    crit6 = Critter("Angela",hunger = Critter.randomness(), boredom = Critter.randomness())

    all_critters = [crit1, crit2, crit3, crit4, crit5, crit6]
    
    choice = None
    while choice != "0":
        print \
        (f"""
        Critter Caretaker
        
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter

        """)
        
        choice = input("Choice: ")
        print()
        
        #exit
        if choice == "0":
            print("Good-bye.")
            
        #listen to your critter
        elif choice == "1":
            for crit in all_critters:
                crit.talk()
        
        #feed your critter
        elif choice == "2":
            food = Critter.food_quantity()
            for crit in all_critters:
                crit.eat(food)
            
        #play with your critter
        elif choice == "3":
            fun = Critter.play_time()
            for crit in all_critters:
                crit.play(fun)


        #secret choice
        elif choice == "xray":
            print(f"Congrats, you found the secret way to access the exact values of your critter boredom and hunger!!\n")
            for crit in all_critters:
                print(crit)
            
        #some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice." )


main()
("\n\nPress the enter key to exit.")