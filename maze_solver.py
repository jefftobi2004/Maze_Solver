import sys
from tabulate import tabulate
#import copy

v = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m=[int(x) for x in input().split()]
x = [1]*(m+2)
v.append(x)
for i in range(1, n+1):

    line = list(tuple([1]) + tuple([int(j) for j in input().split()]) + tuple([1]))

    v.append(line)

v.append(x)
iS,js,ie,je=[int(x) for x in input().split()]

def bk(i,j,pas):
    global iS, ie, js, je, v
    #print(i, j, pas)

    if v[i][j] == 0:
        v[i][j] = pas
        if i == ie and j == je:
            print(tabulate(v, tablefmt="fancy_grid"))
            sys.exit(0)
        else:
            for k in range(0,4):
                bk( i + dx[k], j + dy[k], pas + 1)
        v[i][j]=0

bk(iS,js,2)