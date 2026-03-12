import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
screen.setup(750, 550)
states = pd.read_csv('50_states.csv')
answer_state = screen.textinput(title = "Guess the States",prompt = "What's the name of U.S states?").title()
correct_answers = []
state_names = states.state.to_list()
while len(correct_answers) < 50:
    if answer_state == "Exit":
        missed_answers = [s for s in state_names if s not in correct_answers]
        missed_data = pd.DataFrame(missed_answers)
        missed_data.to_csv('missed_states.csv')
        break
    if answer_state in state_names and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_row = states[states.state == answer_state]
        x_cor = state_row.x.item()
        y_cor = state_row.y.item()
        t.goto(x_cor, y_cor)
        t.write(answer_state)
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 correct states", prompt="What's the name of another state?").title()






