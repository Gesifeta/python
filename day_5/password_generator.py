import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$*924

# get random letters

letter_combination=""
number_combination=""
symbol_comibination=""
for number in range(0,nr_letters):
    random_letters =random.randint(0,len(letters)-1)
    letter_combination += letters[random_letters]
for number in range(0,nr_numbers):
    random_letters =random.randint(0,len(numbers)-1)
    number_combination +=numbers[random_letters]
for number in range(0, nr_symbols):
    random_letters =random.randint(0,len(symbols)-1)
    symbol_comibination += symbols[random_letters]
print(f"Your password is : {letter_combination}+{symbol_comibination}+{number_combination}")