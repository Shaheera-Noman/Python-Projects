# import tkinter as tk
# from turtle import RawTurtle, ScrolledCanvas

# def open_turtle_window():
#     turtle_window = tk.Toplevel(root)
#     canvas = ScrolledCanvas(turtle_window)
#     canvas.pack(fill=tk.BOTH, expand=True)
    
#     turtle = RawTurtle(canvas)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
    
# root = tk.Tk()
# root.title("Tkinter and Turtle")

# button = tk.Button(root, text="Open Turtle Window", command=open_turtle_window)
# button.pack(pady=20)

# root.mainloop()

# from turtle import Screen, Turtle

# def create_ball(x, y):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()

#     turtle.color("blue")
#     turtle.begin_fill()
#     turtle.circle(10)
#     turtle.end_fill()

# turtle = Turtle()
# screen = Screen()
# screen.title("Turtle: Horizontal Row of 5 Small Balls")

# # Set starting x-coordinate for the first ball
# start_x = -80

# for _ in range(5):
#     create_ball(start_x, 0)
#     start_x += 40  # Adjust the distance between balls

# screen.exitonclick()

# from tkinter import *
# from turtle import Turtle, Screen
# import time
# import random

# window = Tk()
# window.title("Bubble...")
# window.config(padx=50, pady=50)

# screen = Screen()
# screen.tracer()

# canvas = Canvas(width=500, height=500)

# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=2, stretch_wid=2)
#         self.color("red")
#         self.speed("fastest")

# food1 = Food()
# food2 = Food()
# food3 = Food()
# food4 = Food()
# food5 = Food()

# food1.goto(-220, 0)
# food2.goto(-120, 0)
# food3.goto(120, 0)
# food4.goto(220, 0)
# food5.goto(0, 0)

# def bubble_blast():
#     global food1, food2, food3, food4, food5
#     # Check if any of the food items are close to the turtle
#     if food1.distance(turtle) < 20:
#         food1.hideturtle()
#     elif food2.distance(turtle) < 20:
#         food2.hideturtle()
#     elif food3.distance(turtle) < 20:
#         food3.hideturtle()
#     elif food4.distance(turtle) < 20:
#         food4.hideturtle()
#     elif food5.distance(turtle) < 20:
#         food5.hideturtle()

# # Assume you have a turtle object called 'turtle'
# turtle = Turtle()
# turtle.shape("turtle")

# time.sleep(1)
# screen.listen()
# screen.onkey(bubble_blast, "Return")

# screen = Screen()
# time.sleep(1)
# screen.exitonclick()

# from tkinter import *
# from turtle import Turtle, Screen
# import time

# def bubble_blast():
#     global food1, food2, food3, food4, food5
#     # Check if any of the food items are visible, and hide the first visible one
#     for food in [food1, food2, food3, food4, food5]:
#         if food.isvisible():
#             food.hideturtle()
#             break

# window = Tk()
# window.title("Bubble...")
# window.config(padx=50, pady=50)

# screen = Screen()
# screen.tracer()

# canvas = Canvas(width=500, height=500)

# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=2, stretch_wid=2)
#         self.color("red")
#         self.speed("fastest")

# food1 = Food()
# food2 = Food()
# food3 = Food()
# food4 = Food()
# food5 = Food()

# food1.goto(-220, 0)
# food2.goto(-120, 0)
# food3.goto(120, 0)
# food4.goto(220, 0)
# food5.goto(0, 0)

# button = Button(text="Click Me", command=bubble_blast)
# button.pack()

# # Assume you have a turtle object called 'turtle'
# turtle = Turtle()
# turtle.shape("turtle")

# time.sleep(1)
# screen.listen()

# # Use the button's command to trigger the bubble_blast function
# # screen.onkey(bubble_blast, "Return")

# window.mainloop()


# from tkinter import *
# from turtle import RawTurtle, ScrolledCanvas
# import time

# window = Tk()
# window.title("Bubble...")
# window.config(padx=50, pady=50)

# # Create a Tkinter Canvas
# canvas = Canvas(window, width=500, height=500, bg="white")
# canvas.pack()

# class Food(RawTurtle):
#     def __init__(self, canvas):
#         super().__init__(canvas)
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=2, stretch_wid=2)
#         self.color("red")
#         self.speed("fastest")

# def create_bubble():
#     food1 = Food(canvas)
#     food2 = Food(canvas)
#     food3 = Food(canvas)
#     food4 = Food(canvas)
#     food5 = Food(canvas)

#     food1.goto(-220, 0)
#     food2.goto(-120, 0)
#     food3.goto(120, 0)
#     food4.goto(220, 0)
#     food5.goto(0, 0)

# button = Button(text="Click Me", command=create_bubble)
# button.pack()

# # Optional: Uncomment the lines below if you want to exit the Tkinter window after a certain time
# # time.sleep(10)
# # window.quit()
# # window.destroy()
# window.mainloop()

# from tkinter import *
# from turtle import RawTurtle, ScrolledCanvas

# window = Tk()
# window.title("Bubble...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=500, height=500, bg="white")
# canvas.grid()

# class Bubble(RawTurtle):
#     def __init__(self, canvas):
#         super().__init__(canvas)
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=2, stretch_wid=2)
#         self.color("red")
#         self.speed("fastest")

# def create_bubble():
#     food1 = Bubble(canvas)
#     food2 = Bubble(canvas)
#     food3 = Bubble(canvas)
#     food4 = Bubble(canvas)
#     food5 = Bubble(canvas)

#     food1.goto(-220, 0)
#     food2.goto(-120, 0)
#     food3.goto(120, 0)
#     food4.goto(220, 0)
#     food5.goto(0, 0)

# button_create = Button(text="Create Bubble", command=create_bubble)
# button_create.grid(column=0, row=0)

# def bubble_blast():
#     # Your bubble_blast function code here
#     pass

# button_blast = Button(text="Bubble Blast", command=bubble_blast)
# button_blast.grid(column=1, row=0)

# window.mainloop()

from tkinter import *
from turtle import RawTurtle

window = Tk()
window.title("Bubble...")
window.config(padx=50, pady=50)

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

# Declare the list of bubbles globally
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

    # Append the bubbles to the global list
    bubble_list = [food1, food2, food3, food4, food5]

button_create = Button(text="Create Bubble", command=create_bubble)
button_create.grid(column=3, row=1)

def bubble_blast():
    global bubble_list
    # Check if any of the bubbles are visible, and hide the first visible one
    for food in bubble_list:
        if food.isvisible():
            food.hideturtle()
            break

button_blast = Button(text="Activate Me", command=bubble_blast)
button_blast.grid(column=1, row=1)

window.mainloop()
