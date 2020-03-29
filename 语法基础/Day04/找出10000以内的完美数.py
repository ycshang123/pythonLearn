"""
找出1000以内的完美数
"""
for num in range(1,1000):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if num == sum:
            print(num)
print()