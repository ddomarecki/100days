try:
    age = int(input("how old are you?"))
except ValueError:
    print("Type valid number")
    age = int(input("how old are you?"))

if age > 18:
    print(f"You can drive at age {age}")