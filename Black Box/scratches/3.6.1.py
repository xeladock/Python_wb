import requests
c = open('/home/xela/py/4.txt','w')
r=requests.get('https://stepic.org/media/attachments/course67/3.6.2/349.txt')
print(r.text, file=c)
print(len(open('/home/xela/py/4.txt').readlines()))