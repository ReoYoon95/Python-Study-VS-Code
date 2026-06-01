from PIL import Image, ImageTk, ImageFilter

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open(
    "D:\\VS Code File\\python Study\\Python Class Work\\260601\\noddle.jpg"
)


# tk_img = ImageTk.PhotoImage(img)

out = img.filter(ImageFilter.BLUR)
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()
