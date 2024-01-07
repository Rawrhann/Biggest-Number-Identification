
#Ask user to input 3 numbers. Find and print the biggest num,ber using only if statement
#create a new github repository
#Upload your progress to github using git bash
#Record a demo presenting your program [less than 2 min only]
#Send the demo directly to sir Danilo's messenger
#Deadline before Jan 13, 2023

#Pseudo code
from tkinter import *
from tkinter import simpledialog
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import tkinter.font
from tkinter import font
from tkinter.simpledialog import Dialog

#Identification of larger numbers
#Between the first and second number, check which is higher
#Between the first and third number, check which is higher
#Between the second and third number, check which is higher
def identify(highest_number):
    if first_number_variable > second_number_variable and first_number_variable > third_number_variable:
        return highest_number
    elif second_number_variable > third_number_variable:
        return highest_number
    else:
        return highest_number
#Asking for numbers and checking if it is a number

main_window = tk.Tk() 
main_window.title ("Startup")
main_window.config(bg = "#212121")
font.families()

# for storing numbers
first_number_variable=tk.IntVar
second_number_variable=tk.IntVar
third_number_variable=tk.IntVar

button_start = Button(main_window, width = "15", height = "2", text = "Identify", command = identify, bg="green", fg="white")
button_exit = Button(main_window, width = "15", height = "2", text = "Exit", command = exit, bg="red", fg="white")

#Input First number
first_number_entry = tk.Entry(main_window, textvariable = first_number_variable, font=('calibre',10,'normal'))
first_number_label = tk.Label(main_window, text = 'First Number', font=('calibre',10, 'bold'), bg="#454545", fg="white", relief="solid")
#Check if the first number is a number


#Input second number
second_number_entry = tk.Entry(main_window, textvariable = second_number_variable, font=('calibre',10,'normal'))
second_number_label = tk.Label(main_window, text = 'Second Number', font=('calibre',10, 'bold'), bg="#454545", fg="white", relief="solid")
#Check if the second number is a number

#Input third number
third_number_entry = tk.Entry(main_window, textvariable = third_number_variable, font=('calibre',10,'normal'))
third_number_label = tk.Label(main_window, text = 'Third Number', font=('calibre',10, 'bold'), bg="#454545", fg="white", relief="solid")
#Check if the third number is a number




#The number that will get a higher result twice would be the highest between them all
#Display that number

#Placements in the main window
button_start.place(x=0, y=0)
button_exit.place(x=0, y=560)
first_number_label.place(height=15, width=150, x=100, y=50)
second_number_label.place(height=15, width=150, x=100, y=150)
third_number_label.place(height=15, width=150, x=100, y=250)

first_number_entry.place(height=15, width=150, x=100, y=100)
second_number_entry.place(height=15, width=150, x=100, y=200)
third_number_entry.place(height=15, width=150, x=100, y=300)

#Main window size
main_window.geometry("400x600")
main_window.resizable(False, False)

main_window.mainloop()