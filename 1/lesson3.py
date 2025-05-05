size = input("What size pizza do ytou want? S, M or L?")
pepperoni = input("Pepperoni Y or N")
extra_cheese = input("double chesse? Y or N")

bill = 0
if size == "S":
    bill+=15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"${bill}")