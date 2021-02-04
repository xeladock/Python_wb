import requests
# m=''
# c = open('/home/xela/py/1/4.txt','w')
url1='https://stepic.org/media/attachments/course67/3.6.3/'
# url='https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
par=r.text
# r=requests.get(url1,params=par)
# print(par)
# print(type(url1))
# m = url1 + par
# print(m)
# r = requests.get(m)
# par=r.text
# print(par)
# m=url1+par
# print((m))
# print(r.url)
while 'We' not in par:
    m = url1 + par
    r = requests.get(m)
    par=r.text
    print(par)
# for s in r.text:
#     if 'We' not in r.text:
#         requests.get(str(url)+'s')
#         print(s)
#     else:
#         print(s)

# for s in r:
#     if 'We' in no
