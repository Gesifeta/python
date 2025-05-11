print("Welcome to Python Pizza Deliveries!\n\n")
piza_size = input("What size pizza do you want? S, M or L: L ")
add_peperoni=input("Do you want peperon on your pizza (Y or N) " )
extra=input("Do you want extra cheese on you pizza? (Y or N) ")
price =0
if piza_size == "S" or piza_size  == "s":
    price = 15
    if add_peperoni == "Y" or add_peperoni ==  "y":
        price += 2
elif piza_size == "M" or piza_size == "m":
    price = 20
    if add_peperoni == "Y" or add_peperoni ==  "y":
        price += 3
elif piza_size == "L" or piza_size == "L":
    price = 5
    if add_peperoni == "Y" or  "y":
        price += 3
if extra == "Y" or extra ==  "y":
    price +=1
print(f"Your final bill is: {price}")