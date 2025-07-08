import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 2, 1))


window.mainloop()