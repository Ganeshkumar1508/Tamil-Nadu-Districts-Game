import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Tamil Nadu District Game")
image = "TamilNadu-District.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("districts_data.csv")
all_districts = data.districts.to_list()
guessed_districts = []

while len(guessed_districts) < 32:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/32 districts correct",
                                    prompt="What's another state's name ?").title()
    print(answer_district)

    if answer_district == "Exit":
        missing_districts = []
        for district in all_districts:
            if district not in guessed_districts:
                missing_districts.append(district)
        new_data = pd.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")
        break

    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.districts == answer_district]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(answer_district)

screen.exitonclick()

