from tkinter import *

window = Tk()

w1 = Label(window, text="박스 #1", bg="red", fg="white")
w1.place(x=0, y=0)
w2 = Label(window, text="박스 #2", bg="green", fg="black")
w2.place(x=50, y=150)
w3 = Label(window, text="박스 #3", bg="blue", fg="white")
w3.place(x=20, y=100)

window.mainloop()
