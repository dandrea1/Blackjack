############### Blackjack Project #####################
import random
import art
from replit import clear
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


#Define Function to turn Ace from 11 to 1
def change_ace_value(hand):
    for n, i in enumerate(hand):
        if i == 11:
            hand[n] = 1

#Define Function for Computer GamePlay
def computer_game_play(c_score, c_hand, p_score):
    while c_score < 17:
        c_hand.append(random.choice(cards))
        c_score = sum(c_hand)
        print(f"The dealer's hand is now {c_hand} and the score is {c_score}")
    if c_score == 21:
        print(f"You Lose, the computer got blackjack.\nComputer final hand: {c_hand}, final score:{c_score}  \nPlayer Final Score:{p_score}")
        game_play()
    elif c_score > 21:
        print(f"You win! The dealer busted\nComputer final hand: {c_hand}, final score:{c_score}  \nPlayer Final Score:{p_score}")
        game_play()
    else:
        if c_score > p_score:
            print(f"You win!\nComputer final hand: {c_hand}, final score:{c_score}  \nPlayer Final Score:{p_score}")
            game_play()
        elif c_score == p_score:
            print(f"You win!\nComputer final hand: {c_hand}, final score:{c_score}  \nPlayer Final Score:{p_score}")
            game_play()
        else:
            print(f"You win!\nComputer final hand: {c_hand}, final score:{c_score}  \nPlayer Final Score:{p_score}")
            game_play()

def game_play():   
    play = input("Do you want to play blackjack? Type 'y' or 'n': ")
    if play == 'n':
        print("Thanks for playing.")
    else:
        clear()
        print(art.logo)
        #Declare Required Variables
        player_hand = []
        player_score = 0
        computer_hand = []
        computer_score = 0
        keep_playing = True

        #Deal Cards to Computer and Player
        for card in range(0,2):
            player_hand.append(random.choice(cards))
            computer_hand.append(random.choice(cards))

        #Calculate Scores
        player_score = sum(player_hand)
        computer_score = sum(computer_hand)

        if computer_score == 21:
            print(f"You lose. Computer got blackjack. \nComputer final hand: {computer_hand}, final score:{computer_score}  \nPlayer Final Hand:{player_hand} ,final score:{player_score}")
            keep_playing = False
            game_play()
        elif player_score == 21:
            print(f"You win. You got a blackjack.\nComputer final hand: {computer_hand}, final score:{computer_score}  \nPlayer Final Hand:{player_hand} ,final score:{player_score}")
            keep_playing = False
            game_play()
        else: 
            print(f"Your hand is {player_hand} and you score is: {player_score}")
            print(f"The dealer's first card is {computer_hand[0]}")
            #print(f"Test:{computer_hand}, {computer_score}")
            #Player GamePlay
            while keep_playing == True:
                #Ask player if they want another card
                next_card = input("Type 'y' to get another card, type 'n' to pass:  ")
                if next_card == 'y':
                    player_hand.append(random.choice(cards))
                    player_score = sum(player_hand)
                    if player_score < 21:
                        print(f"Your hand is {player_hand} and you score is: {player_score}")
                    elif player_score == 21:
                        keep_playing = False
                        print("You got a blackjack. You won!\nComputer final hand: {computer_hand}, final score:{computer_score}  \nPlayer Final Hand:{player_hand} ,final score:{player_score}")
                        game_play()
                    elif player_score > 21:
                        if 11 not in player_hand:
                            print(f"You busted. You lose. \nComputer final hand: {computer_hand}, final score:{computer_score}  \nPlayer Final Hand:{player_hand} ,final score:{player_score}")
                            keep_playing = False
                            game_play()
                        else:
                            change_ace_value(hand=player_hand)
                            player_score = sum(player_hand)
                            print(f"Your hand is {player_hand} and you score is: {player_score}")
                            
                elif next_card == 'n':
                    computer_game_play(c_score = computer_score, c_hand = computer_hand, p_score = player_score)
                    keep_playing = False
game_play()






