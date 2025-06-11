# list comprehension

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_list = [num ** 2 for num in numbers]
ranges = [item * 2 for item in range(0,5)]
print(new_list)
print(ranges)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [short for short in names if len(short) <= 4]
print(short_names)
upper_names = [short.upper() for short in names if len(short) > 4]
print(upper_names)