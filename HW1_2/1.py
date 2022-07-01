import numpy as np
import matplotlib.pyplot as plt
class particle:
    def __init__(self):
        self.pos = 0
        self.speed = 0
        self.pbest = 0

class PSO:
    def __init__(self):
        ## 初始值設定
        self.w = 1
        self.c1 = 1
        self.c2 = 1
        self.gbest = 0
        self.N = 4
        self.POP = []
        self.iter_N = 20

    def fitness(self, x):
        ## objective function
        return -(x**5) + 5*(x**3) + 20*x -5        

    def g_best(self, pop):
        for bird in pop:
            if bird.fitness > self.fitness(self.gbest):
                self.gbest = bird.pos

    def initPopulation(self, pop, N):
        ########### 題目要求的起始位置 ##########
        init_ = [-2,0,1,3]
        ######################################
        for i in range(N):
            bird = particle()
            bird.pos = init_[i]
            bird.fitness = self.fitness(bird.pos)
            bird.pbest = bird.fitness
            pop.append(bird)

        self.g_best(pop)

    def update(self, pop):
        for bird in pop:
            speed = self.w * bird.speed + self.c1 * np.random.random() * (bird.pbest - bird.pos) + self.c2 * np.random.random() *  (self.gbest - bird.pos)
            pos = bird.pos + speed
            ## X值範圍(題目規定的)
            if -4 <= pos <= 4:
                bird.pos = pos
                bird.speed = speed
                bird.fitness = self.fitness(bird.pos)
                if bird.fitness > self.fitness(bird.pbest):
                    bird.pbest = bird.pos

    def implement(self):
        self.initPopulation(self.POP, self.N)
        for i in range(self.iter_N):
            self.update(self.POP)
            self.g_best(self.POP)

pso = PSO()
pso.implement()

best_x=0
best_y=0
for ind in pso.POP:
    if ind.fitness>best_y:
        best_y=ind.fitness
        best_x=ind.pos
print("x = ", best_x)
print("f(x) = ", best_y)

x = np.linspace(-4, 4, 100000)

def fun(x):
    return -(x**5) + 5*(x**3) + 20*x -5        
y=fun(x)
plt.plot(x, y)

plt.scatter(best_x,best_y,c='r',label='best point')
plt.legend()
plt.show()
                
