
## 解法：暴力算出所有可能組合，再計算符合條件的組合數量

import numpy as np

weight = [3.3, 3.4, 6.0, 26.1, 37.6, 62.5, 100.2, 141.1, 119.2, 122.4, 247.6, 352.0, 24.2, 32.1, 42.5]
sum_=0
count = 0
total_count = 0
c = []
for a_1 in range(2):
    for a_2 in range(2):
        for a_3 in range(2):
            for a_4 in range(2):
                for a_5 in range(2):
                    for a_6 in range(2):
                        for a_7 in range(2):
                            for a_8 in range(2):
                                for a_9 in range(2):
                                    for a_10 in range(2):
                                        for a_11 in range(2):
                                            for a_12 in range(2):
                                                for a_13 in range(2):
                                                    for a_14 in range(2):
                                                        for a_15 in range(2):
                                                            c.append(a_1)
                                                            c.append(a_2)
                                                            c.append(a_3)
                                                            c.append(a_4)
                                                            c.append(a_5)
                                                            c.append(a_6)
                                                            c.append(a_7)
                                                            c.append(a_8)
                                                            c.append(a_9)
                                                            c.append(a_10)
                                                            c.append(a_11)
                                                            c.append(a_12)
                                                            c.append(a_13)
                                                            c.append(a_14)
                                                            c.append(a_15)

                                                            total_count+=1

                                                            if (c[0:3] == [0,0,0] or c[3:6] == [0,0,0] or c[12:] == [0,0,0]) == False:
                                                                for i in range(len(c)):
                                                                    sum_ += c[i]*weight[i]
                                                                if sum_ <= 529:
                                                                    count+=1

                                                            c = []
                                                            sum_ = 0


#print("總共可能解數量:",total_count)
print("總共可能解數量:",count)                                                    
    
