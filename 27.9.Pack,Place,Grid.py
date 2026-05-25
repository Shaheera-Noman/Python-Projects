from tkinter import *

def button_clicked():
    print("I got Clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=100,pady=200)

my_label = Label(text="Shaheera Noman here", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)
# my_label.pack(side="left")
# my_label.place(x=100, y=200)

# my_label = Label(text="New Button",font=("Arial", 24, "bold"))
# my_label.grid(column=3, row=2)

button = Button(text="Activate Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack(side="left")

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)
# input.pack(side="left")

window.mainloop()