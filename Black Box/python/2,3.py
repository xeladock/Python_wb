# n=int(input())
# for i in range(n):
#     print('*'*n)

    # n = int(input())
    # for i in range(n):
    #     for j in range(n):
    #         print('*', end='')
    #     print()

a, b, c ,d =int(input()),int(input()),int(input()),int(input())
for j in range(c,d+1):
    print('\t',j, end='')
print()
for i in range(a,b+1):
    print(i,end='')
    for j in range(c, d + 1):
        s=j*i
        print('\t',s,end='')
    print()
        # print()
    #
    # print(i,'\t')
    # for j in range(c, d + 1):
    #         s = j * i
    #         print(i,'\t',s)
