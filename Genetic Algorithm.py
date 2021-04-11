import random as random
from math import sqrt
import operator
import time, sys


config = {
    "goal" : [
                [1,1,1,1,1],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
             ],
    "mutation_percentage" : 0.001,
    "crossover_percentage" : 0.70,
}

spin = 4

number_of_generations = 0 
number_of_mutation = 0 


def animated_loading():
    global spin
    chars = "/—\|" 
    # for char in chars:
    sys.stdout.flush() 
    sys.stdout.write('\r'+'Bring your coffee ☕ ...'+chars[spin%4])
    spin+=1
        # time.sleep(.1)

class Parent:
    
    gen = 1
    child_number =1
    def __init__(self,chromosome,p1id=-1,p2id=-1):
        self.chromosome = chromosome
        self.id = Parent.child_number
        self.p1id = p1id
        self.p2id = p2id
        self.fitness =1e9
        self.mutation_map = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

        for i in range(5):
            for j in range(5):
                self.mutation_map[i][j]="\033[0;37;48m "+str(self.chromosome[i][j])+" \033[0m"

        self.generation = Parent.gen
        Parent.child_number+=1
        pass
    

    def print_mutation_map(self,):
        print("fitness:",round(self.fitness,5), "\ngen:",self.generation , "\tID:",self.id,"\nP1ID:",self.p1id,"\tP2ID:",self.p2id )
        for i in range(5):
            for j in range(5):
                print(self.mutation_map[i][j], end="\033[0;37;48m")
            print()
        print()
  
        pass

    def print_chromosome(self):
        print("fitness:",round(self.fitness,5), "\ngen:",self.generation , "\tID:",self.id,"\nP1ID:",self.p1id,"\tP2ID:",self.p2id )
        for i in range(5):
            for j in range(5):
                print(self.chromosome[i][j], end=" ")
            print()
        print()

        pass

    def calculate_fitness(self):
        sum = 0

        for i in range(5):
            for j in range(5):
                    sum += int((self.chromosome[i][j]!=config["goal"][i][j]))

        # if(sum != 0):
            self.fitness = sqrt(sum) 
        # else:
        #     self.fitness
        pass

    def crossover(self, parent2):
        Parent.gen +=1
        child1 = Parent([
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],self.id,parent2.id)

        child2 = Parent([
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],self.id,parent2.id)

        segment_start = random.randrange(0,25)
        segment_length = random.randrange(0,int(100*config["crossover_percentage"]))/4
        
        current = 0
        for i in range(5):
            for j in range(5):
                if current >= segment_start and current <= segment_start+segment_length:
                    current+=1
                
                    child1.chromosome[i][j]=self.chromosome[i][j]
                    child2.chromosome[i][j]=parent2.chromosome[i][j]

                    child1.mutation_map[i][j]=self.mutation_map[i][j]
                    child2.mutation_map[i][j]=parent2.mutation_map[i][j]

                else:

                    child1.chromosome[i][j]=parent2.chromosome[i][j]
                    child2.chromosome[i][j]=self.chromosome[i][j]

                    child1.mutation_map[i][j]=parent2.mutation_map[i][j]
                    child2.mutation_map[i][j]=self.mutation_map[i][j]
                    

        
        mutation_chance = random.randrange(0, int(1/config["mutation_percentage"]))
        
        global number_of_mutation
        
        if(mutation_chance == 1):
            number_of_mutation+=1
            

            random_i = random.randrange(0, 5)
            random_j = random.randrange(0, 5)

            if(random.randrange(0, 2)==0):
                child1.chromosome[random_i][random_j] = int(not child1.chromosome[random_i][random_j])
                child1.mutation_map[random_i][random_j] = "\033[1;31;48m "+str(child1.chromosome[random_i][random_j])+" \033[0m"

            else:
                child2.chromosome[random_i][random_j] = int(not child2.chromosome[random_i][random_j])
                child2.mutation_map[random_i][random_j] = "\033[1;31;48m "+str(child2.chromosome[random_i][random_j])+" \033[0m"


        return child1,child2
                


if __name__ == "__main__":  

    population  = [] 
    p1 = Parent([
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ])
    p2 = Parent([
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0], 
    ])


    p1.calculate_fitness()
    p2.calculate_fitness()
    
    population.append(p1)
    population.append(p2)
 
    try:
        start = time.perf_counter()
        while True:
            if random.randrange(0,100) < 3:
                animated_loading()

            population.sort(key=operator.attrgetter("fitness"))

            c1,c2 = population[0].crossover(population[1])
            
            c1.calculate_fitness()
            c2.calculate_fitness()
            
            population.append(c1)
            population.append(c2)

            if(c1.chromosome == config["goal"] or c2.chromosome==config["goal"]):
                end = time.perf_counter()
                sys.stdout.flush() 
                population.sort(key=operator.attrgetter("fitness"))
                for i in range(30):
                    try:
                        population[29-i].print_mutation_map()
                    except:
                        pass
                print("child found!")
                print("number of generations:",Parent.gen)
                print("number of mutations:",number_of_mutation)
                print("number of children:",len(population))
                print(f"Runtime: {end - start:0.6f} seconds")

                break
    except:
        end = time.perf_counter()
        sys.stdout.flush() 
        population.sort(key=operator.attrgetter("fitness")) 
        for i in range(30):
            try:
                population[29-i].print_mutation_map()
            except:
                pass
        print("inturpted!")
        print("number of generations:",Parent.gen)
        print("number of mutations:",number_of_mutation)
        print("number of children:",len(population))
        print(f"Runtime: {end - start:0.6f} seconds")

