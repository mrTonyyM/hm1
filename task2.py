a = int(input())
b = int(input())
c = int(input())
d = int(input())
for k in range(c,d+1):
    print('\t',  k, end = '')
print()
for i in range(a,b+1):
    s = str(i)
    for j in range(c,d+1):
        s = s +'\t' + str(i*j)
    print(s)
