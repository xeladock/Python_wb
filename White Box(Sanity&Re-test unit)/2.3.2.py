a,b,n =int(input()),int(input()),0
for j in range(a,b+1):
    if j%3==0: n=n+1
print(sum(j for j in range(a,b+1) if j%3==0)/n)




