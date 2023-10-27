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
    chosen_color = random(4)
    gambler.append([Deck[chosen_card][chosen_color]])
    valueofCards(gambler)
    #print(f"{gambler[-1][-1]} of {gambler[-1][-2]}")
    #Add a drew this card message
    
#Deals out random cards from the deck and stores
#in specified list
    
def valueofCards(gambler):
    global Dealervalue
    global Dealerstring
    global Playervalue
    global Playerstring
    
    if gambler == Dealer:
        current_value = Dealervalue
        current_string = Dealerstring
    elif gambler == Player:
        current_value = Playervalue
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
    
def hitorStay(Player):
    print("Do you want to hit or stay?")
    answer = input("1: Hit 2: Stay ")
    if answer == "1":
        print(f"Player draws another card.")
        dealCards(Player)
    elif answer == "2":
        print(f"Player stays at the current hand, which is {Playervalue}.")
    else:
        print("/n")
        print("Incorrect input please pick 1 or 2.")
    #Options for the player after first draw.
    #Call bust function after dealt cards.

def hitorStayNPC(NPC):
    #Try to make it so NPC string combine with value
    #So that we get tex: Dealervalue when we input Dealer
    if Dealervalue < 15 and Dealervalue > 10:
        Hitchance = (2)
        #50% chance of drawing another card
    elif Dealervalue > 15:
        Hitchance = (4)
        #25% chance of drawing another card
    elif Dealervalue > 17 and Dealervalue < 20:
        Hitchance = (100)
        #1% chance of drawing another card
    
        
    
    
        
    
    
dealCards(Player)
valueofCards(Player)
print(Playervalue)
