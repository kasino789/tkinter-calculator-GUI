from tkinter import*

def button_press(num):
    global calculator_text
    calculator_text += str(num)
    calculator_text = calculator_text.lstrip('0')
    calculator_label.set(calculator_text)
    
def equal():
    global calculator_text
    
    try:
     total = str(eval(calculator_text))
     calculator_label.set(total)
     calculator_text = total
     
    except SyntaxError:
        calculator_label.set('Syntax Error')
        calculator_text = ""
        
    except ZeroDivisionError:
     calculator_label.set('Arithmetic Error')
     calculator_text = ""
     
     
def clear():
    global calculator_text
    
    calculator_label.set("")
    calculator_text = ""    
 
def bck():
    global calculator_text
    
    calculator_text = calculator_text[:-1]   
    calculator_label.set(calculator_text)

window = Tk() #instantiate an instance of a window
window.geometry("600x600")
window.title("Calculator")


# icon = PhotoImage(file="C:\\Users\\rishi\\OneDrive\\Desktop\\Python\\tkinter tut\\calculator.png")
# window.iconphoto(True,icon)

window.config(background='black')

calculator_text = "" 
calculator_label = StringVar()

label = Label(window, textvariable=calculator_label, font=('monospace',20),bg='black',fg='white',width=24,height=3)
label.pack()

frame = Frame(window)
frame.pack(side=BOTTOM)

#Buttons
button7 = Button(frame, text=7, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(7))
button7.grid(row=0,column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(8))
button8.grid(row=0,column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(9))
button9.grid(row=0,column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(6))
button6.grid(row=1,column=2)

button1 = Button(frame, text=1, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(1))
button1.grid(row=2,column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(2))
button2.grid(row=2,column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(3))
button3.grid(row=2,column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='orange', command= lambda: button_press(0))
button0.grid(row=3,column=1)


dot = Button(frame, text='.', height=4, width=9, font=35, fg='white', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda: button_press('.'))
dot.grid(row=3,column=0)

div = Button(frame, text='/', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda: button_press('/'))
div.grid(row=0,column=3)

mul = Button(frame, text='*', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda: button_press('*'))
mul.grid(row=1,column=3)

sub = Button(frame, text='-', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda: button_press('-'))
sub.grid(row=2,column=3)

add = Button(frame, text='+', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda: button_press('+'))
add.grid(row=3,column=3)

clear = Button(frame, text='AC', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= clear)
clear.grid(row=0,column=4)

bck = Button(frame, text='Back', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= bck)
bck.grid(row=1,column=4)

equal= Button(frame, text='=', height=4, width=9, font=35, fg='white', bg='orange', border=0,activebackground='black', activeforeground='white', command= equal)
equal.grid(row=3,column=2)

left_bracket = Button(frame, text='(', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda:button_press('('))
left_bracket.grid(row=2,column=4)

right_bracket = Button(frame, text=')', height=4, width=9, font=35, fg='orange', bg='black', border=0,activebackground='black', activeforeground='white', command= lambda:button_press(')'))
right_bracket.grid(row=3,column=4)


window.mainloop()