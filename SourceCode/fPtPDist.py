import math
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *



def calculate():
    x1 = float(x1_text.get())
    x2 = float(x2_text.get())
    y1 = float(y1_text.get())
    y2 = float(y2_text.get())
    d = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    d_answer = Label(root, text = d)
    d_answer.place(x = 80, y = 160, width = 150 , height = 40)
    def graph(x1,x2,y1,y2):
        x_list= [x1,x2]
        y_list = [y1,y2]
        f = Figure()
        f.patch.set_facecolor('#53fca1')
        a = f.add_subplot(111)
        a.plot(x_list,y_list, label = 'The distance', marker = 'o', linewidth = 3)
        plt.ylabel('Y value')
        plt.xlabel('X value')
        a.legend()
        a.grid(True)
        canvas = FigureCanvasTkAgg(f, master = root)
        canvas.get_tk_widget().place(x = 255,y = 0, width = 445, height = 300)
        canvas.draw()
        pass
    graph(x1,x2,y1,y2)

    pass

root = Tk()
root.title('From Point to Point Distance')
img = PhotoImage(file = 'icon.png')
root.tk.call('wm','iconphoto', root._w, img)
root.geometry(("700x300"))
root.minsize(700,300)
root.maxsize(700,300)
canvas = Canvas(root,width = 700,height = 300, bg = '#53fca1')
canvas.create_line(250,0,250,300,width = 5, dash = (10,2), fill = '#170606')
canvas.pack()

x1_lab = Label(root,text = 'x1')
x1_lab.place(x = 5, y =5, width = 70)

x2_lab = Label(root,text = 'x2')
x2_lab.place(x = 5, y = 35, width = 70)

y1_lab = Label(root,text = 'y1')
y1_lab.place(x = 5, y = 65, width = 70)

y2_lab = Label(root,text = 'y2')
y2_lab.place(x = 5, y = 95, width = 70)

x1_text = Entry(root,width = 15)
x1_text.place(x = 80, y = 5)

x2_text = Entry(root,width = 15)
x2_text.place(x = 80, y = 35)

y1_text = Entry(root,width = 15)
y1_text.place(x = 80 , y = 65)

y2_text = Entry(root,width = 15)
y2_text.place(x = 80, y = 95)

d_lab = Label(root, text = 'd = ')
d_lab.place(x = 5, y = 160, width = 70, height = 40)


calc = Button(root,text = 'Calculate')
calc.config(command = calculate)
calc.place(x = 50, y = 250, width = 100)

root.mainloop()


@Unbewohnte
