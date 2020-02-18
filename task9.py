
def average (ls):
    sum = 0
    for l in ls:
        l = int(l)
        sum += l
    return sum/len(ls)

with open(r'C:\Users\RobotOne\Downloads\task9_1.txt','r', encoding="utf-8") as inf:
    makrMath,makrPhis,makrRus = [],[],[]
    for line in inf:
        line = line.strip()
        words = line.split(';')
        marks = words[1:]
        makrMath += [marks[0]]
        makrPhis += [marks[1]]
        makrRus += [marks[2]]
        print(average(marks))
    print(average(makrMath),average(makrPhis),average(makrRus))