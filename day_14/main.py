import random
from art import logo
from art import vs
from game_data import data

def get_players():
    player_1 = random.randint(0, len(data)-1)
    player_2 = random.randint(0, len(data)-1)
    while player_1 == player_2:
        player_2 = random.randint(0, len(data)-1)
    return [data[player_1],data[player_2]]
# compare the two players
def check_winner():
    player = get_players()
    print(f"Compare A: {player[0]['name']}, {player[0]['description']}, from {player[0]['country']}")
    print(vs)
    print(f"Compare B: {player[1]['name']}, {player[1]['description']}, from {player[1]['country']}\n\n")
    print("---------------------------------------------------------------------------------------")
    play = input("Who has more followers? Type 'A' or 'B': ").lower()
    if play == 'a':
        if player[0]['follower_count'] > player[1]['follower_count']:
            return True
        else:
             return False
    elif play == 'b':
         if player[1]['follower_count'] > player[0]['follower_count']:
            return True
         else:
             return False
    return False
# calculat scores
def calculate_score():
    if check_winner() == True:
        return 1
    else:
        return 0
def main():
    print(logo)
    score = 0
    while check_winner() != False:
        get_players()
        check_winner()
        score += calculate_score()
        print("Score ===> ",score)
       
    print(f"That is wrong. Final score is : {score}")

main()
