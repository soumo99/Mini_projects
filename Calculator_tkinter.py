#Calculator appication using python tkinter

from tkinter import *
import parser  #helps in solving the mathematical calculations which is going to pop up onto the calculator
#accepts and compiles the entire expression

root = Tk()
root.title('Calculator')

#style.configure("TButton", background='red', font="Serif 15", padding=10 )

#Getting the input from the user and place it in the text field
i=0 #for the index , global i  variable keep tracks of the position where the value is to be inserted
def get_variables(num):
    global i
    display.insert(i,num)
    i += 1

#for the AC button on the calculator
def clear_all():
    display.delete(0,END)

#for the undo button on the calculator
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"ERROR!")


#for the arithmetic operations on the calculator
def arithmetic_operations(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length

#Calculation part
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR!")

#Adding the input field
display = Entry(root)
display.grid(row=1, columnspan = 6, sticky = W + E)

#Adding the numeric buttons to the calculator
Button(root, text = "1" ,command = lambda :get_variables(1)).grid(row=2, column=0)
Button(root, text = "2" , command = lambda :get_variables(2)).grid(row=2, column=1)
Button(root, text = "3", command = lambda :get_variables(3)).grid(row=2, column=2)

Button(root, text = "4" , command = lambda :get_variables(4)).grid(row=3, column=0)
Button(root, text = "5" , command = lambda :get_variables(5)).grid(row=3, column=1)
Button(root, text = "6" , command = lambda :get_variables(6)).grid(row=3, column=2)

Button(root, text = "7" , command = lambda :get_variables(7)).grid(row=4, column=0)
Button(root, text = "8" , command = lambda :get_variables(8)).grid(row=4, column=1)
Button(root, text = "9" , command = lambda :get_variables(9)).grid(row=4, column=2)

#Adding other buttons to the calculator
Button(root, text = "AC" , command = lambda :clear_all()).grid(row=5, column=0)
Button(root, text = "0" , command = lambda :get_variables(0)).grid(row=5, column=1)
Button(root, text = "=" , command = lambda :calculate()).grid(row=5, column=2)

#Adding the Arithmetic button to the calculator
Button(root, text = "+" , command = lambda :arithmetic_operations("+")).grid(row=2, column=3)
Button(root, text = "-" , command = lambda :arithmetic_operations("-")).grid(row=3, column=3)
Button(root, text = "*" , command = lambda :arithmetic_operations("*")).grid(row=4, column=3)
Button(root, text = "/" , command = lambda :arithmetic_operations("/")).grid(row=5, column=3)

Button(root, text = "pi" , command = lambda :arithmetic_operations("*3.14")).grid(row=2, column=4)
Button(root, text = "%" , command = lambda :arithmetic_operations("%")).grid(row=3, column=4)
Button(root, text = "(" , command = lambda :arithmetic_operations("(")).grid(row=4, column=4)
Button(root, text = "exp" , command = lambda :arithmetic_operations("**")).grid(row=5, column=4)

Button(root, text = "<-" , command = lambda :undo()).grid(row=2, column=5)
Button(root, text = "x!" , command = lambda :arithmetic_operations()).grid(row=3, column=5)
Button(root, text = "^" , command = lambda :arithmetic_operations("**2")).grid(row=4, column=5)
Button(root, text = ")" , command = lambda :arithmetic_operations(")")).grid(row=5, column=5)
Button(root, text = "." , command = lambda :arithmetic_operations(".")).grid(row=5, column=5)

root.mainloop()
