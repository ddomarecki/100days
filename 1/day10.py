# def format_name(f_name, l_name):
#     """Function
#        explanation"""
#     if f_name == "" or l_name == "":
#         return
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     # print(f"{formated_f_name} {formated_l_name}")
#
#     return f"{formated_f_name} {formated_l_name}"
#
# # print(format_name("damian", "DomareckI"))
# formated_string =  format_name("damian", "DomareckI")
# print(formated_string)
#
# # def is_leap_year(year):
# #     if year % 4 != 0:
# #         return False
# #     elif year % 100 != 0:
# #         return True
# #     elif year % 400 == 0:
# #         return True
# #     else:
# #         return False

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

operations["*"](4, 8)
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type y to continue calculation with {answer}, or type n to start new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()