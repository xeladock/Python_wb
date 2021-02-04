a=list(map(int, input().split()))
b=a[0];c=a[1]
d=[i for i in range(b,c+1)]
for m in d:
    if m % 3==0 and m % 5==0:
        print('FizzBuzz')
    elif m % 3==0:
        print('Fizz')
    elif  m % 5==0:
        print('Buzz')
    else:
        print(m)
# print(d)
# for c in range()
