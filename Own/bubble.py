from tkinter import *
# from turtle import Turtle, Screen
from turtle import RawTurtle
# from turtle import Turtle
# import time
# import random


window = Tk()
window.title("Bubble...")
window.config(padx=50, pady=50)
# screen = Screen()
# screen.tracer()

canvas = Canvas(width=500, height=500, bg="white")
canvas.grid()


class Bubble(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color("red")
        self.speed("fastest")

bubble_list = []

def create_bubble():
    global bubble_list, food1, food2, food3, food4, food5
    food1 = Bubble(canvas)
    food2 = Bubble(canvas)
    food3 = Bubble(canvas)
    food4 = Bubble(canvas)
    food5 = Bubble(canvas)

    food1.goto(-220, 0)
    food2.goto(-120, 0)
    food3.goto(120, 0)
    food4.goto(220, 0)
    food5.goto(0, 0)

    bubble_list = [food1, food2, food3, food4, food5]

button_create = Button(text="Create Bubble", command=create_bubble)
button_create.grid(column=3, row=1)

def bubble_blast():
    global bubble_list
    # Check if any of the food items are visible, and hide the first visible one
    for food in bubble_list:
        if food.isvisible():
            food.hideturtle()
            break
    


button_blast = Button(text="Activate Me", command=bubble_blast)
button_blast.grid(column=1, row=1)
# time.sleep(10)
# screen.listen()
# screen.onkey(bubble_blast, "Enter")    

# screen = Screen()
# time.sleep(1)
# screen.exitonclick()




window.mainloop()

