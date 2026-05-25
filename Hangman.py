# Step 1.
word_list = ["raspberry", "watermelon", "mango", "blackberry", "plum", "grapefruit"]

# Randomly choose a word.
import random
choosen_word = random.choice(word_list)

# Guess a letter.
guess = input("Guess a Letter!\n").lower()

# Check if the letter user guess is one of the letters in the choosen_word.
for letters in choosen_word:
    if letters == guess:
        print("Right")
    else:
        print("Wrong")

