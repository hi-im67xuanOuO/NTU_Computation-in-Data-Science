from random import *
import random
import numpy as np
from matplotlib import pyplot
import math
from pprint import pprint

# =========================== hill_climbing ===========================

def randomSolution(tsp):
    #cities = list(range(len(tsp)))
    cities = [num for num in range(1,15)]
    solution = []
    solution.append(0)
    for i in range(len(tsp)-1):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

def getNeighbours(solution):
    neighbours = []
    for i in range(1,len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp, neighbours, time):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
        time+=1
        #print(time)
    return bestNeighbour, bestRouteLength, time

def hillClimbing(tsp):
    result = []
    time = 1
    
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    
    bestNeighbour = neighbours[0] 
    bestNeighbourRouteLength = routeLength(tsp, bestNeighbour) 

    while time<=100:
        neighbours = getNeighbours(currentSolution)

        random_ = random.randrange(0, len(neighbours))
        neighbor = neighbours[random_]
        
        RouteLength = routeLength(tsp, neighbor)
        if RouteLength <= bestNeighbourRouteLength:
            bestNeighbourRouteLength = RouteLength
            currentSolution = neighbor # 從現在位置繼續找
           
        result.append(bestNeighbourRouteLength)
        time += 1
        #print("time：",time)


    return currentSolution, bestNeighbourRouteLength, result



# =========================== random_walk ===========================

def randomSolution_2(tsp):
    cities = [num for num in range(1,15)]
    solution = []
    solution.append(0)
    for i in range(len(tsp)-1):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution

