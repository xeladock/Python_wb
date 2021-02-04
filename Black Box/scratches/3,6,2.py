import requests
# import re
c = open('/home/xela/py/1/4.txt','w')
r=requests.get('https://stepic.org/media/attachments/course67/3.6.2/316.txt')

# d=sys.argv[c]
# for line in open(d):
#     lines += 1

    # letters += len(line)
# r=str
#r=r.splitlines()
print(r.text, file=c)

# print(len(c.strip().splitlines( )))
# print(type(r))
# print(re.findall(r"[\n']+", open(c).read()))
print(len(open('/home/xela/py/1/4.txt').readlines()))

print(len(r.text.splitlines()))