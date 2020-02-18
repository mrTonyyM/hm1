s_value=''
value = None
with open(r'C:\Users\RobotOne\Downloads\dataset_3363_2(2).txt') as inf:
    for line in inf:
        line = line.strip()
        key = line[0]
        for ch in line:
            if ch.isalpha():
                if value != None:
                    print(key*value,end = '')
                s_value = ''
                key = ch
            else:
                s_value += ch
                value = int(s_value)
        print(key*value)
# with open(r'C:\Users\RobotOne\Downloads\dataset_3363_OUT.txt') as ouf:
#     ouf.write(s)