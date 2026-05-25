# Step 2.

import random
word_list = ["raspberry", "watermelon", "mango", "blackberry", "plum", "grapefruit"]
choosen_word = random.choice(word_list)

# Testing Code.
print(f"The Solution is {choosen_word}")

# Empty Display List.
# Add a "_" in dsiplay.
display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
 guess = input("Guess a Letter!\n").lower()

# Loop through each position in the choosen_word.
# Check Guess Letter.
for position in range(word_length):
    letter = choosen_word[position]
    print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {guess}")
    if letter == guess:
        display[position] = letter
print(display)

if "_" not in display:
   end_of_game = True
   print("You Win.")


