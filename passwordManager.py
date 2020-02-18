import random
enterData = input()
listData = list(enterData)
listNum=[]
for x in range(len(enterData)):
    listNum[x] = random.randint(len(enterData))
listData