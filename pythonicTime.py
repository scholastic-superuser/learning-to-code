# copied from https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/#
from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to display time on the label

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


# Styling the label widget so that clock will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
			background='purple',
			foreground='white')

# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()




'''
My goals for this program are the following:

    Set up a clock that refreshes to give me the time in realtime
    Print out the current Unix time
    import Tkinter for a graphical digital clock
    Print out the current moon phase for my area
    Print out the sunrise, sunset, moonrise, and moonset times
'''
