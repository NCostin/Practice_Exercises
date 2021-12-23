# Blackjack
# From 1 to 7 players compete against a dealer

import cards, games     

class BJ_Card(cards.Card):

# extends the definition of what a card is by inheriting from cards.Card

    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):

# class is used to create a deck of blackjack cards.
# class is same as cards.Deck, it just overiddes cards.Deck.populate()
    #so that a new BJ_Deck object gets populated with BJ_Card objects

    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))
    

class BJ_Hand(cards.Hand):

# class is based on cards.Hand, is used for blackjack hands
# cards.Hand constructor is overidded and it's added a
    # name attribute to represent the name of hand owner
# it overiddes the inherited __str__() method to display the total point value of the hand

    """ A Blackjack Hand. """
    def __init__(self, name):               #constructorul clasei BJ_Hand
        super(BJ_Hand, self).__init__()     #constructorul clasei BJ_Hand, care preia din constructorul clasei cards.Hand()
        self.name = name                    #atributul nou din constructor

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
              t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):

# class is based on BJ_Hand and is used for blackjack players:

    """ A Blackjack Player. """
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

        
class BJ_Dealer(BJ_Hand):

# class is based on BJ_Hand and is used for the game blackjack dealer

    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):

# class is used to create a single object that represents a blackjack game
# the class contains the code for the main game loop in the method play()

    """ A Blackjack Game. """
    def __init__(self, names):                  #constructoru clasei BJ_Game
        self.players = []                       #se initializeaza lista players = []
        for name in names:                      #pt fiecare name in names:
                                                    #-se creeaza obiectul player = BJ_Player(name) cu parametrul name
                                                    #-listei players se adauga obiectul player
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")       #se creeaza obiectul dealer = BJ_Dealer("Dealer") 

        self.deck = BJ_Deck()                   #se creeaza obiectul deck = BJ_Deck
        self.deck.populate()                    #obiectul deck activeaza metoda populate()
        self.deck.shuffle()                     #obiectul shuffle activeaza metoda shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
           
    def play(self):
        # here the game loop is defined
        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first 

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()                    
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
        

def main():
    print("\t\tWelcome to Blackjack!\n")
    
    names = []                                      #se initializeaza lista cu numele
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8) #in variabila number se stocheaza nr. de jucatori, returnat de 
                                                                                    #games.ask_number()
    for i in range(number):                                                     #pt fiecare element din number:
                                                                                        # -name = numele jucatorului
                                                                                        # -numele jucatorului se ataseaza la lista names
        name = input("Enter player name: ")
        names.append(name)
    print()
        
    game = BJ_Game(names)                                                       #se creeaza un obiect care apartine clasei BJ_Game, ca si parametru este lista names

    again = None
    while again != "n":                                                         #atata timp cat again != "n" ruleaza game.play()
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")


