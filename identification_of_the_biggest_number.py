
#Ask user to input 3 numbers. Find and print the biggest num,ber using only if statement
#create a new github repository
#Upload your progress to github using git bash
#Record a demo presenting your program [less than 2 min only]
#Send the demo directly to sir Danilo's messenger
#Deadline before Jan 13, 2023

#Pseudo code
from tkinter import *
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import tkinter.font
from tkinter import font



#Asking for numbers and checking if it is a number

#Identification of larger numbers
def identify():
    if any (entry == "" for entry in (first_number_entry.get(), second_number_entry.get(), third_number_entry.get())):
        messagebox.showerror("Input", "Don't leave blank entries")
        return
    
    try:
        first_number = float(first_number_entry.get())
        second_number = float(second_number_entry.get())
        third_number = float(third_number_entry.get())
        

    except ValueError:
        messagebox.showerror("Input", "Only input numbers")
        return

    def largest(first_number, second_number, third_number):
        if first_number > second_number and first_number > third_number:
            return first_number
        elif second_number > third_number:
            return second_number
        else:
            return third_number
        
    largest_number = largest(first_number, second_number, third_number)
    largest_number_display.configure(text=(largest_number))
    largest_number_display_words = tk.Label(main_window, text="The largest number\n among the 3 inputs are", font=display_font, bg="#454545", fg="white", relief="solid", justify="center")
    largest_number_display_words.place(height=60, width=200, x=75, y=300)
    largest_number_display.place(height=30, width=150, x=100, y=360)

#Main User Interface
main_window = tk.Tk() 
main_window.title ("Startup")
main_window.config(bg = "#212121")

#Fonts
font.families()
courier_font = ("courier", 13, 'bold')
display_font = ("Eccentric", 10)

button_start = Button(main_window, width = "15", height = "2", text = "Identify", command = identify, bg="green", fg="white")
button_exit = Button(main_window, width = "15", height = "2", text = "Exit", command = exit, bg="red", fg="white")

#Input First number
first_number_entry = tk.Entry(main_window, font=('calibre',10,'normal'), justify="center")
first_number_label = tk.Label(main_window, text = 'First Number', font=courier_font, bg="#454545", fg="white", relief="solid", justify="center")
#Check if the first number is a number


#Input second number
second_number_entry = tk.Entry(main_window, font=('calibre',10,'normal'), justify="center")
second_number_label = tk.Label(main_window, text = 'Second Number', font=courier_font, bg="#454545", fg="white", relief="solid", justify="center")
#Check if the second number is a number

#Input third number
third_number_entry = tk.Entry(main_window, font=('calibre',10,'normal'), justify="center")
third_number_label = tk.Label(main_window, text = 'Third Number', font=courier_font, bg="#454545", fg="white", relief="solid", justify="center")
#Check if the third number is a number

#The number that will get a higher result twice would be the highest between them all
#Display that number
largest_number_display = tk.Label(main_window)

#Placements in the main window
button_start.place(x=0, y=0)
button_exit.place(x=0, y=460)
first_number_label.place(height=30, width=150, x=100, y=50)
second_number_label.place(height=30, width=150, x=100, y=125)
third_number_label.place(height=30, width=150, x=100, y=200)

first_number_entry.place(height=30, width=150, x=100, y=75)
second_number_entry.place(height=30, width=150, x=100, y=150)
third_number_entry.place(height=30, width=150, x=100, y=225)

#Main window size
main_window.geometry("400x500")
main_window.resizable(False, False)

main_window.mainloop()