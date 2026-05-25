from tkinter import *
window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="Shaheera Noman here", font=("Arial", 24, "bold"))
my_label.pack(side="top")
# my_label.pack(expand=True)

my_label["text"] = "New text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked!")
    my_label.config(text="Button Got Clicked!")

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()