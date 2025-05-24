from data import MENU
from data import resources
from data import report

# check if there exist enough resources for the request

def resources_available(order):
    if order.lower() != 'espresso':
        if MENU[order]['ingredients']['milk'] > resources['milk']:
            return print("“​Sorry there is not enough milk.")
    if MENU[order]['ingredients']['water'] > resources['water']:
        return print("“​Sorry there is not enough water.")
    if MENU[order]['ingredients']['coffee'] > resources['coffee']:
        return print("“​Sorry there is not enough coffee.")
    return True     
#  check the coins denominations and calculate total coins
def process_coins():
    print("\n"*70)
    print('1. pennies')
    print('2. nickles')
    print('3. dimes')
    print('4. quarters\n')
    coin = int(input("Enter the coin: "))
    total_coins = 0
   
    if coin == 4:
        total_coins += .25
    elif coin == 3:
        total_coins += .10
    elif coin == 2:
        total_coins += .05
    elif coin == 1:
        total_coins += .01      
    return total_coins

def main():
    continue_serving = True
    total_coins = 0.0
    while continue_serving != False:
        print("\n"*100)
        print("1. espresso")
        print("2. latte")
        print("3. cappuccino\n")
        print("4. report.")
        user_response = int(input("What would like to order? : "))
        if user_response == 1:
           if resources_available("espresso") == True:
               continue_inserting_coins = True
               while continue_inserting_coins != False:
                    total_coins +=  process_coins()
                    continue_inserting_coins = input("Continue inserting coins? (Y/N): ").lower()
                    if continue_inserting_coins == 'n':
                        continue_inserting_coins = False   
               if total_coins < MENU['espresso']['cost']:
                   print(f"You added only {total_coins}: Not sufficient to order {user_response}.")
               else:
                   report['money'] += total_coins 
                   report['coffee'] += MENU['espresso']['ingredients']['coffee']
                   report['water'] += MENU['espresso']['ingredients']['water']

                   resources['water'] -= MENU['espresso']['ingredients']['water']
                   resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                                 
        elif user_response == 2:
            if resources_available("latte") == True:
               
               continue_inserting_coins = True
               while continue_inserting_coins != False:
                    total_coins +=  process_coins()
                    continue_inserting_coins = input("Continue inserting coins? (Y/N): ").lower()
                    if continue_inserting_coins == 'n':
                        continue_inserting_coins = False  
               if total_coins < MENU['latte']['cost']:
                   print(f"You added only {total_coins}: Not sufficient to order {user_response}.")
               else:
                   report['money'] += total_coins 
                   report['coffee'] += MENU['latte']['ingredients']['coffee']
                   report['water'] += MENU['latte']['ingredients']['water']
                   report['milk'] += MENU['latte']['ingredients']['milk']
                   resources['water'] -= MENU['latte']['ingredients']['water']
                   resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                   resources['milk'] -= MENU['latte']['ingredients']['milk']
                    
        elif user_response == 3:
            if resources_available("cappuccino") == True:
               continue_inserting_coins = True
               while continue_inserting_coins != False:
                    total_coins +=  process_coins()
                    continue_inserting_coins = input("Continue inserting coins? (Y/N): ").lower()
                    if continue_inserting_coins == 'n':
                        continue_inserting_coins = False   
               if total_coins < MENU['cappuccino']['cost']:
                   print(f"You added only {total_coins}: Not sufficient to order.")
               else:
                   report['money'] += total_coins 
                   report['coffee'] += MENU['cappuccino']['ingredients']['coffee']
                   report['water'] += MENU['cappuccino']['ingredients']['water']
                   report['milk'] += MENU['cappuccino']['ingredients']['milk']
                   resources['water'] -= MENU['cappuccino']['ingredients']['water']
                   resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                   resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        elif user_response == 4:
            print(f"Water: {report['water']}ml")
            print(f"Milk: {report['milk']}ml")
            print(f"Coffee: {report['coffee']}g")
            print(f"Money: ${report['money']}ml")
        else:
            print("Invalid response.")
        continue_serving = input("Continue serving? (Y/N): ")
        if continue_serving.lower() == 'n':
            continue_serving = False
            print(f"You ordered {user_response}, and paid {total_coins}")
main()
    
