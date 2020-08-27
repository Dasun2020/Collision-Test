from tkinter import *
import time
x_ = 0
y_ = 0
#=========================================== def MOUSE class ===========================================
class MOUSE:
    def __init__(self, canvas):
        self.id = canvas.create_oval(10, 10, 25, 25, fill="red")
        self.canvas = canvas
        global color
        color = "red"

        
    def draw(self):
        def motion(event):
            global x_
            global y_
            x_, y_ = event.x, event.y
            radius = 20
            x = x_ + radius
            x2 = x_ - radius
            y = y_ + radius
            y2 = y_ - radius
            self.canvas.delete(self.id)
            self.id = canvas.create_oval(x, y, x2, y2, fill=color)
        self.canvas.bind_all('<Motion>', motion)

#=========================================== def CENTER class ===========================================
class CENTER:
    def __init__(self, canvas):
        self.id = canvas.create_oval(10, 10, 25, 25, fill="red")
        self.canvas = canvas
        self.canvas.move(self.id, 232.44, 233)
        
#=========================================== def LINE class ===========================================
        
class LINE:
    def __init__(self, canvas, x1, y1):
        self.id = canvas.create_line(x_, y_, x1, y1)
        self.length = 0
        self.canvas = canvas
        
        
    def draw(self):
        self.canvas.delete(self.id)
        self.id = canvas.create_line(x_, y_, 250, 250)
        global dist
        global dist2
        dist = x_ - 250
        dist2 = y_ - 250
        if self.HIT() == True:
            print("Collision!")
        else:
            print("Not Collision. . . ")
            
        
    def HIT(self):
        self.length = round(((dist ** 2 + dist2 ** 2) ** (1 / 2)))
        if self.length <= 28:
            return True
        else:
            return False
            
#=========================================== def canvas and tk ===========================================

tk = Tk()
tk.title("Collision test")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
mouse = MOUSE(canvas)
center = CENTER(canvas)
line = LINE(canvas, 140, 120)

#=========================================== while loop ===========================================

while True:
    line.draw()
    mouse.draw()
    tk.update()
    tk.update_idletasks()
