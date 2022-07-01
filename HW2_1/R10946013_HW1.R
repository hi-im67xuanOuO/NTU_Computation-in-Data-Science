census_tract <- read.csv("HW1_census-tract_data.csv", header=TRUE, fill=FALSE)
census_tract <- census_tract[2:6]
View(census_tract)

## 針對X5運算
census_tract[5] <- census_tract[5]*100
X_bar <- round(apply(census_tract, 2, mean),2)
X_bar
S <- round(var(census_tract),3) ## 計算covariance
View(S)
eigen_original <- eigen(S)
eigen_original$values
round(eigen_original$vectors,3)

# 特徵值佔總特徵值的比例，等於每個PC的方差占總方差的比例
eigen_original$values/sum(eigen_original$values)

## Notes:
## eigenvalues 就是 lambda




#0.781 * sqrt(6.93129415) / sqrt(4.308)
#0.306 * sqrt(6.93129415) / sqrt(1.767)
#0.334 * sqrt(6.93129415) / sqrt(0.801)
## 前兩項的eigenvector值*sqrt(那一項的eigenvalue)/sqrt(那一項的covariance=自己的variance)
eigenvector = round(eigen_original$vectors,3)[,1:2]
eigenvalue = round(eigen_original$values,3)[1:2]
pc_1 = eigenvector[,1] * sqrt(eigenvalue[1])
pc_2 = eigenvector[,2] * sqrt(eigenvalue[2])
for (i in 1:length(pc_1)) {
  print(pc_1[i] / sqrt(S[i,i]))
}
for (i in 1:length(pc_2)) {
  print(pc_2[i] / sqrt(S[i,i]))
}














# 標準化
#Z <- apply(census_tract, 2, scale)
#View(Z)
#R <- round(var(Z), 3)
#View(R)
#eigen_std <- eigen(R)
#eigen_std$values
#eigen_std$vectors

# 特徵值佔總特徵值的比例，等於每個PC的方差占總方差的比例
#eigen_std$values/sum(eigen_std$values)



#eigenvector = round(eigen_original$vectors,3)[,1:2]
#eigenvalue = round(eigen_original$values,3)[1:2]
#pc_1 = eigenvector[,1] * sqrt(eigenvalue[1])
#pc_2 = eigenvector[,2] * sqrt(eigenvalue[2])
#for (i in 1:length(pc_1)) {
#  print(pc_1[i] / sqrt(S[i,i]))
#}
#for (i in 1:length(pc_2)) {
#  print(pc_2[i] / sqrt(S[i,i]))
#}

