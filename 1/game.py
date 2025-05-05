choice1 = input("You are at a srossroad, where do yoy want to go? Type \"left\" or \"right\"").lower()
if choice1 == "left":
    print("continue game")
    choice2 = input("you have come to the lake type wait or swim").lower()
    if choice2 == "wait":
        choice3 = input("choice 3 doors yellow red or blue").lower()
        if choice3 == "red":
            print("game over")
        elif choice3 == "yellow":
            print("u win!")
        elif choice3 == "blue":
            print("game over")
    else:
        print("game over")
else:
    print("Game Over")
