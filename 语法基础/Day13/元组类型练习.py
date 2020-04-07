"""
元组类型练习
"""
#定义元组
t = ('尚宇驰',19,True,'江苏徐州')
print(t)
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
#t[0]="王大锤"
#变量重新引用了新的元组，原来的元组将被回收
t = ("王大锤",20,True,'云南昆明')
print(t)
#将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '王二锤'
person[1] = 19
#将列表转换成元组
fruits_list = ['apple','banana','orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)