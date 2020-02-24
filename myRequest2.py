import requests
i = 0
with open(r'C:\Users\RobotOne\Downloads\dataset_3378_3(1).txt') as inf:
    filename = inf.readline().strip().split('/')
    filename = filename[7]
    while True:
        i += 1
        print(i)
        print('https://stepic.org/media/attachments/course67/3.6.3/' + filename)
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename)
        line = r.text.split()
        print(line[0])
        if (line[0] == 'We'):
            print(r.text)
            print(line)
            break
        else:
            filename = r.text