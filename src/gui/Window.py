import tkinter

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

top=tkinter.Tk()

C = tkinter.Canvas(top, bg="gray", height=600, width=800)


circle = create_circle(100,100,25, C)

for i in range(3):
    create_circle(100*(i+1), 100,25, C)

line = C.create_line(100,100, 200, 100)

C.pack()
top.mainloop()


