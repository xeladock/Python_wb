a,b,c = int(input()),int(input()),int(input())
if ((a>=c and a>=b) and (b<=a and b<=c)):
    print(a,b,c,sep = '\n')
elif ((a>=c and a>=b) and (c<=a and c<=b)):
    print(a,c,b,sep = '\n')
elif ((b>=c and b>=a) and (a<=b and a>=c)):
    print(b,c,a,sep = '\n')
elif ((b>=c and b>=a) and (c<=b and c>=a)):
    print(b,a,c,sep = '\n')
elif ((c>=a and c>=b) and (b>=a and b<=c)):
    print(c,a,b,sep = '\n')
elif ((c>=a and c>=b) and (a>=b and a<=c)):
    print(c,b,a,sep = '\n')
