import operator
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
        self.id=Grid.counter
        Grid.counter+=1
        self.parent = parent
        self.grid = grid
        self.empty_at = [-1,-1]
        self.fitness = 0

    def calculate_fitness(self,):
        # fitness = 0
        # output(self)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]==0:
                    self.empty_at = [i,j]
                g.fitness += abs(distance[self.grid[i][j]][0] - i) + abs(distance[self.grid[i][j]][1] - j)

        return g.fitness


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
    print(g.fitness,g.id)
    print("")
        
def output_grid(g):
    for i in g:
        print(i)
    print("")

def get_first(queue):
    queue.sort(key=operator.attrgetter("fitness"))
    first = []
    for i in range(len(queue)):
        if queue[i].fitness==queue[0].fitness:
            first.append(queue[i])
            output(queue[i])
    return first

def BFS(g):
    parent = g.parent

    steps = [[0,1],[1,0],[0,-1],[-1,0]]

    queue = []
    queue.append(g)

    while( g.grid != goal and len(queue)>0):
        
        queue = get_first(queue)
        print(queue)
        for s in steps:
            if(g.empty_at[0]+s[0] in range(n) and g.empty_at[1]+s[1] in range(m)):
                cgrid = [ 
                        [None,None,None],
                        [None,None,None],
                        [None,None,None],
                        ] 
                for i in range(len(cgrid)):
                    for j in range(len(cgrid[i])):
                        cgrid[i][j]=g.grid[i][j]
                        pass
                cgrid[g.empty_at[0]+s[0]][g.empty_at[1]+s[1]] , cgrid[g.empty_at[0]][g.empty_at[1]] = cgrid[g.empty_at[0]][g.empty_at[1]],cgrid[g.empty_at[0]+s[0]][g.empty_at[1]+s[1]]            

                child = Grid(cgrid,g.empty_at)
                print(child.calculate_fitness())
                # print(child.fitness)
                # child.fitness = child.calculate_fitness()
                # print(child.fitness)

                # output(child)
                
                queue.append(child)
            pass 
        break
        pass   

if __name__ == "__main__":
    initialize()
    print(distance)
    
    g = Grid([
        [2,1,3],
        [8,0,4],
        [7,6,5],
    ])

    print(g.calculate_fitness())
    print(g.fitness)

    output(g)
    BFS(g)
    # get_nabors(g)
    output(g)

    a =1
    b= 2
    a,b = b,a

    print(a,b)
    # print(cgrid)