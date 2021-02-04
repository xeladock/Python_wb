# lst = [1, 2, 3, 4, 5, 6]
def modify_list(l):
    le = len(l)-1
    i = le
    while i!=-1:
        if l[i]%2:
            del l[i]
        else:
            l[i]=l[i]//2
        i -=1
    return
lst = [2, 12, 3, 14, 5, 6]
print(modify_list(lst))
# modify_list(l)# None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
#
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4
#

# def app(xs):
#     xs.append(1)
# a=[]
# app(a)
# print(a)
# old_list=[1,2,3]
# # old_list
# new_list = old_list.copy()
# print(new_list)
# You can slice it:

# new_list = old_list[:]