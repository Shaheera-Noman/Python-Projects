# Step 4.

import random

stages = ['''
 +___+
 |   |
 O   |
/|\  |
/ \  |
     |
=======
''' , '''
+____+
 |   |
 O   |
/|\  |
/    |
     |
=======
''' , '''
+____+
 |   |
 O   |
/|\  |
/    |
     |
=======
''' , '''
+____+
 |   |
 O   |
/|\  |
     |
     |
=======
''' , '''
+____+
 |   |
 O   |
     |
     |
     |
=======
''' , '''
+____+
 |   |
     |
     |
     |
     |
=======
''']

end_of_game = False
word_list = ["raspberry", "watermelon", "mango", "blackberry", "plum", "grapefruit"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

# Create a variable called lives.
lives = 6

# Testing Code.
print(f"The Solution is {choosen_word}")

# Create Blanks.
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

# Check Guess Letter.
for position in range(word_length):
    letter = choosen_word[position]
    #print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {guess}")
    if letter == guess:
        display[position] = letter
    else:
        print("No Match.")

# Reduce lives by 1.

if lives not in choosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You Lose.")

# Join all the elements in the list and turn it into a string.
print(f"{' '.join(display)}")

# Check if user has got all letters.
if "_" not in display:
    end_of_game = True
    print("You Win.")

