import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correctly_guessed_states = []

while len(correctly_guessed_states) < 50:
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in correctly_guessed_states]
        states_to_learn_df = pandas.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_learn.csv")

        for state in states_to_learn:
            missing_state = data[data.state == state]
            missing_state_name = turtle.Turtle()
            missing_state_name.color("red")
            missing_state_name.hideturtle()
            missing_state_name.penup()
            missing_state_name.goto(int(missing_state.x.iloc[0]), int(missing_state.y.iloc[0]))
            missing_state_name.write(state, align="center", font=("Arial", 12, "normal"))
        screen.update()
        break
    elif answer_state in all_states and answer_state not in correctly_guessed_states:
        correctly_guessed_states.append(answer_state)

        correct_state = data[data.state == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(correct_state.x.iloc[0]), int(correct_state.y.iloc[0]))
        state_name.write(answer_state, align="center", font=("Arial", 12, "normal"))

    answer_state = screen.textinput(title=f"{len(correctly_guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()

screen.mainloop()
