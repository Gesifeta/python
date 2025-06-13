def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
sum1 = add(1, 2, 3)
print(sum1)
sum2 = add(1, 2,5,6,7, 3)
print(sum2)
