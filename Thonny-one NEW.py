from random import randint
Deck = {1:["Ace",(1,11,"Heart","Ace"),(1,11,"Spade","Ace"),(1,11,"Club","Ace"),(1,11,"Diamond","Ace")],2:["Two",(2,"Heart","Two"),(2,"Spade","Two"),(2,"Club","Two"),(2,"Diamond","Two")],3:["Three",(3,"Heart","Three"),(3,"Spade","Three"),(3,"Club","Three"),(3,"Diamond","Three")],4:["Four",(4,"Heart","Four"),(4,"Spade","Four"),(4,"Club","Four"),(4,"Diamond","Four")],5:["Five",(5,"Heart","Five"),(5,"Spade","Five"),(5,"Club","Five"),(5,"Diamond","Five")],6:["Six",(6,"Heart","Six"),(6,"Spade","Six"),(6,"Club","Six"),(6,"Diamond","Six")],7:["Seven",(7,"Heart","Seven"),(7,"Spade","Seven"),(7,"Club","Seven"),(7,"Diamond","Seven")],8:["Eight",(8,"Heart","Eight"),(8,"Spade","Eight"),(8,"Club","Eight"),(8,"Diamond","Eight")],9:["Nine",(9,"Heart","Nine"),(9,"Spade","Nine"),(9,"Club","Nine"),(9,"Diamond","Nine")],10:["Ten",(10,"Heart","Ten"),(10,"Spade","Ten"),(10,"Club","Ten"),(10,"Diamond","Ten")],11:["Jack",(10,"Heart","Jack"),(10,"Spade","Jack"),(10,"Club","Jack"),(10,"Diamond","Jack")],12:["Queen",(10,"Heart","Queen"),(10,"Spade","Queen"),(10,"Club","Queen"),(10,"Diamond","Queen")],13:["King",(10,"Heart","King"),(10,"Spade","King"),(10,"Club","King"),(10,"Diamond","King")]}
#Deck contains all the possible cards.
Gamblers = {"Player":{"Hand":[],"Value": 0},"Dealer":{"Hand":[],"Value": 0}}
Player = []
#This is the players hand, he starts with zero cards.
Playervalue = 0
#This is the starting value of the players hand.
Playerstring = []
#This is a list that stores the hand in string format.
Dealer = []
#This is the players hand, he starts with zero cards.
Dealervalue = 0
#This is the starting value of the dealers hand
Dealerstring = []
#This is a list that stores the hand in string format.

#Future idea: possibly put those global variables in a dict.

def random(limit):
    randomvalue = randint(1,limit)
    return randomvalue
#Function gets an input(like the length of the list
#and returns a random value between 1 and the input.

def dealCards(gambler):
    chosen_card = random(len(Deck))
    chosen_color = random(len(Deck[chosen_card])-1)
    gambler.append([Deck[chosen_card][chosen_color]])
    drawncard = Deck[chosen_card][chosen_color]
        #removes the card from the dictionary after being drawn.

    if gambler == Player:
        print(f"Player is dealt {Deck[chosen_card][chosen_color][-1]} of {Deck[chosen_card][chosen_color][-2]}")
    elif gambler == Dealer:
        print(f"Dealer is dealt {Deck[chosen_card][chosen_color][-1]} of {Deck[chosen_card][chosen_color][-2]}")
        
    (Deck[chosen_card]).remove(drawncard)
    #removes the card from the dictionary after being drawn.
    valueofCards(gambler)
    
    
#Deals out random cards from the deck and stores
#in specified list
    
def valueofCards(gambler):
    global Dealervalue
    global Dealerstring
    global Playervalue
    global Playerstring
    
    if gambler == Dealer:
        current_value = 0
        current_string = Dealerstring
    elif gambler == Player:
        current_value = 0
        current_string = Playerstring
        
    for tpl in gambler:
        card_string = (f"{tpl[0][-1]} of {tpl[0][-2]}")
        if card_string not in current_string:
            current_string.append(card_string)
        #Supposed to store the strings of tuple in list
        #to print it out later
        if len(tpl[0]) > 3: #Only the Ace tuples are longer than 3
            if current_value+ tpl[0][1] > 21:
                current_value += tpl[0][0]
                #if player would become bust when 11 is added,adds the value 1 instead,
            else:
                current_value += tpl[0][1]
                #Otherwise Ace adds 11 points.
        else:
            current_value += tpl[0][0]
    if gambler == Dealer:
        if current_value == 21:
            current_value = "Thonny-one"
            print("Dealer hit Thonny-one!")
        elif current_value > 21:
            current_value = "Bust"
            print("Dealer went bust!")
        Dealervalue = current_value
        
    elif gambler == Player:
        if current_value == 21:
            current_value = "Thonny-one"
            print("Player hit Thonny-one!")
        elif current_value > 21:
            current_value = "Bust"
            print("Player went bust!")
        Playervalue = current_value
    
    
