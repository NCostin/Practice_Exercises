class Television(object):
    """Television simulation"""

    def __init__(self, channel_number= None,volume_level= 50):
        self.channel_number = channel_number
        self.volume_level = volume_level

    def change_channel_number(self):
        number = input("What channel do you want to view (0-85)?\n")
        try:
            number = int(number)
        except:
            pass
        if number in range(0,85+1):
            self.channel_number = number
            print("You changed the channel")
        else:
            print(f"Sorry, {number}, is out of range or wrong ")
            
    def change_volume_level(self):
        level = input("Do you want to raise or lower the volume?\n")
        if level == "raise":
            self.volume_level += 20
            if self.volume_level > 100:
                self.volume_level = 100
        elif level == "lower":
            self.volume_level -= 20
            if self.volume_level < 0:
                self.volume_level = 0
        else:
            print(f"\nSorry, {level}, is wrong\n")
            
        
def main():
    tv = Television()
    
    choice = None
    while choice != "0":
        print \
        ("""
        This is you remote control, decide what do you want to do:
        0 - Quit
        1 - Enter the channel number
        2 - Raise or Lower the volume level
        
        """)
        
        print(f"Right now, the channel number is: {tv.channel_number}")
        print(f"Right now, the volume level is: {tv.volume_level}")
        
        choice = input("\nChoice: ")
        
        if choice == "0":
            print("Good-bye.")
            
        elif choice == "1":
            tv.change_channel_number()
            
        elif choice == "2":
            tv.change_volume_level()
        
        else:
            print(f"Sorry, but {choice}, isn't a valid choice." )


main()
("\n\nPress the enter key to exit.")



