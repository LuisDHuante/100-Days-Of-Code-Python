from this import s
import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S Staes Game")
image = "blank_states_img.gif"
t = turtle.Turtle()
t.hideturtle()
t.penup()
screen.addshape(image)
turtle.shape(image)

game_is_on = True
score = 0
states = df.state.to_list()
correct_states = []

while score < 50:
    answer_state = screen.textinput(title="Guess the state", prompt=f"{score}/50 states correct").title()


    #Exit
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_states]
        break

    #Game
    if answer_state in states:
        correct_states.append(answer_state)
        state_data = df[df.state == df.answer_state]
        turtle.goto(int(state_data.x), int(state_data.y))

        #Or we can use state_data.state-item()
        turtle.write(answer_state)
        score += 1

    #Converting missing states to csv
new_data = pd.DataFrame(missing_states)
new_data.to_csv("to_learn.csv")

