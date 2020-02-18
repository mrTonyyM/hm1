mtrx = []
mtrx2 = []
while True:
    s = [i for i in input().split()]
    if s[0] == 'end': break
    s = [int(i) for i in s]
    mtrx.append(s)
n = len(mtrx)
m  = len(mtrx[0])
print(' строка ' , n)
print(' столбец ' , m)

# mtrx2 = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         #mtrx2[i][j] = mtrx[i-1][j] + mtrx[i+1-n][j] + mtrx[i][j-1] + mtrx[i][j+1-n]
#         print(mtrx2[i][j], end = ' ')
#     print()