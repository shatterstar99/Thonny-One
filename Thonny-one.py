from random import randint
Deck = {1:["One",(1,"Heart","One"),(1,"Spade","One"),(1,"Club","One"),(1,"Diamond","One")],2:["Two",(2,"Heart","Two"),(2,"Spade","Two"),(2,"Club","Two"),(2,"Diamond","Two")],3:["Three",(3,"Heart","Three"),(3,"Spade","Three"),(3,"Club","Three"),(3,"Diamond","Three")],4:["Four",(4,"Heart","Four"),(4,"Spade","Four"),(4,"Club","Four"),(4,"Diamond","Four")],5:["Five",(5,"Heart","Five"),(5,"Spade","Five"),(5,"Club","Five"),(5,"Diamond","Five")],6:["Six",(6,"Heart","Six"),(6,"Spade","Six"),(6,"Club","Six"),(6,"Diamond","Six")],7:["Seven",(7,"Heart","Seven"),(7,"Spade","Seven"),(7,"Club","Seven"),(7,"Diamond","Seven")],8:["Eight",(8,"Heart","Eight"),(8,"Spade","Eight"),(8,"Club","Eight"),(8,"Diamond","Eight")],9:["Nine",(9,"Heart","Nine"),(9,"Spade","Nine"),(9,"Club","Nine"),(9,"Diamond","Nine")],10:["Ten",(10,"Heart","Ten"),(10,"Spade","Ten"),(10,"Club","Ten"),(10,"Diamond","Ten")],11:["Jack",(10,"Heart","Jack"),(10,"Spade","Jack"),(10,"Club","Jack"),(10,"Diamond","Jack")],12:["Queen",(10,"Heart","Queen"),(10,"Spade","Queen"),(10,"Club","Queen"),(10,"Diamond","Queen")],13:["King",(10,"Heart","King"),(10,"Spade","King"),(10,"Club","King"),(10,"Diamond","King")]}
Player = []
#This is the players hand, he starts with zero cards.
Dealer = []
#This is the players hand, he starts with zero cards.

def random(limit):
    randomvalue = randint(1,limit)
    return randomvalue
#Function gets an input(like the length of the list
#and returns a random value between 1 and the input.
def dealCards():
    Player.append[Deck[random(len(Deck))][random(4)]]
    Player.append[Deck[random(len(Deck))][random(4)]]

