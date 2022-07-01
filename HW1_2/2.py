from __future__  import print_function
import math
import random
from matplotlib import pyplot
import numpy as np
from numpy.random import randint
from numpy.random import rand

weight = [3.3, 3.4, 6.0, 26.1, 37.6, 62.5, 100.2, 141.1, 119.2, 122.4, 247.6, 352.0, 24.2, 32.1, 42.5]
survival_point = [7,8,13,29,48,99,177,213,202,210,380,485,9,12,15]


n_pop = 1
initial = []
c = list()


while len(initial)<n_pop:
    c = randint(0, 2, 15).tolist()
    if (c[0:3] == [0,0,0] or c[3:6] == [0,0,0] or c[6:12] == [0,0,0,0,0,0] or c[12:] == [0,0,0]) == False:
        sum_ = 0
        for i in range(len(c)):
            sum_ += c[i]*weight[i]
        if sum_ <= float(529):
            initial.append(c)


def function(x):
    ans = 0
    survival_point = [7,8,13,29,48,99,177,213,202,210,380,485,9,12,15]

    for i in range(len(x)):
        ans += x[i]*survival_point[i]

    if x[0]==1 and x[5] == 1:
        ans += 5
    if x[3]==1 and (x[8]==1 or x[9]==1):
        ans += 15
    if (x[7]==1 or x[10]==1) and (x[5]==1 and x[14]==1):
        ans += 25
    if (x[12]==1 and x[13]==1 and x[14]==1):
        ans += 70

    return ans


def check_weight(x,weight):
    sum_ = 0
    for i in range(len(x)):
        sum_ += x[i]*weight[i]
    if sum_ <= 529:
        return True

# ================== Hill climbing ================== #

def hill_climbing(N, variables, x):
    result = []
    walk_num = 1
    x1 = [randint(0, 2, 15).tolist()][0]
    while(walk_num<=200):
        u = random.randint(0,14)
        x1[u] = 1-x1[u]
        while (x1[0:3] == [0,0,0] or x1[3:6] == [0,0,0] or x1[6:12] == [0,0,0,0,0,0] or x1[12:] == [0,0,0]) or check_weight(x1, weight)!= True:
            u = random.randint(0,14)
            x1[u] = 1-x1[u]
            
        if(function(x1) > function(x)): # Find Better Solution
            x = x1.copy() # 下次從最佳解附近找candidate
        result.append(function(x))
        walk_num += 1

    print("最终最佳點:",x)
    print("最终最佳解:",function(x))

    return result

hill_climbing = hill_climbing(10, 15, initial[0])



# ================== Random Walk ==================
def random_walk(N, variables, x1):
    result = []
    pbest = function(x1)
    pbest_ = x1
    walk_num = 1
    while(walk_num<=200):
        u = random.randint(0,14)
        x1[u] = 1-x1[u]
        while (x1[0:3] == [0,0,0] or x1[3:6] == [0,0,0] or x1[6:12] == [0,0,0,0,0,0] or x1[12:] == [0,0,0]) or check_weight(x1, weight)!= True:
            u = random.randint(0,14)
            x1[u] = 1-x1[u]
            
        if(function(x1) > pbest): # Find Better Solution
            pbest = function(x1) # 存取歷史最佳解
            pbest_ = x1.copy() # 下次從最佳解附近找candidate

        result.append(pbest)
        walk_num += 1
        
    print("最终最佳點:",pbest_)
    print("最终最佳解:",pbest)

    return result

    
random_walk = random_walk(10, 2, initial[0])






# ================== genetic algorithm ==================
# genetic algorithm search of the one max optimization problem
from numpy.random import randint
from numpy.random import rand
import random

