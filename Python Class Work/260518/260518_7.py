# 7번까지 해서 만드는데
# 엔트리박스는 7~9번박스에 한개 나머지 두칸에 결과값을 한개

# 노란바탕에 글씨 검정

from tkinter import *

window = Tk()
window.title("My Caculator")
display1 = Entry(window, width=33, bg="yellow")
display1.grid(row=0, column=0, columnspan=5)
display2 = Entry(window, width=13, bg="blue", fg="white")
display2.grid(row=0, column=3, columnspan=5)

button_list = [
    "7",
    "8",
    "9",
    "/",
    "C",
    "4",
    "5",
    "6",
    "*",
    "",
    "1",
    "2",
    "3",
    "-",
    "",
    "0",
    ".",
    "=",
    "+",
    "",
]

row_index = 1
col_index = 0

for button_text in button_list:

    def process(t=button_text):
        click(t)

    Button(window, text=button_text, width=5, command=process).grid(
        row=row_index, column=col_index
    )
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0


def process2():
    display1.delete(0, END)
    display2.delete(0, END)


def click(key):
    if key == "=":
        result = eval(display1.get())
        s = str(result)
        display2.insert(END, s)
    elif key == "C":
        process2()
    else:
        display1.insert(END, key)


window.mainloop()
