import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 Correct States", prompt="What's your guess?").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        correct_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

states_to_learn = []
for state in states:
    if state not in correct_states:
        states_to_learn.append(state)
states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")