# objective function
# 把所有條件都算好 survival points加起來
def onemax(x):
    ans = 0
    survival_point = [7,8,13,29,48,99,177,213,202,210,380,485,9,12,15]

    for i in range(len(x)):
        ans += x[i]*survival_point[i]

    if x[0]==1 and x[5] == 1:
        ans += 5
    if x[3]==1 and (x[8]==1 or x[9]==1):
        ans += 15
    if (x[7]==1 or x[10]==1) and (x[5]==1 and x[14]==1):
        ans += 25
    if (x[12]==1 and x[13]==1 and x[14]==1):
        ans += 70

    #print(x)
    #print(ans)
    return ans

# roulette-wheel selection
def selection(pop, scores, k=3):
    max = 0
    for i in scores:
        max+=i
    pick = random.uniform(0, max)
    current = 0
    for j in range(len(scores)):
        current += scores[j]
        if current > pick:
            return pop[j]
    
def crossover(p1, p2, r_cross):
    c1, c2 = p1.copy(), p2.copy()
    if rand() < r_cross:
        # 隨機生成一個 crossover point (不能是最後一個)
        pt = randint(1, len(p1)-2) # 生成1~len(p1)-2的隨機整數
        # 進行 crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]

def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        if rand() < r_mut:
            # 把0轉換為1，1轉換為0
            bitstring[i] = 1 - bitstring[i]

ga_scores = []
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
    pop = list() ## 存放初始生成的組合
    while len(pop)<n_pop:
        c = randint(0, 2, 15).tolist()
        if (c[0:3] == [0,0,0] or c[3:6] == [0,0,0] or c[6:12] == [0,0,0,0,0,0] or c[12:] == [0,0,0]) == False:
            sum_ = 0
            for i in range(len(c)):
                sum_ += c[i]*weight[i]
            if sum_ <= 529:
                pop.append(c)
    	
    # 存放 best solution
    best, best_eval = 0, objective(pop[0])
    for gen in range(n_iter):
        # 計算candidate的objective function值
        scores = [objective(c) for c in pop]
        # 檢查是否大過目前最優解
        for i in range(n_pop):
            if scores[i] > best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))

            ga_scores.append(best_eval)

        # select 
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # 存放children
        children = list()

        for i in range(0, n_pop, 2):
            # 取兩個作為一對parents
            p1, p2 = selected[i], selected[i+1]
            # crossover ＆ mutation
            for c in crossover(p1, p2, r_cross):
                cond = False ## 預設cond為False
                while cond == False: ## 只要cond為False就要再次找新符合標準的組合
                    # mutation
                    mutation(c, r_mut)
                    # check是否符合條件(a)
                    if (c[0:3] == [0,0,0] or c[3:6] == [0,0,0] or c[6:12] == [0,0,0,0,0,0] or c[12:] == [0,0,0]) == False:
                        # check重量是否符合條件
                        sum_ = 0 # weight的計算結果
                        for k in range(len(c)):
                            sum_ += c[k]*weight[k]
                            
                        # 如果重量符合條件則新增為其中一個children
                        if sum_ <= float(529):
                            children.append(c)
                            cond = True
            # 把心找到的children設為下一次要做實驗的parents
            pop = children

    return [best, best_eval]


weight = [3.3, 3.4, 6.0, 26.1, 37.6, 62.5, 100.2, 141.1, 119.2, 122.4, 247.6, 352.0, 24.2, 32.1, 42.5]
survival_point = [7,8,13,29,48,99,177,213,202,210,380,485,9,12,15]


n_iter = 20 # 迭代次數
n_bits = 15 # 武器個數
n_pop = 10 # population size
r_cross = 0.1 # crossover probability
r_mut = 1.0 / float(n_bits) # mutation rate

best, score = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
print('f(%s) = %f' % (best, score))                                
#print(ga_scores)








# line plot of best scores  
pyplot.plot(hill_climbing, '.-', label = 'hill climbing')
pyplot.plot(random_walk, '.-', label = 'random walk')
pyplot.plot(ga_scores, '.-', label = 'genetic algorithm')
pyplot.legend(loc='lower right')
pyplot.xlabel('Iterations')  
pyplot.ylabel('Evaluation f(x)')  
pyplot.show()

