# removing the duplicates

numbers = [2,5,2,3,4,5,7,6,6]

uniqueList = []

for i in numbers:
    if i not in uniqueList:
        uniqueList.append(i)

print(uniqueList)