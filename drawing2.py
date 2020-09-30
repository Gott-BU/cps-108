from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=800, height=500)
c.pack()

# Put drawing here!


for y in range(50, 500, 50):
    c.create_line(0, y, 500, y)
    c.create_text(18, y + 10, text=str(y))

for x in range(50, 500, 50):
    c.create_line(x, 0, x, 500)
    c.create_text(x + 18, 10, text=str(x))

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
