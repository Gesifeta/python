from turtle import Turtle, Screen
import pandas
import random

screen = Screen()
turtle = Turtle()

screen.listen()
screen.title("U.S. State Guessing Game")
colors =["red","blue","yellow","green","purple","orange","pink"]
states_image = "blank_states_img.gif"
screen.addshape(states_image)
turtle.pencolor("yellow")
turtle.shape(states_image)

# U.S. State lists

state_lists = pandas.read_csv("./50_states.csv")

def guess_state():
    state_guess = screen.textinput("Guessing State", "Enter your guess")
    return state_guess
guessed_state = guess_state()
all_state = state_lists["state"].to_list()
game_is_over = False
score = 0
score_board = Turtle()
score_board.hideturtle()
score_board.penup()

while not game_is_over:
    if guessed_state in all_state:
        score_board.clear()
        score += 1
        score_board.goto(0, 270)
        score_board.write(f"Score: {score}/50", align="center", font=("Arial", 20, "bold"))
        new_state = Turtle()
        new_state.penup()
        new_state.shape("turtle")
        new_state.hideturtle()
        new_state.color(random.choice(colors))
        new_state.goto(state_lists[state_lists.state == guessed_state]["x"].to_list()[0],state_lists[state_lists.state == guessed_state]["y"].to_list()[0])
        new_state.write(guessed_state,False,align="center",font=("Arial",10,"bold"))
        guessed_state = guess_state()
    if guessed_state == "exit":
        game_is_over = True


screen.mainloop()