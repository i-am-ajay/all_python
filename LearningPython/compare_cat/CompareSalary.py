__author__ = 'gaa8664'

from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import *


def frame():
    frame = Tk()
    frame.geometry("500x500")
    my_text = StringVar()
    field = Entry(width=40)
    field.grid(row=1, column=1,sticky='e', padx=5, pady=5, columnspan=2)
    button = Button(text="upload", width=15)
    button.grid(row=1, column=3, pady=5)
    dialog = askopenfilename(initialdir='d://')
    my_text.set(dialog)
    print(my_text.get())
    frame.mainloop()


if __name__ == '__main__':
    frame()
