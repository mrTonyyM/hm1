ls = []
ls2 = []
while True:
    val = int(input())
    ls.append(val)
    if sum(ls) == 0: break
print(ls)
for x in ls:
    sqr = x*x
    ls2.append(sqr)
ss=sum(ls2)
print(ss)

n = int(input())
for x in range(n):
    for j in range(x+1):
        print(x+1, end = ' ')