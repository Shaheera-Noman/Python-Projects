def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
move()
move()
turn_around()
move()
move()
turn_around()

# Draw Square in Square.
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# Using For Loop HURDLE 1.
def turn_around():
    turn_left()
    turn_left()
   
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for step in range(6):
    jump()

# Using While Loop.
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# HURDLE 2.

while not at_goal():
    jump()

# HURDLE 3.
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# HURDLE 4.
def turn_around():
    turn_left()
    turn_left()
   
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Maze.
def turn_around():
    turn_left()
    turn_left()
   
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


