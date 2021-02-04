n=int(input())
sp= [[0 for j in range(n)] for i in range(n)]
dx, dy = 1, 0
x, y = 0, 0
for i in range(n):
    for j in range(n):
        # sp[n][n]==n
        print(sp[n][n])

# a=[i for i in range(5)]
# print(a)


# A = [ [1, 2, 3], [4, 5, 6] ]
# S = 0
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         S += A[i][j]
#         print(S)