def hitorStay(Player):
    hitloop = True
    
    while hitloop != False:
        print("")
        print("Do you want to hit or stay?")
        answer = input("1: Hit 2: Stay ")
        print("")
        if answer == "1":
            print(f"You draw another card.")
            dealCards(Player)
            print(f"For a new value of {Playervalue}")
            if Playervalue == "Bust":
                hitloop = False
        elif answer == "2":
            valueofCards(Player)
            print(f"You stay at the current hand, which is {Playerstring}.")
            hitloop = False
        else:
            print("/n")
            print("Incorrect input please pick 1 or 2.")
    #Options for the player after first draw.
    #Call bust function after dealt cards.

def hitorStayNPC(NPC):
    #Try to make it so NPC string combine with value
    #So that we get tex: Dealervalue when we input Dealer
    
    if Dealervalue == "Bust" or Dealervalue == "Thonny-one":
       print(f"Dealer stays at the current hand of {Dealerstring}")
       #This function is to prevent syntax error
       #with comparing string and integer below.
       
    if Dealervalue < 16 and Dealervalue > 10:
        Hitchance = (2)
        #50% chance of drawing another card
    elif Dealervalue > 15:
        Hitchance = (4)
        #25% chance of drawing another card
    elif Dealervalue > 17 and Dealervalue < 20:
        Hitchance = (100)
        #1% chance of drawing another card
    elif Dealervalue <= 10:
        Hitchance = (1)
       #100% chance of drawing another card
        
    Hitrng = random(Hitchance)
    if Hitrng == 1:
        print("Dealer hits and draws another card")
        dealCards(Dealer)
        #activates if the random function gives back a hit
    else:
        print(f"Dealer stays at the current hand of {Dealerstring} with a value of {Dealervalue}")

def score():
    if Playervalue == "Thonny-one" and Dealervalue != Playervalue:
        winner = "Player"
    elif Dealervalue == "Thonny-one" and Playervalue != Dealervalue:
        winner = "Dealer"
    elif Dealervalue == "Bust" and Playervalue != "Bust":
        winner = "Player"
    elif Playervalue == "Bust" and Dealervalue != "Bust":
        winner = "Dealer"    
    elif Playervalue > Dealervalue and Playervalue < 21:
        winner = "Player"
    elif Dealervalue > Playervalue and Dealervalue < 21:
        winner = "Dealer"
    

    elif Dealervalue == Playervalue:
        winner = "Draw"

    return winner
        
def newGame():
    print("Welcome! I'll be your dealer today.")
    print("Would you like to start a round of Thonny-one? Y/N")
    answer = input()
    if answer == "y":
        print("Alright lets begin, good luck.")
        print("")
        dealCards(Player)
        dealCards(Player)
        print(f"For a value of {Playervalue}")
        
        print("")
        dealCards(Dealer)
        dealCards(Dealer)
        print(f"For a value of {Dealervalue}")
        
        print("")
        hitorStay(Player)
        print("")
        hitorStayNPC(Dealer)
        
        winner = score()
        if winner == "Draw":
            print("")
            print(f"Player hand is worth {Playervalue} and Dealer hand is worth {Dealervalue}.")
            print("It's a draw!")
        else:
            print("")
            print(f"Player hand is worth {Playervalue} and Dealer hand is worth {Dealervalue}.")
            print(f"The winner is {winner}!")
    elif answer == "n":
        print("Maybe next time. Have a good day.")
    else:
        print("Sorry was that a yes or a no?")
newGame()        
    
    
        


    
    
        
    
    
        
    
    
