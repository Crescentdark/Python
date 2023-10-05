from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))

screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
