import random

def is_prime(num):
    is_prime=True
    value = num-1
    if num == 0 or num == 2:
        return True
    while value > 1: 
        if num % value == 0:
            is_prime =False
            break
        value -= 1
    return is_prime
def guess_number(random_number):
    guess = int(input("Guess a number between 1 t0 100: "))
    if guess < random_number:
        print("Number too low: ")
    elif guess > random_number:
        print("Number too high: ")
    elif guess == random_number:
        print(f"You won , the correct number is {random_number}")
        return
    return random_number == guess

def play():
    random_number = random.randint(1,100)
    difficulty = input("Choose difficulty level (Easy/Hard)").lower()
    plays = 0
    if difficulty == "easy":
        plays = 10
    elif difficulty == "hard":
        plays = 5
    else:
        print("Invalid input")
        return
    while guess_number(random_number) == False:
        if plays == 0:
            print(f"You lost. The number was {random_number}")
            break
        guess_number(random_number)
        plays -= 1
        print(f"You have {plays} remaining to guess the game.")
play()

