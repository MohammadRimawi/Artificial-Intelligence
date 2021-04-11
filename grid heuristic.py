import operator,random
goal = [
    [1,2,3],
    [8,0,4],
    [7,6,5],
]

n = 3
m = 3

class Grid:
    counter = 0
    def __init__(self,grid,parent=[-1,-1]):
        self.id = Grid.counter
        Grid.counter+=1
        self.parent = parent
        self.grid = grid
        self.empty_at = [-1,-1]
        self.fitness = 0

    def calculate_fitness(self,):
        fitness = 0
        # output(self)
        self.fitness = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]==0:
                    self.empty_at = [i,j]
                fitness += abs(distance[self.grid[i][j]][0] - i) + abs(distance[self.grid[i][j]][1] - j)

        self.fitness = fitness
        return self.fitness


distance = [
    [None,None], 
]*n*m

def initialize():
    for i in range(len(goal)):
        for j in range(len(goal[i])):
            distance[goal[i][j]]=[i,j]
    pass

def output(g):
    for i in g.grid:
        print(i)
    print("fitness:",g.fitness,"\nID:",g.id,"\nparent:",g.parent,"\nempty at:",g.empty_at)
    print("")
        
def output_grid(g):
    for i in g:
        print(i)
    print("")

def get_first(queue):
    queue.sort(key=operator.attrgetter("fitness"))
    for i in range(min(5,len(queue))):
        output(queue[i])
        # print("***********************************")
    first = []
    for i in range(len(queue)):
        if queue[i].fitness==queue[0].fitness or i<100:
            first.append(queue[i])
            # output(queue[i])
    # print(first)
    # return queue
    return first

def BFS(src):
    parent = src.parent

    steps = [[0,1],[1,0],[0,-1],[-1,0]]

    current_queue = []
    next_queue = []

    next_queue.append(src)

    while( src.grid != goal):
        random.shuffle(steps)
        print(steps)
        current_queue=[]
        current_queue = get_first(next_queue)
        next_queue = []
        
        for i in range(len(current_queue)):
            src = current_queue[i]
            for s in steps:
                if(src.empty_at[0]+s[0] in range(n) and src.empty_at[1]+s[1] in range(m) and [src.empty_at[0]+s[0],src.empty_at[1]+s[1]]!=src.parent):
                    cgrid = [ 
                            [None,None,None],
                            [None,None,None],
                            [None,None,None],
                            ] 
                    for i in range(len(cgrid)):
                        for j in range(len(cgrid[i])):
                            cgrid[i][j]=src.grid[i][j]
                            pass
                    cgrid[src.empty_at[0]+s[0]][src.empty_at[1]+s[1]] , cgrid[src.empty_at[0]][src.empty_at[1]] = cgrid[src.empty_at[0]][src.empty_at[1]],cgrid[src.empty_at[0]+s[0]][src.empty_at[1]+s[1]]            

                    child = Grid(cgrid,src.empty_at)
                    child.calculate_fitness()
    
                    child.calculate_fitness()
        
                    output(child)
                    
                    if (child.grid == goal):
                        print("***************************")
                        output(child.grid)
                        return 0 
                    
                    next_queue.append(child)
            pass 
        # break
        output(src) 

if __name__ == "__main__":
    initialize()
    print(distance)
    
    g = Grid([
        [2,8,3],
        [6,5,1],
        [0,7,4],
    ])

    g.calculate_fitness()
    

    BFS(g)
    # get_nabors(g)
    # output(g)
    # output(h)
    # output(u)

   