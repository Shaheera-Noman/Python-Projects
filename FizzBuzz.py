# for number in range(1,101):
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)

game = int(input("Select your number\n"))
if game % 3 == 0:
    print("Fizz")
elif game % 5 == 0:
    print("Buzz")
elif game % 3 == 0 and game % 5:
    print("FizzBuz")
else:
    print("Game Over")


