# Simple way of calculationg the Average Height.
student_heights = input("Input the list of students heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heights = sum(student_heights)
num_of_students = len(student_heights)
average_students = round(total_heights/num_of_students)
print(average_students)

# Another way of calculating the Average Height.
total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

# num_of_students = len(student_heights)
# average_height = total_heights/num_of_students
# print(average_height)

# Another way of len function.
num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)

average_height = round(total_heights/num_of_students)
print(average_height)
