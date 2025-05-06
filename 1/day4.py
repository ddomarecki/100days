import random
#
# random_integer = random.randint(1, 10)
#
# print(random_integer)
#
# random_number = random.random() * 10
#
# random_float = random.uniform(1, 10)

# friends = ["Alice", "Bob", "David"]
#
# print(random.choice(friends))
#
# list_items = len(friends) - 1
#
# random_integer = random.randint(0, list_items)
#
# print(friends[random_integer])
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])

elements = ["rock", "paper", "scissors"]
computerChoice = random.randint(0, len(elements) - 1)

humanChoice = int(input("Chose between rock 0, paper - 1, and scissors - 2\n"));

if humanChoice == computerChoice:
    print("Draw")
elif (humanChoice == 0 and computerChoice == 2) or \
     (humanChoice == 1 and computerChoice == 0) or \
     (humanChoice == 2 and computerChoice == 1):
    print("You win!")
else:
    print("You lose!")