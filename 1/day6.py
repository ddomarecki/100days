#Hurdle 3 from Reeborg's World

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    else:
        move()