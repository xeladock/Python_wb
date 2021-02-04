# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(c, d+1):
#     print('\t', i, end='')
# print()
# for j in range(a, b+1):
#     print(j, '\t', end='')
#     for g in range(c, d+1):
#         print('\t', g*j, end='')
#         # print()

# a, b, c ,d =int(input()),int(input()),int(input()),int(input())
# for j in range(c,d+1):
#     print('\t',j, end='')
# print()
# for i in range(a,b+1):
#     print(i,end='\t')
#     for j in range(c, d + 1):
#         s=j*i
#         print(s,end='\t')
#     print()

# a,b,n =int(input()),int(input()),0
# for j in range(a,b+1):
#     if j%3==0: n=n+1
# print(sum(j for j in range(a,b+1) if j%3==0)/n)

# x=[j for j in range((int(input()),int(input()) + 1)) if j%3==0]
# z=len(x) ;print(x/z)

# m = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
# print(sum(m)/len(x))
# text = 'Привет, как дела?'
# strr = 'как дела'
# ac=str.lower(input())
# k = 0
# tmp = []
#
# for i, t in enumerate(ac):
#     if t == ac[k]:
#         if k == len(ac) - 1:
#             tmp.append(ac[i - len(ac) + 1:i + 1])
#             k = 0
#         else:
#             k += 1
#     else:
#         k = 0
#
# print(tmp)

# s=input()
# b=str()
# s=s+'1'
# c=s[0]
# i=0
# for r in s:
#   if c!=r:
#     b+=c+str(i)
#     c=r
#     i=0
#   i+=1
# print(b)

# a, b, n = int(input()),int(input()),1
# while n==n:
#     if n%a==0 and n%b==0: break
#     else: n+=1
# print(n)

# a=[int(i) for i in input().split()]
# for i in a:
#     # i=int
#     print(a[i]+1)

# from functools import reduce
# l = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x*y, l))
# list = [10, 20, 30, 40, 50, 20]
# n = int(input("\nEnter a Number to search from the list : "))
# for m in list:
#     if n == m :
#         print(list.index(n))
# else :
#     print("\nMatch not found")

# A = ['red', 'green', 'blue']
# print(' '.join(A)) //red green blue
# print(''.join(A)) //redgreenblue
# print('***'.join(A)) //red***green***blue

k = (int(i) for i in input().split())
print(k)
