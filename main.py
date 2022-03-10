import pandas as pd
from turtle import Turtle, Screen

FONT = 'Arial', 5, 'bold'
data = pd.read_csv("50_states.csv")
image = "blank_states_img.gif"

screen = Screen()
screen.setup(width=725, height=500)
screen.addshape(image)

image_screen = Turtle()
image_screen.penup()
image_screen.shape(image)

t = Turtle()
t.penup()
t.hideturtle()

all_states = data.state.to_list()
states_placed = []


while len(states_placed) < 50:
    answer = screen.textinput(title=f"({len(states_placed)}/50) Guess the state", prompt="Type a state name:").title()

    if answer in all_states:
        chosen_state = data[data.state == f"{answer}"]
        x = int(chosen_state.x)
        y = int(chosen_state.y)
        t.goto(x, y)
        t.write(f"{answer}", font=FONT)
        states_placed.append(chosen_state)
        all_states.remove(answer)

    elif answer == "exit".title():
        break

states_to_learn = {
    "state": all_states
}
learn_data = pd.DataFrame(states_to_learn)
learn_data.to_csv("states_to_learn.csv")

screen.exitonclick()
