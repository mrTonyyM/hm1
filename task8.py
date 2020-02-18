words = []
di = {}
with open(r'C:\Users\RobotOne\Downloads\dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip()
        words += line.lower().split()
        setWords = set(words)
for word in setWords:
        di[word] = words.count(word)
maxV = max(di.values())
res = []
for k , v in di.items():
        if maxV == v:
                res += [k]
minRes = min(res)
print(minRes, di[minRes])
with open (r'C:\Users\RobotOne\Downloads\task8.txt', 'w') as outF:
        outF.write(str(minRes)+' '+str(di[minRes]))