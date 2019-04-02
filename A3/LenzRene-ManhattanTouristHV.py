#!usr/bin/env python3

import sys

inputData = sys.stdin
weightList = []
inputData.readline()

for r in inputData.readlines():
        weight = r.strip("  ").strip(" \n").split("   ")

        if (len(weight) > 1):
            rowLength = len(weight)
            weightList.append(weight)

allCols = len(weightList)
columns = len(weightList[0])
rows = len(weightList[allCols-1])+1

weightCount={}
for i in range(rows):
    weightCount[i]=[]
    for j in range(columns):
        weightCount[i].append(0)

for i in range(rows-1):
    weightCount[0][i+1] = round(weightCount[0][i] + float(weightList[rows-1][i]),2)

for i in range(columns-1):
    weightCount[i+1][0] = round(weightCount[i][0] + float(weightList[i][0]),2)

for j in range(rows-1):       
        for i in range(columns-1):
                down = round(weightCount[j][i+1]+ float(weightList[j][i+1]),2)
                right = round(weightCount[j+1][i]+ float(weightList[rows+j][i]),2)
                if (down > right):
                        weightCount[j+1][i+1] = down
                else:
                        weightCount[j+1][i+1] = right

print(weightCount[rows-1][columns-1])

