import requests
url1='https://stepic.org/media/attachments/course67/3.6.3/'
r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt'); par=r.text
while 'We' not in par:
    m = url1+par; r = requests.get(m)
    par=r.text
print(par)
