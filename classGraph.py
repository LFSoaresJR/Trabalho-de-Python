class Graph:
    def __init__(self):
        self.g = [] #Graph in adjacency list
        self.coord = {} #Dictionary with coordinates of each vertex
        self.last = 0 # Account about wich vertex is being created

    def add_v(self,x,y): #Add a new vertex to the variables
        self.coord[(x,y)] = self.last 
        self.g.append([])
    
    def verify_v(self,x,y): #Verify if the point wich the vertex is being do not overlap another
        for i in self.coord:
            if((x<=i[0]+40 and x>=i[0]-40) and (y<=i[1]+40 and y>=i[1]-40)):
                return True
        return False

    def connection(self,x1,y1,x2,y2): #Make connection between the two vertex selected, adding to the adjacency list 
        for i in self.coord:
            if((x1<=i[0]+20 and x1>=i[0]-20) and (y1<=i[1]+20 and y1>=i[1]-20)):
                x1 = i[0] 
                y1 = i[1]
                m = self.coord[(x1,y1)]
                for j in self.coord:
                    if((x2<=j[0]+20 and x2>=j[0]-20) and (y2<=j[1]+20 and y2>=j[1]-20)):
                        x2 = j[0]
                        y2 = j[1]
                        n = self.coord[(x2,y2)]
                        self.g[m].append(n)
                        self.g[n].append(m)
                        return (x1,y1,x2,y2)