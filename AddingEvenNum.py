# Add Odd Numbers.
total = 0
for number in range(1, 101, 2):
    print(number)

# Add Even Numbers.
total = 0
for number in range(2, 101, 2):
    print(number)

# Total Even Numbers.
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Another Method of Adding Even Numbers.
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)
