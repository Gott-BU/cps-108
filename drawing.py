from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=800, height=500)
c.pack()

# Put drawing here!
#background
c.create_rectangle(0, 0, 800, 350, outline='#75bbfd', fill='#75bbfd')
c.create_rectangle(0, 350, 800, 500, outline='#4da409', fill='#4da409')

#House
c.create_rectangle(50, 200, 450, 450, outline='#f1da7a', fill='#f1da7a')
c.create_rectangle(300, 210, 450, 460, outline='#fef69e', fill='#fef69e')

#roof
c.create_polygon(75, 100, 425, 100, 475, 200, 25, 200, fill='#4e5481')
c.create_polygon(375, 125, 275, 210, 475, 210, fill='#85a3b2')
c.create_polygon(375, 100, 275, 200, 275, 210, 375, 125, fill='#758da3')
c.create_polygon(375, 100, 375, 125, 475, 210, 475, 200, fill='#b7c9e2')

#windows
c.create_oval(358, 150, 392, 184, fill='#d6fffe')
c.create_rectangle(75, 250, 175, 350, fill='#d6fffe')
c.create_rectangle(325, 255, 425, 355, fill='#d6fffe')
c.create_rectangle(325, 255, 425, 355, fill='#d6fffe')


#cloud
#c.create_oval(150, 250, 300, 400, fill='blue')

# for y in range(50, 500, 50):
#     c.create_line(0, y, 500, y)
#     c.create_text(18, y + 10, text=str(y))

# for x in range(50, 500, 50):
#     c.create_line(x, 0, x, 500)
#     c.create_text(x + 18, 10, text=str(x))

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
