# bai 1
def ma_hoa_list(l):
    new_l = {}
    for index, item in enumerate(l, 0):
        if new_l.get(item) == None:
            new_l.update({item: index})
    for i in range(len(l)):
        l[i] = new_l.get(l[i])
    return l

print('List ma hoa: ',ma_hoa_list(l=['xanh', 'do', 'cam', 'vang', 'xanh', 'do']))

# Bai 2
import math
# input: {'1': 1, '2': 5, '3': 9}
# out: Max: {'3': 9}
def gtln (dic):
    max = -math.inf # tru vo cung
    maxKey = ''
    for i in dic:
        if max < dic[i]:
            maxKey = i
            max = dic[i]
    print(f"Max: ({maxKey} : {max})")
gtln({'1': -1, '2': 5, '3': 9})