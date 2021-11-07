from functools import reduce
#1. lambda parameter_list : expression
max = lambda a, b: a if a >b else b
print(max(10,20))

#2. (lambda parameter: expression) (argument)
print((lambda a: a*a)(5))

# 3. filter(lambda parameter: expression, iterable)
# iterable = 數組
nums = [50, 2, 10 , 40]
print(type(nums), nums)
# 想要過濾出大於20 的資料
result = filter(lambda x: x > 20, nums)
print(list(result)) # 轉 list

# 4. map(lambda parameter: expression, iterable)
# map 轉換
scores = [50, 80 , 90, 30] # [False, True, True , False]
result = map(lambda x:  '真 ' if x >= 60 else '假', scores)
print(list(result))

# 4. reduce(lambda parameter: expression, iterable)
# map 轉換
scores = [50, 80 , 90, 30]
result = reduce(lambda x, y: x+y , scores)
print(result)

# 5. sorted(iterable, key=lambda parameter: expression)
scores = [50, 80 , 90, 30]
print(sorted(scores))
print(sorted(scores, reverse=True))

prices = [('2330.TW', 599), ('2317.TW', 108), ('3008.TW', 2080)]
print(sorted(prices, key=lambda aaa: aaa[1], reverse=True))