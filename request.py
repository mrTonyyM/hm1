a = int(input())
b = int(input())
i = 1
if a > b:
    maxV = a
    minV = b
else:
    maxV = b
    minV = a
while i <= maxV:
    d1 = maxV*i
    i += 1
    if d1 % minV == 0:
        print(d1)
        break