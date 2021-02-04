def f(x):
    if x<=-2:
        print(1-((x+2)**2))
        return ''
    elif -2<x<=2:
        print(-x/2)
        return ''
    elif 2<x:
        print(1+((x-2)**2))
        return''
