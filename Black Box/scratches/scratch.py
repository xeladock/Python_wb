# col_len=5
# row_len=7
# arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]
# print(arr_sum, end='\n')
# s=['hello']
# s+='privet'
# # s=s+i
# print(s)

# students = [['Ivan', 'Masha', 'Sasha'],['Olga']]
# # students += ['Olga']
# # students += 'Olga'
# print(zip(*students)[0])
# ['Ivan', 'Masha', 'Sasha', 'Olga', 'O', 'l', 'g', 'a']
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(n, end='')
#     print()
#
# while n!='end':
#     a=int
# (int(i) for i in input().split())

# a = [int(i) for i in input(). split()]
# print(a)

# lst = 'ghbdtn'
# lst+='0'
# print((lst))


# a=input().split()
# for i in list(set(a)):
#     # a.sort(i)
#     if a.count(i) == 1: a.remove(i)
#     print (i, end=' ')

# # s=list(set(a))
# for g in list(set(a)):
#     print(g, end=' ')


#arr[col_len-1][row_len]+arr[col_len+1][row_len]+arr[col_len][row_len-1]+arr[col_len][row_len+1]
# col_len=0
# row_len=1
# md=""
# arr=[]
# a0,b0,an,bn=0,0,0,0
# # формируем матрицу
# while row_len>0: # бесконечный цикл
#     md=input().split() # разбиваем строку на элементы для добавления в список
#     if "end" in md:
#         row_len-=1
#         break # если в строке попалось END, закрываем список
#     else:
#         if row_len==1:
#             col_len=len(md)
#         row_len+=1 # счетчик
#         arr.append(md) # добавляем элементы строки в двухмерный список
# # формируем нулевую матрицу
# arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]
# # определяем в матрице элементы из суммы смежных
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i-1<0: a0=row_len-1
#         else: a0=i-1
#         if j-1<0: b0=col_len-1
#         else: b0=j-1
#         if i+1>row_len-1: an=0
#         else: an=i+1
#         if j+1>col_len-1: bn=0
#         else: bn=j+1
#         arr_sum[i][j]= int(arr[a0][j])+int(arr[an][j])+int(arr[i][b0])+int(arr[i][bn])
# # выводим новую матрицу на экран
# for row in arr_sum:
#     for elem in row:
#         print(elem, end=' ')
#     print()
z,x=3,10
arr_sum = [[0 for j in range(z)] for i in range(x)]
print(arr_sum)

for i in range(len(arr_sum)):
    for j in range(len(arr_sum[i])):
            print (sum(arr_sum[j][i],end=' '))