# student_scores = [140, 134, 194, 501, 143, 21, 41, 491, 41]
# #
# # max = 0
# #
# # for score in student_scores:
# #     if score > max:
# #         max = score
# # print (max)

# sum = 0
# for number in range(1, 101):
#     sum += number
#
# print(sum)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
sum_letters = len(letters)
sum_numbers = len(symbols)
sum_symbols = len(numbers)

password = ""
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for number in range(0, (nr_letters - nr_symbols - nr_numbers )):
    password += letters[random.randint(0, sum_letters)]
for number in range(0, nr_numbers):
    password += numbers[random.randint(0, sum_numbers)]
for number in range(0, nr_symbols):
    password += symbols[random.randint(0, sum_symbols)]

password2 = list(password)
random.shuffle(password2)
password2 = ''.join(password2)
print (password2)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P