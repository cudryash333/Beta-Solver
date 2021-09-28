from tkinter import *
from tkinter import messagebox


def show_message():
    messagebox.showinfo("Solution", new_message)


root = Tk()
root.title("Beta Solver")
root.geometry("600x400+300+300")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

new_message = open('output.txt', 'r')

message_button = Button(text="Enter", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()
