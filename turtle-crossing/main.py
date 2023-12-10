import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CAR_INITIAL_SPEED = 5
CAR_SPEED_INCREMENT = 5
TOTAL_CARS_PER_SCREEN = 25
TOTAL_SCREENS = 4
CAR_OUT_SCREEN = -350


def create_fleet():
    car_fleet = []
    car_start_x = -SCREEN_WIDTH/2
    car_end_x = SCREEN_WIDTH/2
    for _ in range(TOTAL_SCREENS):
        for _ in range(TOTAL_CARS_PER_SCREEN):
            new_car = Car()
            new_car.place_car(start_screen=car_start_x, end_screen=car_end_x)
            car_fleet.append(new_car)
        car_start_x += SCREEN_WIDTH
        car_end_x += SCREEN_WIDTH
    return car_fleet


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move, key="Up")

car_speed = CAR_INITIAL_SPEED
screen_tracker = (SCREEN_WIDTH * 4) - (SCREEN_WIDTH / 2)

# Fleet setup
fleet = create_fleet()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for turtle_car in fleet:
        turtle_car.move(car_speed)

    screen_tracker -= car_speed

    # Turtle crossed
    if player.ycor() > 300:
        for car in fleet:
            car.goto(CAR_OUT_SCREEN, 0)
        fleet = create_fleet()
        player.reset_player()
        car_speed += CAR_SPEED_INCREMENT
        screen_tracker = (SCREEN_WIDTH * 4) - (SCREEN_WIDTH / 2)
        scoreboard.level_up()

    # Turtle crash
    for car in fleet:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # All cars passed
    if screen_tracker < 0:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
