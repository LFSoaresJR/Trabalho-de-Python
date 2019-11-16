import tkinter as tk
import classGraph as graph

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.g = graph.Graph()
        self.line = False
        self.old_item = None
        self.canvas = tk.Canvas(self, width=1280, height = 720, bg = 'white')
        self.canvas.bind("<Button-1>",self.draw_circle)
        #self.canvas.bind("<Motion>",self.mouse_motion)
        self.canvas.pack()
        

    def draw_circle(self,event):
        x,y = event.x,event.y
        if(self.g.verify_v(x,y) is False):
            bbox = (x-20,y-20,x+20,y+20)
            self.canvas.create_oval(*bbox ,  width = 2)
            #label = Label(root , text = str(g.last),bg = 'white').place(x = x-5 , y = y-5)
            self.g.add_v(x,y)
            self.g.last = self.g.last+1
            self.line = False
            self.canvas.itemconfig(self.old_item ,outline = 'black')
            self.canvas.create_text(x,y, text = self.g.last)
        else:
            if(self.line):
                self.canvas.itemconfig(self.old_item ,outline = 'black')
                self.old_item = None
                self.line = False
                x_ori,y_ori= self.line_source
                points = self.g.connection(x_ori,y_ori,x,y)
                x1 = points[0]
                y1 = points[1]
                x2 = points[2]
                y2 = points[3]
                if(x1 is x2 and y1 is y2):
                    points = (x1-35, y1, x2, y2-35)
                    self.canvas.create_arc(*points, start=0, extent=270,style='arc')
                else:
                    if(x1 < x2):
                        points = (x1+20, y1, x2-20, y2)
                    else:
                        points = (x1-20, y1, x2+20, y2)
                    self.canvas.create_line(*points,fill='black')
            else:
                self.old_item = self.canvas.find_closest(x+20,y+20)
                self.canvas.itemconfig(self.old_item ,outline = 'red')
                self.line_source = (x,y)
                self.line = True
                

    # def mouse_motion(self,event):
    #     self.canvas.itemconfig(self.current, fill="black")
    #     self.current = self.canvas.find_closest(event.x,event.y)
    #     self.canvas.itemconfig(self.current, fill="yellow")


app = App()
app.mainloop()