def my_range(start, stop, step = 1):
    result = []
    x = start
    if step > 0: sign = 1
    else: sign = -1
    print(sign*(x < stop))
    while sign*(x < stop):
        result += [x]
        x += step
    return result

# print(my_range(2,15,3))

def modify_list(l):
    n_circus = len(l)-1
    for i in range(n_circus,-1,-1):
        if l[i] % 2 != 0:
            # del (l[i])
            l.remove(l[i])
        else:
            l[i] = l[i] // 2

ls = [10,5,8,3]
modify_list(ls)
print(ls)