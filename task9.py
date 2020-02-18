import numpy as np
with open(r'C:\Users\RobotOne\Downloads\task9_1.txt','r', encoding="utf-8") as inf:
    for line in inf:
        line = line.strip()
        words = line.split(';')
        print(words)
        marks = words[1:]
        sum = 0
        for mark in marks:
            mark = int(mark)
            sum += mark

        print(sum/len(marks))
        # print(np.mean(marks))