pizza_size = input("Whcich pizza size do you want? s, m, l \n")

add_peproni = input("Do you want to add peproni 'y' or 'n'?\n")
extra_cheese = input("Do you want to extra cheese 'y' or 'n'?\n")

bill = 0

if pizza_size == "s":
    if add_peproni == "y":
        bill = 12
    else:
        bill = 15
if extra_cheese == "y":
    bill +=2

if pizza_size == "m":
    if add_peproni == "y":
        bill = 15
    else:
        bill = 18

if extra_cheese == "y":
    bill +=3

if pizza_size == "l":
    if add_peproni == "y":
        bill = 18
    else:
        bill = 20

if extra_cheese == "y":
    bill +=4

print(f"Your final bill is {bill}")
