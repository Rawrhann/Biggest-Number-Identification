
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

#Asking for numbers and checking if it is a number

main_window = tk.Tk() 
main_window.title ("Startup")
main_window.config(bg = "black")
font.families()

# for storing numbers
first_number_variable=tk.IntVar
second_number_variable=tk.IntVar
third_number_variable=tk.IntVar

#button_start = Button(main_window, width = "15", height = "2", text = "Start", command = calculate, bg="green", fg="white")
button_exit = Button(main_window, width = "15", height = "2", text = "Stop", command = exit, bg="red", fg="white")

#Input First number
first_number_entry = tk.Entry(main_window, textvariable = first_number_variable, font=('calibre',10,'normal'))
first_number_label = tk.Label(main_window, text = 'First Number', font=('calibre',10, 'bold'))
#Check if the first number is a number


#Input second number
second_number_entry = tk.Entry(main_window, textvariable = second_number_variable, font=('calibre',10,'normal'))
second_number_label = tk.Label(main_window, text = 'Second Number', font=('calibre',10, 'bold'))
#Check if the second number is a number

#Input third number
third_number_entry = tk.Entry(main_window, textvariable = third_number_variable, font=('calibre',10,'normal'))
third_number_label = tk.Label(main_window, text = 'Third Number', font=('calibre',10, 'bold'))
#Check if the third number is a number


#Identification of larger numbers
#Between the first and second number, check which is higher
#Between the first and third number, check which is higher
#Between the second and third number, check which is higher

#The number that will get a higher result twice would be the highest between them all
#Display that number

#Placements in the main window
button_exit.grid(padx = 50, column = 4)
first_number_label.grid(row=0, column=0, )
second_number_label.grid(row=1, column=0)
third_number_label.grid(row=2, column=0)

first_number_entry.grid(row=0, column=1)
second_number_entry.grid(row=1, column=1)
third_number_entry.grid(row=2, column=1)

#Main window size
main_window.geometry("900x300")
main_window.resizable(False, False)

main_window.mainloop()