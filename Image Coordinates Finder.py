import turtle

screen = turtle.Screen()
screen.title("Tamil Nadu District Game")
image = "TamilNadu-District1.gif"

screen.addshape(image)
turtle.shape(image)


def get_mouse_click_corr(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_corr)
turtle.mainloop()