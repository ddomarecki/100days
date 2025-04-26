print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input ("What te percentage tip woluld like to give 10, 12, 15?"))
people = int(input("Howa many peo9ple to split the bill?"))

bill_with_tip = tip/ 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay {final_amount}")