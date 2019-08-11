import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    img_tt = turtle.Turtle()
    img_tt.shape("turtle")
    img_tt.color("white")
    img_tt.speed(2)
    for i in range(1,37):
        draw_square(img_tt)
        img_tt.right(10)

    """
    draw_square(img_tt)
    angle = turtle.Turtle()
    angle.shape("arrow")
    angle.color("black")
    angle.circle(100)
    window.exitonclick()
    """

draw_art()