import random

#Random numbers.

random_side = random.randint(0,1)
if random_side == 1:
    print("heads")
else:
    print("Tails")

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

randomInteger = random.randint(1,20)
print(randomInteger)

randomFloat = random.random() * 5
print(randomFloat)

#Random Names.
#fav = ["Shaheera", "Ali", "Fatima", "Hssan"]
names = input("Give me the names\n")
random_names = names.split(",")
print(len(random_names))

#random_names = random.randint(0,fav-1)
print(random_names)