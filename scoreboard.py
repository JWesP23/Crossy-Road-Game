from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, message, position, message_color, is_level_counter):
        super().__init__()
        self.message = message
        self.position = position
        self.message_color = message_color
        self.penup()
        self.hideturtle()
        self.color(self.message_color)
        self.setpos(self.position)
        self.write(self.message,align="center",font= FONT)
        if is_level_counter:
            self.level = 0
            self.append_level(1)

    def append_level(self, lvl_increase):
        self.clear()
        self.level += lvl_increase
        self.color(self.message_color)
        self.setpos(self.position)
        self.write(self.message + str(self.level),align="center",font= FONT)