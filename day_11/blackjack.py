import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_card = [cards[random.randint(0,len(cards)-1)], cards[random.randint(0,len(cards)-1)]]
player_card = [cards[random.randint(0,len(cards)-1)], cards[random.randint(0,len(cards)-1)]]
# Get a deal for the player
def deal():
    player_card.append(cards[random.randint(0,len(cards)-1)])
    # if deals card is less than or equal to 16 make add a card
    if sum(dealer_card) <= 16:
         dealer_card.append(cards[random.randint(0,len(cards)-1)])

def play(continue_playing):
    print(logo)
    if continue_playing == 'y':
        deal()

def main():
    continue_playing = 'y'
    while continue_playing != 'n' and (sum(player_card) < 21 and sum(dealer_card) < 21):
         print(f"Your cards: {player_card}, current score: {sum(player_card)}")
         print(f"Computer's first card: {dealer_card[0]}")
         continue_playing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
         if sum(player_card) < 21 and sum(dealer_card) < 21:
             play(continue_playing)

    if sum(player_card) >= 21:
        print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
        print(f"Computer's final hand: {dealer_card}, final score: {sum(dealer_card)}")
        print("You went over. You lose!")
    if sum(dealer_card) >= 21: 
        print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
        print(f"Computer's final hand: {dealer_card}, final score: {sum(dealer_card)}")        
        print("You Won!")

main()



