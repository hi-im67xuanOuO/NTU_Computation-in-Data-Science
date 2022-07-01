from __future__  import print_function
import math
import random
from matplotlib import pyplot
import numpy as np

def function(x):
    r = 6*x[0]*x[0] - 6*x[0]*x[1] + 2*x[1]*x[1] - x[0] -2*x[1]
    return r

#initial = [random.uniform(-40,40), random.uniform(-40,40)]
initial = [6.76, 8.6]
#initial = [20,20]

# ================== Hill climbing ================== #

def hill_climbing(N, variables, x):
    result = []
    walk_num = 1
    while(len(result)<10):
        u = [random.uniform(-1,1) for i in range(variables)] 
        u1 = [u[i]/math.sqrt(sum([u[i]**2 for i in range(variables)])) for i in range(variables)]
        x1 = [x[i] + u1[i] for i in range(variables)]
        if(function(x1) < function(x)): # Find Better Solution
            x = x1 # 下次從最佳解附近找candidate
            result.append(function(x))
        walk_num += 1
        #print(walk_num)

    print("hill_climbing最终最佳點:",x)
    print("hill_climbing最终最佳解:",function(x))

    return result

hill_climbing = hill_climbing(10, 2, initial)



# ================== Random Walk ==================
def random_walk(N, variables, x):
    result = []
    pbest = function(x)
    pbest_ = x
    walk_num = 1
    while(len(result)<10):
        u = [random.uniform(-1,1) for i in range(variables)] # 隨機變數
        u1 = [u[i]/math.sqrt(sum([u[i]**2 for i in range(variables)])) for i in range(variables)]
        x1 = [x[i] + u1[i] for i in range(variables)]
        if(function(x1) < pbest): # Find Better Solution
            pbest = function(x1) # 存取歷史最佳解
            pbest_ = x1 # 存取歷史最佳點
            result.append(function(x1))
            print(len(result))
        x = x1 # 下次從目前所在位置繼續搜尋candidate
        walk_num += 1

    print("random_walk最终最佳點:",pbest_)
    print("random_walk最终最佳解:",pbest)

    return result

    
random_walk = random_walk(10, 2, initial)



# ================== SA ==================
def SA(eta, k, t, initial):
    result = []
    x_old = initial
    x_best = function(x_old)
    best = x_old

    #times = 0
    #while times < 100:
    while t>=0.2:
        value_old = function(x_old)
        x_new = [x_old[0] + random.uniform(-1,1), x_old[1] + random.uniform(-1,1)]
        value_new = function(x_new)
        res = value_new-value_old
        if res<0 or np.exp(-res/(k*t))>np.random.rand():
            x_old = [x_new[0], x_new[1]]
            if value_new < x_best:
                x_best = function(x_new)
                best = x_new
                result.append(function(x_new))
        t = t*eta
        #times += 1
        if len(result) >= 10:
            break
    
    print("SA最终最佳點: ",best[0], " " ,best[1])
    print("SA最终最佳解：",x_best)

    return result


SA = SA(0.95, 1, 1000, initial)





# line plot of best scores  
pyplot.plot(hill_climbing, '.-', label = "hill_climbing")
pyplot.plot(random_walk, '.-', label = "random_walk")
pyplot.plot(SA, '.-', label = "SA")
pyplot.legend(loc='upper right')
pyplot.xlabel('Times')  
pyplot.ylabel('Evaluation f(x)')  
pyplot.show()
