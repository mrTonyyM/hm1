
e=int(input('введите число ступеней'))

str=''
strSH=''
for x in range(e,0,-1):
    strSH += '#'
    str=" "*(x-1)
    print(str+strSH)
    str=''
strSH=''