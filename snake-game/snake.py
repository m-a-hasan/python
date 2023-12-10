from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head.heading()) == RIGHT or int(self.head.heading()) == LEFT:
            self.head.setheading(UP)

    def down(self):
        if int(self.head.heading()) == RIGHT or int(self.head.heading()) == LEFT:
            self.head.setheading(DOWN)

    def left(self):
        if int(self.head.heading()) == UP or int(self.head.heading()) == DOWN:
            self.head.setheading(LEFT)

    def right(self):
        if int(self.head.heading()) == UP or int(self.head.heading()) == DOWN:
            self.head.setheading(RIGHT)
