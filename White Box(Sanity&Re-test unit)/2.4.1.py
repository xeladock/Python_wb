a, ag, ac=str.lower(input()),0,0
for i in a:
    if i == 'c': ac=ac+1
    if i == 'g': ag=ag+1
print(((ag+ac)/len(a))*100)
