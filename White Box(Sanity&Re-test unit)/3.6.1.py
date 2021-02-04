import requests
c = open(4.txt','w')
r=requests.get('https://stepic.org/media/attachments/course67/3.6.2/316.txt')
print(r.text, file=c)
print(len(open('4.txt').readlines()))
