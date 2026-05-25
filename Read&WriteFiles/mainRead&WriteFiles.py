file = open("Read&WriteFiles\my_file.txt")
# # file = open("my_file.txt")
contents = file.read()
print(contents)

       # ANOTHER METHOD OF READ FILES.

# with open("Read&WriteFiles\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

       # "w" FOR WRITE IN FILES. 

with open("Read&WriteFiles\my_file.txt", mode = "w") as file:
    file.write("New Text.")

       # "a" FOR APPEND IN FILES.

# with open("Read&WriteFiles\my_file.txt", mode = "a") as file:
#     file.write("\nNew text.")

# with open("..\..\24.Read&WriteFiles\my_file.txt") as file:
#     contents = file.read()
#     print(contents)