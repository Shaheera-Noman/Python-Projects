import random

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images = [rock, paper, scissor]
user_chioce = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissor.\n"))
if user_chioce >= 3 or user_chioce < 0:
    print("You typed an invalid number, You Lose.")
else:
    print(game_images[user_chioce])

    computer_choice = random.randint(0,2)
    # print("Computer chose:")
    print(f"Computer chose: {computer_choice}")
    print(game_images[computer_choice])

# if user_chioce >= 3 or user_chioce < 0:
#     print("You typed an invalid number, You Lose.")
    if user_chioce == 0 and computer_choice == 2:
     print("You Win.")
    elif computer_choice == 0 and user_chioce == 2:
     print("You Lose.")
    elif user_chioce > computer_choice:
     print("You Win.")
    elif computer_choice > user_chioce:
     print("You Lose.")
    elif user_chioce == computer_choice:
     print("It's a draw.")
