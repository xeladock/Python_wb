# c=3
# w=[['Зенит', '0n', 'Зенит', '0n', 'Зенит', '0pr', 'Зенит', '0w', 'Зенит', '3', 'Зенит', '3l'], ['Локомотив', '0n', 'Локомотив', '0n', 'Локомотив', '0pr', 'Локомотив', '0pr', 'Локомотив', '3', 'Локомотив', '3'], ['Спартак', '0n', 'Спартак', '0n', 'Спартак', '0w', 'Спартак', '0w', 'Спартак', '3l', 'Спартак', '3l']]
# for ww in w:
#     ww.insert(1, str(c - 1))
#     s = ww[0]
#     ww.insert(0, s+str(':'))
#     # for gg in range(0,len(ww)):
#     for www in ww[:]:
#
#         if s == www:
#             ww.remove(www)
#     print(*ww)

# w=['2', '03', '0n', '0n', '0pr', '0w', '3l']
# for m in w:
#     if m.count('0w') == 1 :
#         w.remove(m)
#         if m.count('0pr') == 1 :
#             w.remove(m)
#     # if w.count(0pr) > 1:
#     #     w.remove(m)
# print(w)
def checkio(data):
    for index in range(len(data) - 1, -1, -1):
        if data.count(data['0pr']) == 1:
            del data[index]
    return data

w=['2', '03', '0n', '0n', '0pr', '0w', '3l']
for m in w:
    print(checkio(m))