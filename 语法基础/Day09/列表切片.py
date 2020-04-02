"""
列表切片
"""

fruits =['grape','apple','strawberry','waxberry']
fruits =['pitaya','pear','mango']
#列表切片
fruits2 = fruits[1:4]
#['apple','strawberry','waxberry']
print(fruits2)
# ['pear', 'mango']
# 可以通过完整的切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)
# ['pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)
# ['pitaya', 'pear']
fruits5 = fruits[::-1]
print(fruits5)
# ['mango', 'pear', 'pitaya']
