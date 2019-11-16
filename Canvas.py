import tkinter as tk
import classGraph as graph


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.g = graph.Graph() #Create a type Graph
        self.line = False #Variable to know if the user is drawing a line
        self.old_item = None #Get the item was selected
        self.menubar = tk.Menu(self)

        #Create the file menu bar
        self.fileBar = tk.Menu(self.menubar, tearoff=0)
        self.fileBar.add_command(label="New")
        self.fileBar.add_command(label="Open")
        self.fileBar.add_command(label="Save")
        self.fileBar.add_command(label="Save as...")
        self.fileBar.add_command(label="Close")
        self.menubar.add_cascade(label="File", menu=self.fileBar)

        #Create the algorithms menu bar
        self.algoBar =tk. Menu(self.menubar, tearoff=0)
        self.algoBar.add_command(label="Articulation Point")
        self.algoBar.add_command(label="Bellman Ford")
        self.algoBar.add_command(label="BFS")
        self.algoBar.add_command(label="Bridges")
        self.algoBar.add_command(label="Dijkstra")
        self.algoBar.add_command(label="DFS")
        self.algoBar.add_command(label="Edmond-Karp")
        self.algoBar.add_command(label="Eulerian")
        self.algoBar.add_command(label="Floyd-Warshall")
        self.algoBar.add_command(label="Kruskal")
        self.algoBar.add_command(label="Prim")
        self.algoBar.add_command(label="Colorful Prim")
        self.algoBar.add_command(label="Topological Sort")
        self.menubar.add_cascade(label="Algorithms",menu = self.algoBar)

        #Create Canvas
        self.canvas = tk.Canvas(self, width=1280, height=720, bg='white')
        self.canvas.bind("<Button-1>", self.draw_circle)
        self.config(menu=self.menubar)
        self.title("Graph Analysis")
        self.canvas.pack()

    # def fileNew():
    #     #screen_width = root.winfo_screenwidth() - 100
    #     #screen_height = root.winfo_screenheight() - 150
    #     myToolbar = Toolbar(root)
    #     screen_width = 1600
    #     screen_height = 768
    #     w = Canvas(root, width=screen_width, height=screen_height, bg = "white")
    #     w.pack()

    # def fileOpen():
    #     global root
    #     root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
    #                                                 filetypes = (("grf files","*.grf"),("all files","*.*")))
    # def fileSaveas():
    #     global root
    #     root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save as...",
    #                                                 filetypes = (("grf files","*.grf"),("all files","*.*")))
    #     print (root.filename)

    def draw_circle(self,event):
        x,y = event.x,event.y

        #Draw a vertex 
        if(self.g.verify_v(x,y) is False):
            bbox = (x-20,y-20,x+20,y+20)
            self.canvas.create_oval(*bbox ,  width = 2)
            self.g.add_v(x,y)
            self.canvas.create_text(x,y, text = self.g.last)
            self.g.last = self.g.last+1
            self.line = False
            self.canvas.itemconfig(self.old_item ,outline = 'black')
            
        else:
            
            #Draw a line
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

            #Select a vertex and change the outline color
            else:
                self.old_item = self.canvas.find_closest(x+20,y+20)
                self.canvas.itemconfig(self.old_item ,outline = 'red')
                self.line_source = (x,y)
                self.line = True

app = App()
app.mainloop()
