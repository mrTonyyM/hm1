import requests
with open (r'C:\Users\RobotOne\Downloads\dataset_3378_2.txt') as inf:
    for line in inf:
        line = line.strip()
print(line)
r = requests.get(line)
nstr = r.text.splitlines()
# print(r.text)
print(nstr)

