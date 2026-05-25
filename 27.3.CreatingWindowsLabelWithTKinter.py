import tkinter
window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Shaheera Noman here", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack(expand=True)

import turtle

tim = turtle.Turtle()
tim.write("Think Deep", font=("Times New Roman", 80, "bold"))

# window.mainloop()