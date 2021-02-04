a=[
    [0, 5, 7],
    [2,4,3],
    [1,4,5]
]
# for i in a:
#     for j in i:
#         j+=10
#         print(j, end=' ')
#     print()
# with indexes
for i in range(3):
    for j in range(3):
        a[i][j]
        print(a[i][j],end=' ')
    print()
print(a)

for j in range(3):
    for i in range(3):
        a[i][j]
        print(a[i][j],end=' ')
    print()

for j in range(2,-1,-1):
    for i in range(2,-1,-1):
        a[i][j]
        print(a[i][j],end=' ')
print()
print(a)
for i in range(3):
    s=0
    for j in range(3):
        s+=a[i][j]
    print(s, end=' ')

  # [0, 5, 7],
  #   [2,4,3],
  #   [1,4,5]
