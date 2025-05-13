import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)_____
       | ________)
       |_________
       __________)
      (_____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
# Assign options into lists
picks = [rock,paper,scissors]
human = int(input("Enter your choice. "))
computer = random.randint(0,2)
print("Computer chose\n",picks[computer])
print("You chose\n",picks[human])
if picks[computer] == picks[human]:
    print("Draw")
elif picks[computer] == rock and picks[human] == paper or scissors:
    print("You Won! ")
elif picks[computer] == paper and picks[human] == rock:
    print("You Lost! ")
elif picks[computer] == scissors and picks[human] == paper:
    print("You Won! ")
else:
    print("Invalid input, YOu lost!")