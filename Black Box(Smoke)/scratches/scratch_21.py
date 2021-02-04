# x=[['0', '1'], ['2', '3'], ['4', '5'], ['6', '7'], ['8', '9']]
# z=[]
# zz=[]
# print(len(x))
# for m in x:
#     if '0' in m:
#         z.append(m[1])
#     if '4' in m:
#         zz.append(m[1])
#     # for mm in m:
#         # z=[::1]
#     # m=str(m)
#     else:
#         continue
# print(zz)
# print(z)
    #     print(m[1])

# kk = ['1','100','100','100']
# kk = list(map(int, kk))
# print(len(kk))
# print(len(kk)-1)
# kk=sum(kk[1:])/(len(kk)-1)
# # print(m)
# # kk = list(kk)
# print(kk)

# nested_list = [['1', '128', '1', '128', '1', '130'], ['10', '167', '10', '169', '10', '170', '10', '170', '10', '171'], ['11', '177', '11', '179', '11', '180'], ['2', '127', '2', '128', '2', '129', '2', '130', '2', '131'], ['3', '131', '3', '131', '3', '131', '3', '136', '3', '137'], ['4', '138', '4', '141', '4', '141', '4', '142', '4', '142'], ['5', '149'], ['6', '155', '6', '158', '6', '158', '6', '160'], ['7', '156', '7', '158', '7', '158', '7', '160', '7', '160', '7', '163'], ['8', '163', '8', '166', '8', '167'], ['9', '165', '9', '165', '9', '167', '9', '170', '9', '173']]
# # sorted_list = list(map(int, nested_list))
# sorted_list = sorted(nested_list, key=lambda x: x[0])
# #
# print(sorted_list)

# a=''1' 5 14 2 85 87 1'
# a= a.split()
# map_object = map(int, a)
# list_of_integers = list(map_object)
# print(list_of_integers)
#
# a=[1,2,3]
# print(sum(a))
# a=[1, 62.916666666666664, 10, 90.25, 11, 101.0, 2, 73.0, 3, 78.57142857142857, 4, 76.29411764705883, 5, 79.06666666666666, 6, 85.61538461538461, 7, 84.66666666666667, 8, 90.57142857142857, 9, 90.0]
# a=[a[i:i+2] for i in range(0, len(a),2)]
# print(a)

# a=[[1], [10, 169.4], [11, 178.66666666666666], [2, 129.0], [3, 133.2], [4, 140.8], [5, 149.0], [6, 157.75], [7, 159.16666666666666], [8, 165.33333333333334], [9, 168.0]]
#
# for m in a:
#     if len(m)==1:
#         print(*m, '-')
#     else: print(*m)

# with open ('/home/xela/py/77.txt', 'r') as a: a=a.read().lower().split(); ff = open('/home/xela/py/777.txt','w')
# # a= [a for x in a]
# # a.extend(a)
# print(a)

# o= open ('/home/xela/py/77.txt', 'r');ff = open('/home/xela/py/777.txt','w')
# b=[]
# for s in o:
#     b.append(o.readline().split())
# print(b)

# with open('input.txt', 'r', encoding='utf-8') as f:

with open ('/home/xela/py/77.txt', 'r') as a:
    for line in a:
        line=line.strip()
        print(line)