def routeLength_2(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

def getNeighbours_2(solution):
    neighbours = []
    for i in range(1,len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def random_walk(tsp):
    result = []
    time = 1
    
    currentSolution = randomSolution_2(tsp)
    currentRouteLength = routeLength_2(tsp, currentSolution)
    neighbours = getNeighbours_2(currentSolution)

    random_ = random.randrange(0, len(neighbours))
    neighbor = neighbours[random_]
    RouteLength = routeLength_2(tsp, neighbor)
    
    bestNeighbour = neighbor
    bestNeighbourRouteLength = RouteLength
    BEST = bestNeighbour # 初始化最佳解
    BEST_LENGTH = bestNeighbourRouteLength # 初始化最佳解長度
    
    while time<=100:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength

        if (currentRouteLength < BEST_LENGTH):
            BEST = currentSolution
            BEST_LENGTH = currentRouteLength

        result.append(BEST_LENGTH)
        
        neighbours = getNeighbours_2(currentSolution)
        random_ = random.randrange(0, len(neighbours))
        bestNeighbour = neighbours[random_]
        bestNeighbourRouteLength = routeLength_2(tsp, bestNeighbour)

        #result.append(currentRouteLength)
        time += 1
        #print("time：",time)
    
    return BEST, BEST_LENGTH, result





# =========================== tabu_search ===========================

def path_length(path, distance):
    cities_pairs = zip(path, path[1:])
    consecutive_distances = [(distance[a][b]) for (a, b) in cities_pairs]
    return round(sum(consecutive_distances), 2)


def tabu_search(distance):
    ilosc = 15 # 城市個數
    iter_ = 1

    pbest = [n for n in range(ilosc)]
    pbest_x = pbest
    pbest_y = path_length(pbest_x, distance)
    pcur_x = pbest_x
    pcur_y = pbest_y
    tabu = []
    moveb = []
    score = []
    #for n in range(1,iter_):
    while iter_<=100:
        pnew = []
        for i in range(1, len(pbest_x)-1):
            for j in range(2, len(pbest_x)-1):
                if (i != j) and (i < j):
                    acopy = pbest_x
                    acopy[i], acopy[j] = acopy[j], acopy[i]
                    acopy_ = acopy
                    length = path_length( acopy_,distance )
                    move = [i,j]
                    if ( ( (moveb not in tabu) ) and ( ( length<path_length(pnew,distance) ) or ( pnew==[] ) ) or (length<=pbest_y) ):
                        if pnew != []:
                            pnew = []
                            for i in acopy_:
                                pnew.append(i)
                        else:
                            for i in acopy_:
                                pnew.append(i)
                        #pnew = acopy_
                        moveb = move
                        
        pcur_x = pnew
        if pcur_x!=[]:
            if path_length(pcur_x,distance) <= path_length(pbest_x,distance):
                pbest_x = pcur_x
                pbest_y = path_length(pcur_x,distance)
                score.append(pbest_y)
            if moveb not in tabu:
                tabu.append(moveb)
            if len(tabu) >= 10:
                tabu.pop(0)

            iter_ += 1
            if iter_ >= 100:
                break
            #else:
                #score.append(pbest_y)
    
    return pbest_x, tabu, path_length(pbest_x,distance), score



# =========================== SA ===========================

def SA(distmat):
    num = 15 #城市數量
    distmat = np.asarray(distmat)
    solutionnew = np.arange(num)
    solutioncurrent = solutionnew.copy()
    valuecurrent =99000  
    solutionbest = solutionnew.copy()
    valuebest = 99000 
    iter_ = 100
    result = [] 
    time = 0
    solutions = []
    while time < iter_:
        loc1 = np.int(np.ceil(np.random.rand()*(num-1)))
        loc2 = np.int(np.ceil(np.random.rand()*(num-1)))
        if loc1 != loc2:
            solutionnew[loc1],solutionnew[loc2] = solutionnew[loc2],solutionnew[loc1]
            
        valuenew = 0
        for i in range(num-1):
            valuenew += distmat[solutionnew[i]][solutionnew[i+1]]
        valuenew += distmat[solutionnew[0]][solutionnew[14]]
        if valuenew<valuecurrent: 
            valuecurrent = valuenew
            solutioncurrent = solutionnew.copy()
            if valuenew < valuebest:
                valuebest = valuenew
                solutionbest = solutionnew.copy()
        else:
            if np.random.rand() < np.exp(-(valuenew-valuecurrent)/time):
                valuecurrent = valuenew
                solutioncurrent = solutionnew.copy()
            else:
                solutionnew = solutioncurrent.copy()
                    
        solutions.append(solutionnew)
        time += 1
        result.append(valuebest)
    best_length = min(result)
    best_ = solutions[result.index(best_length)]

    return best_length, best_, result







def main():
    city = ["Incheon" ,"Seoul" ,"Busan" ,"Daegu" ,"Daejeon" ,
        "Gwangju" ,"Suwon-si" ,"Ulsan" ,"Jeonju" ,"Cheongju-si" ,
        "Changwon" ,"Jeju-si" ,"Chuncheon" ,"Hongsung" ,"Muan"]
    
    tsp = [
        [0,27,335,244,141,257,33,316,186,115,304,439,102,95,275],
        [27,0,330,237,144,268,31,307,195,113,301,453,75,111,290],
        [335,330,0,95,199,193,304,54,189,221,35,291,330,271,233],
        [244,237,95,0,117,171,212,75,130,130,72,324,236,191,215],
        [141,144,199,117,0,137,114,192,61,36,167,323,175,74,171],
        [257,268,193,171,137,0,238,222,77,173,161,186,311,162,44],
        [33,31,304,212,114,238,0,284,164,84,274,423,91,83,260],
        [316,307,54,75,192,222,284,0,198,205,67,341,296,266,265],
        [186,195,189,130,61,77,164,198,0,96,154,263,234,97,111],
        [115,113,221,130,36,173,84,205,96,0,190,359,139,74,205],
        [304,301,35,72,167,161,274,67,154,190,0,275,306,237,202],
        [439,453,291,324,323,186,423,341,263,359,275,0,498,344,165],
        [102,75,330,236,175,311,91,296,234,139,306,498,0,170,340],
        [95,111,271,191,74,162,83,266,97,74,237,344,170,0,180],
        [275,290,233,215,171,44,260,265,111,205,202,165,340,180,0]
        ]

    currentSolution, bestNeighbourRouteLength, result = hillClimbing(tsp)
    BEST, BEST_LENGTH, result2 = random_walk(tsp)
    pbest_x, tabu, best_length, result3 = tabu_search(tsp)
    best_length, best_, result4 = SA(tsp)


    print("Hill Climbing:")
    print("最佳路線：",currentSolution)
    print("最佳路線長度：",bestNeighbourRouteLength)

    print("Random Walk:")
    print("最佳路線：", BEST)
    print("最佳路線長度：", BEST_LENGTH)

    print("Tabu Search:")
    print("最佳路線：", pbest_x)
    print("最佳路線長度：", best_length)
    print("Tabu List：", tabu)

    print("Simulated Annealing:")
    print("最佳路線：", best_)
    print("最佳路線長度：", best_length)
    
    
    # line plot of best scores  
    pyplot.plot(result, '.-', label = "Hill climbing")
    pyplot.plot(result2, '.-', label = "Random walk")
    pyplot.plot(result3, '.-', label = "Tabu search")
    pyplot.plot(result4, '.-', label = "SA")
    pyplot.legend(bbox_to_anchor=(1.05, 1.0),loc='best')
    pyplot.xlabel('Iterations')  
    pyplot.ylabel('Evaluation f(x)')  
    pyplot.show()

if __name__ == "__main__":
    main()
