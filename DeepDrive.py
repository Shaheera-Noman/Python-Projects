programming_dictionaries = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you ca easily call over and over again.", 
    "Loop": "The action of doing something over and over gain."}

#print(programming_dictionaries["Bug"])

# Add new item in dictionary.

programming_dictionaries["List"] = "A List is a collection of items."
print(programming_dictionaries)

# Add an empty dictionary.
empty_dictionary = {}
print(empty_dictionary)

#Loop through a dictionary.
for keys in programming_dictionaries:
    print(keys)
    print(programming_dictionaries[keys])


