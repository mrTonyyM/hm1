while True:
    val1,val2,val3 = input().split(' ',',')
    val = int(val1)*int(val2)*int(val3)
    if val < 10:
        continue
    elif val > 100:
        break
    print(val)