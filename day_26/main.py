# list comprehension
import  random

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

# Filtering Even Numbers

# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
#
#
#
# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.
#
# Then use list comprehension again to create a new list called result.
#
# This new list should only contain the even numbers from the list numbers.
#
# Again, try to use Python's List Comprehension instead of a Loop.

# Data Overlap
# 💪 This exercise is HARD 💪
#
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
#
# 2
#
# 3
#
# and file2.txt contained:
#
# 2
#
# 3
#
# 4
#
# result = [2, 3]
#
#
#
# IMPORTANT:  The output should be a list of integers and not strings!
#
# Try to use List Comprehension instead of a Loop.

students ={student:random.randint(35,101) for student in names}
passed_student ={ student:students[student] for student in students if students[student]>=65 }
print(students)
print(passed_student)