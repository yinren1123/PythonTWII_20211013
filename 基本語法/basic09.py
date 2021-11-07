import re
# Python 基本資料結構
# list   列表[]    (元素內容可以重複, 元素內容可以修改)
# tuple  列表()    (唯讀, Fast, 分析資料可以加快速度)
# set    列表[]      (元素內容不可重複, 元素內容可以修改)
# dict   字典列表{} (元素內容可以重複, 元素內容可以修改,等同java map)

# list 列表
scores1 = [100, 90]
scores2 = [80, 70]
scores3 = scores1 + scores2
scores1[1] = 95
scores1.append(70)
scores3 = scores1 + scores2
print(scores3)

#tuple
scores1 = (100, 90)
#scores1[1] = 95 # 不可修改
#scoures1. append(70) # 不可增加
print(scores1)

# list 與 tuple 互轉
scores = (100, 90)
scores = list(scores)
print(type(scores), scores)
scores = tuple(scores)
print(type(scores), scores)

# set 列表
empIds = [1, 3 , 5 , 2 ,3 ,1]
empIds = set(empIds)
print(type(empIds), empIds)
print(len(empIds))

# dict 字典列表(key: value)
# key的值不可以重複
# value 的值可以重複
a = {'symbol': '2330.TW', 'price': 599}
b = {'symbol': '2317.TW', 'price': 108}
c = {'symbol': '3008.TW', 'price': 2080}
prices = [a, b , c]
print(type(prices), prices)
for p in prices:
    print(p, p.get('symbol'), p.get('price'))

# 切割字串 split
# 股名,價格,殖利率,本益比,股價淨值比
s = "2330.TW,599,1.67,28.03,7.8"
s = s.split(",")
print(type(s), s, '本益比', s[3])
# 多符號切割(需要 import re)
s = "2330.TW,599#1.67!28.03,7.8"
s = re.split(',|#|!',s)
print(type(s), s, '本益比', s[3])

# split 轉 dict (字典格式 key=value)
s = "股名=2330.TW,價格=599,殖利率=1.67,本益比=28.03,股價淨值比=7.8"
s = dict( each.split("=") for each in s.split(","))
print(type(s), s, s.get('本益比'))

#本益比<12 殖利率大於5%

#股價淨值比 長期小於1 表示市場一直都不看好