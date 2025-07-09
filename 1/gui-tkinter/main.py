from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    new_text = input.get()
    print("I got clicked")
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=20)
input.pack()
input.get()




def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 2, 1))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)



window.mainloop()