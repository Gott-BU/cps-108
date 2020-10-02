from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=800, height=500)
c.pack()
a=100
b=100
w=300
n=0

# Put drawing here!

#Field Background
c.create_rectangle(0,0,800,500,fill="#5cac2d")     #green
c.create_rectangle(a+550,b,a+600,b+300,fill="#fac205")     #goldenrod
c.create_rectangle(a,b,a+50,b+300,fill="#7e1e9c")     #purple

c.create_rectangle(a,b,a+600,b+300,width=5,outline="#ffffff")

#Yardlines
for x in range(175,626,25):
    c.create_line(x,b,x,b+w,width=2,fill='#ffffff')

for x in range(155, 650, 5):
    c.create_line(x,b+75,x,b+100,fill='#ffffff')
    c.create_line(x,b+200,x,b+225,fill='#ffffff')

#yard line markers
for x in range(200,401,50):
    n=n+10
    c.create_text(x+10,125, text=str(n))
for x in range(450,601,50):
    n=n-10
    c.create_text(x+10,125, text=str(n))


# for y in range(50, 500, 50):
#     c.create_line(0, y, 800, y)
#     c.create_text(18, y + 10, text=str(y))

# for x in range(50, 800, 50):
#     c.create_line(x, 0, x, 500)
#     c.create_text(x + 18, 10, text=str(x))

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
