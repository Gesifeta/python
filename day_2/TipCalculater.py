print("Welcome to the tip calcuator \n")

bill_amount= float(input("Enter the total bill amount "))
tip_percentage= float(input("How much tip would you like to give ? 10, 15, 25 "))/100
number_of_persons=int(input("Enter the number of people to split the bill "))
# Calculate total bill
total_bill = bill_amount*(1 + tip_percentage)
bill_per_person = total_bill/number_of_persons

print(f"Each person should pay ${round(bill_per_person,2)}")