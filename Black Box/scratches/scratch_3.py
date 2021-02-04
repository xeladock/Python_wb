# def update_dictionary(d, key, value):
#     # put your python code here
#     if key in d:
#         d[key].append(value)
#         #print('ключ есть')
#     elif key is not d:
#         #d[2*key]=[]
#         if 2*key is d:
#             d[2*key].append(value)
#             #print('ключ 2*key уже есть')
#         elif (2*key is not d) and d.get(2*key)==None:
#             d[2*key]=[]
#             d[2*key].append(value)
#             #print('создание ключа и + новое значение списка')
#         elif (2*key is not d) and d.get(2*key)!=None:
#             d[2*key].append(value)
#             #print('создание ключа и + значение списка')
#     return
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

# d ={0:1,1:2,2:3,3:4,4:5,5:5}
# if key in d:
#     d[key].append(value)
# x=int(input())
# def f(x):
#      ((x-1))
# print(f(x))

# Creating an empty dictionary
myDict = {}
lst=[1,2,3,4,5]
n=6
m=7
lst2=[n,m]
lst.append(lst2)
# Adding list as value
# myDict["key1"] = [1, 2]
myDict[2] = [lst, 6]
# myDict["key1"].append(lst)

print(myDict)