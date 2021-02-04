a=' 1 5 14 2 85 87 ghb'
a= a.split()
m = map(int, (a))
l = list(a)
print(l)
# #//['1', '5', '14', '2', '85', '87', 'ghb']
a=' 1 5 14 2 85 87 1'
a= a.split()
map_object = map(int, a)
list_of_integers = list(map_object)
print(list_of_integers)
print(type(list_of_integers))
# [1, 5, 14, 2, 85, 87, 1]

a=' abc a bCd bC AbC BC BCD bcd ABC'
a= a.split()
b= map(str, a)
a = list(b)
print(a)
# ['abc', 'a', 'bCd', 'bC', 'AbC', 'BC', 'BCD', 'bcd', 'ABC']
import itertools
e=[1,2,3,5,6,78,98,6,54]
w=[]
# ee=[1,2,3,5,6,78,98,6,54]
eee=[[1,2],[3,5],[6,78],[98,6,54]]
tot = [e[i:i+1] for i in range(0, len(e), 2)]
for s in e:
    w.append(list(itertools.chain.from_iterable(s)))
n=[list(item[1]) for item in itertools.groupby(sorted(ee), key=lambda x: x[0])]
print(tot)
print(w)
e = [e[i:i+2] for i in range(0, len(e), 2)]
z=list(set([item for sublist in z for item in sublist]))
# объединение списка списков в один список

# [[1], [3], [6], [98], [54]]
# with open ('/home/xela/py/1', 'w') as a:
#     a.write('hello\n')
#     a.write(str(25))
# .join(str(ss) for ss in fq)

# a=[['Зенит', '1'], ['Локомотив', '1'], ['Локомотив', '1']]
# for m in set(a): print(a)


# aa = [['a',3],['a',4],['c','5']]
# bb={x[0]:x[1] for x in aa}
# print(bb)

# myList = [[8100, 3], [8200, 5], [8400, 9]]
# new_list = []
# new_list2 = []
# for item in myList:
#     new_list.append(item[0])
#     new_list2.append(item[1])
# print (sum(new_list)/3)
# print (sum(new_list2)/3)


# m=[a]
# c =  [ int(x) for x in m.split(" ") ]
# print(c)
# g=[]
# d={}
# for m in range(0,len(a)-1):
#     if a[m] != ' ': g.append(a[m])
#     else:
#         continue
# print(g)
# for b in a:
#    g.append(b)
# print(g)
# b=type(int(a))
# print(b)
# for s,x in enumerate(a):
#     # if x==' ': continue
#     # else:
#         print(s,x)

# list_of_integers = list(map_object)
# list_of_integers = list(a)

# dict = {}
# dict['a'] = 'alpha'
# dict['g'] = 'gamma'
# dict['o'] = 'omega'
#
# print
# dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
#
# print
# dict['a']  ## Simple lookup, returns 'alpha'
# dict['a'] = 6  ## Put new key/value into dict
# 'a' in dict  ## True
# ## print dict['z']                  ## Throws KeyError
# if 'z' in dict: print
# dict['z']  ## Avoid KeyError
# print (dict.get('z'))  ## None (instead of KeyError)
#
# with open ('/home/xela/py/some7.txt', 'r') as a: a=a.read().lower().split()
# b={}
# for m in set(a): b.setdefault(m,[]).append(a.count(m))
# # c=max(b,key=b.get); x=(list(b.values()))
# print(max(b,key=b.get), *max(list(b.values())))