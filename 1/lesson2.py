# lesson 3

print("welcome")
number = int(input("What is ur height in cm?"))

if number % 2 ==0:
    print("even")
    age = int(input("What is you age"))
    if age == 18:
        print("Znizka dla 18 latka")
    elif (age <= 18):
        print("znizka")
    elif age >= 45 and age <= 55:
        print("Free ride")
    else:
        print("bez zniżki")
 
else:
    print("odd")

