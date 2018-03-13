# _*_coding: utf-8 _*_

def normalize(name):
#    return name.capitalize() # 把第一个字母转大写，其余小写
    return name[:1].upper() + name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
