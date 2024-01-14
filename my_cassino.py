from art import logo
from art import welcome_logo
from art import roulette_logo
import random
import os

#FUNCTION TO START THE PYSSINO
def start():
    print(welcome_logo)
    game = input("Welcome to PYssino\nType:\n 1 to play Blackjack\n 2 to play roullete (W.I.P)\n")
    if game == "1":
        os.system('cls')
        blackjack()
    if game == "2":
        os.system('cls')
        roullete()

#ROULLETE GAME (W.I.P)
def roullete():
    print(roulette_logo)
    rules2 = input("Roullete is in implementation. Play blackjack? Y or N: ").lower()
    if rules2 == "y":
        blackjack()
    
    

    rules2 = input('''       # RULES OF THE GAME 
    Each spin of the wheel provides a multitude of options for the player. A player may bet on single numbers, rows of numbers,
    or on adjacent numbers. A player also may play colors, odd or even numbers, among others. A bet on a single number pays 
    35 to 1, including the 0 and 00. Bets on red or black, odd or even pay 1 for 1, or even money.
    The roullete has a single 0 along with the standard 36 numbers
    Single number bet pays 35 to 1. Also called “straight up.”
    Double number bet pays 17 to 1. Also called a “split.” 
    Three number bet pays 11 to 1. Also called a “street.”
    Four number bet pays 8 to 1. Also called a “corner bet.”
    Five number bet pays 6 to 1. Only one specific bet which includes the following numbers: 0-00-1-2-3.
    Six number bets pays 5 to 1. Example: 7, 8, 9, 10, 11, 12. Also called a “line.”
    Twelve numbers or dozens (first, second, third dozen) pays 2 to 1.
    Column bet (12 numbers in a row) pays 2 to 1. 
    18 numbers (1-18) pays even money. 
    18 numbers (19-36) pays even money. 
    Red or black pays even money. 
    Odd or even bets pay even money.
    reds: 1 3 5 7 9 12 14 16 18 19 21 23 25 27 30 32 34 36
    blacks 2 4 6 8 10 11 13 15 17 20 22 24 26 28 29 31 33 35
    PRESS ENTER TO CONTINUE: '''
           )

def blackjack():
    rules = input("You want to read the rules of blackjack? Y or N: ").lower()
    if rules == "y":
        rules = input("""
              Object of the Game
                Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
              Card Values/scoring
                It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.
              The Dealer's Play
                When the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. 
                If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, 
                at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21),
                the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has
                the option of taking one or more cards.
                PRESS ENTER TO CONTINUE: """
              )
        
    os.system('cls')
    print(logo)
    cards = [
            2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 11, 11, 11, 11, 6, 6 ,6 ,6, 7,
            7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
            ]
    bank = 1000
    not_broke = True

    #FUNCTION TO CALCULATE TOTAL VALUE IN HAND, IT HAS A ACE CHECK A = (11 OR 1) IN BLACKJACK
    def total_value(hand):
        x = int(sum(hand))
        if 11 in hand and x >21:   
            for _ in hand:
                if _ == 11:
                    hand.remove(11)
                    hand.append(1)
        return sum(hand)
    
    #FUNCTION TO GAMEOVER
    def gameover(gold):
        if gold <= 0:                      
            print("_________________________________________________\n")
            brokee = input("You are broke!\nPlay again? Y or N: ").lower()
            if brokee == "y":
                os.system('cls')
                start()

    while not_broke:
        print(f"Your bank = {bank}")
        dealer_hand = []
        player_hand = []

        # GETTING BID FROM USER
        bidlist = [1, 5, 25, 50, 100, 500, 1000, 5000]
        bid = input("You can only bid 1, 5, 25, 50, 100, 500, 1000, 5000 or Allin\nPlace your bid: ").lower()   
        if bid == "allin":
            bid = bank
        else:
            bid = int(bid)         
            while bid not in bidlist or bid > bank:
                os.system('cls')
                bid = int(input(f"You can only bid 1, 5, 25, 50, 100, 500 or 1000. You must have the value in bank to bid.\nYour bank is {bank}")) 
        os.system('cls')        
        

        # GIVING STARTER HANDS
        dealer_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))    
        player_hand.append(random.choice(cards)) 
        print(f"Dealer first card = {dealer_hand[0]}")
        print(f"Your cards = {player_hand}")
        total_D = total_value(dealer_hand)
        total_P = total_value(player_hand)
        

        # PLAYER HAND
        mounting_hand = True
        while mounting_hand:
            choice = input(f"Your total is {total_P}\nType 1 to Hit or 2 to Stand: ")
            os.system('cls')
            if choice == "1":
                print(f"Dealer cards = {dealer_hand} Dealer total is {total_D}")
                player_hand.append(random.choice(cards))  
                total_P = total_value(player_hand)
                print(f"Your cards = {player_hand}")
                if total_P >= 21:
                    mounting_hand = False
            else:
                total_P = total_value(player_hand)
                mounting_hand = False

        # CHECKING IF PLAYER PASSED 21
        if total_P > 21:
            print(f"Your total is {total_P}\nYou Bust! Dealer Wins!")
            bank = bank - bid
            gameover(bank)

        # MAKING DEALER HAND
        elif total_P <= 20:
            while total_D <= total_P or total_D <= 16:    
                dealer_hand.append(random.choice(cards))
                total_D = total_value(dealer_hand)
                print(f"Dealer cards = {dealer_hand}")

        # CHECKING WINNER         
        if total_P > total_D and total_P != total_D and total_P <= 21 or total_D > 21:
            print(f"Dealer total is  {total_D}\nYour total is {total_P}")
            print("You win!")
            print("_________________________________________________\n")
            bank = bank + bid
        elif total_D >= total_P and total_D <=21:
            print(f"Dealer total is  {total_D}\nYour total is {total_P}")
            print("Dealer wins!")
            bank = bank - bid
            if bank <= 0:                      
                gameover(bank)

start()