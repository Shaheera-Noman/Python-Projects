from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result.config(text=f"{km}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(width=600, height=500)
window.config(padx=50,pady=50)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer = Label(text="km")
kilometer.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()