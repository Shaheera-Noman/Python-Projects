# FOR LOOP.

numbers = [1, 2 ,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

     # LIST COMPREHENSION.

# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
# print(new_list)

    # STRING AS LIST.

name = "Shaheera"
letter_list = [letter for letter in name]
# print(letter_list)

    # RANGE AS LIST.
range_list = [num * 2 for num in range(1,5)]
# print(range_list)

    # CONDITIONAL LIST COMPREHENSION

# new_list = [new_item for item in list if test]
names = ["Shaheera", "Ali", "Fatima", "Hasan"]
# print(names)
# names = ['Shaheera', 'Ali', 'Fatima', 'Hasan']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)
