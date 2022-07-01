
## Q1 linear programming
def f(x):
    ans = -(x**5) + 5*(x**3) + 20*x -5        
    return ans

from scipy import optimize
max_ = optimize.fminbound(lambda x: -f(x), -4, 4)

print("Q1 Answer: ")
print("x = ",max_)
print("f(x) = ",f(max_))






## Q2 linear programming

from gekko import GEKKO

y = ['Shadow Daggers','Huntsman Knife','Gut Knife','228 Compact Handgun',
     'Night Hawk', 'Desert Eagle Magnum', 'Ingram MAC-10 SMG', 'Leone YG1265 Auto Shotgun',
     'M4A1 Carbine', 'AK-47 Rifle', 'Krieg 550 Sniper Rifles', 'M249 Machine Gun',
     'Gas Mask','Night-Vision Goggle','Tactical Shield']
v = [7,8,13,29,48,99,177,213,202,210,380,485,9,12,15]
w = [3.3, 3.4, 6.0, 26.1, 37.6, 62.5, 100.2, 141.1, 119.2, 122.4, 247.6, 352.0, 24.2, 32.1, 42.5]
items = len(y)


# Create model
m = GEKKO()

#####
eq = m.Param(value=1)

# Variables
x = m.Array(m.Var,len(y),lb=0,ub=1,integer=True) ## 0 或 1

# Objective
m.Maximize(m.sum([v[i]*x[i] for i in range(items)]))

# Constraint
limit = 529 #重量限制
m.Equation(m.sum([w[i]*x[i] for i in range(items)]) <= limit)
m.Equation(m.sum([x[i] for i in range(3)]) >= eq)
m.Equation(m.sum([x[i] for i in range(3,6)]) >= eq)
m.Equation(m.sum([x[i] for i in range(6,12)]) >= eq)
m.Equation(m.sum([x[i] for i in range(12,15)]) >= eq)

# Optimize with APOPT
m.options.SOLVER = 1

m.solve()


print("Q2 Answer: ")
# Print the value of the variables at the optimum
for i in range(items):
    print("%s = %f" % (y[i], x[i].value[0]))

# Print the value of the objective
#print("Objective = %f" % (m.options.objfcnval))


ans = m.options.objfcnval

# 題目給的條件 (達成加分)
if x[0].value[0]==1 and x[5].value[0] == 1:
    ans -= 5
if x[3].value[0]==1 and (x[8].value[0]==1 or x[9].value[0]==1):
    ans -= 15
if (x[7].value[0]==1 or x[10].value[0]==1) and (x[5].value[0]==1 and x[14].value[0]==1):
    ans -= 25
if (x[12].value[0]==1 and x[13].value[0]==1 and x[14].value[0]==1):
    ans -= 70

print("Objective = %f" % (ans))
