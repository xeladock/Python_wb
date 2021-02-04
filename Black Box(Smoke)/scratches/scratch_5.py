# n = int(input())
# mat = [[n]*n for i in range(n)]
# mat[n-2][n-3]=n*n
# print(mat)

# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
#     print(a)

#arr[col_len-1][row_len]+arr[col_len+1][row_len]+arr[col_len][row_len-1]+arr[col_len][row_len+1]
col_len=0
row_len=1
md=""
arr=[]
a0,b0,an,bn=0,0,0,0
# формируем матрицу
while row_len>0: # бесконечный цикл
    md=input().split() # разбиваем строку на элементы для добавления в список
    if "end" in md:
        row_len-=1
        break # если в строке попалось END, закрываем список
    else:
        if row_len==1:
            col_len=len(md)
        row_len+=1 # счетчик
        arr.append(md) # добавляем элементы строки в двухмерный список
# формируем нулевую матрицу
arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]
# определяем в матрице элементы из суммы смежных
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i-1<0: a0=row_len-1
        else: a0=i-1
        if j-1<0: b0=col_len-1
        else: b0=j-1
        if i+1>row_len-1: an=0
        else: an=i+1
        if j+1>col_len-1: bn=0
        else: bn=j+1
        arr_sum[i][j]= int(arr[a0][j])+int(arr[an][j])+int(arr[i][b0])+int(arr[i][bn])
# выводим новую матрицу на экран
for row in arr_sum:
    for elem in row:
        print(elem, end=' ')
    print()