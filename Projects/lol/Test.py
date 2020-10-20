from tkinter import *
root = Tk()
c = Canvas(root, width = 400, height = 400)
c.pack()
for i in range(0, 5):
    for j in range(0, 10):
        c.create_rectangle(i * 80, j*80, i * 80 + 80, j*80 + 80, fill = "white", outline = "black", tag = "change")
root.mainloop()