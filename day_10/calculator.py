from art import logo

def add(first, next, is_inprogress):
    if is_inprogress:
        return next
    return first + next
def subtract(first, next, is_inprogress):
    if is_inprogress:
        return next
    return first - next
def multiply(first, next, is_inprogress):
    if is_inprogress:
        return next
    return first * next
def division(first, next, is_inprogress):
    if next == 0:
        return "Error: Division by zero"
    if is_inprogress:
        return next
    return first / next
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}

def calculate(task, first, next, is_inprogress):
    result = 0
    for key in operations:
         if task == key:
             result = operations[key](first, next, is_inprogress)
             return result
    return result
 
def main():
    continue_calcualtion = 'y'
    total = 0
    is_inprogress = False

    while continue_calcualtion != 'n':
       
        print(logo)
        print("\n")
        operand = input("Select your operation: ")
        first = 0
        next = 0
        if not is_inprogress:
            first = int(input("Enter your first number "))
        next =  int(input("Enter the next number "))
        if operand == "+":
             total += calculate(operand,first,next,is_inprogress)
        elif operand == "-":
             total -= calculate(operand,first,next,is_inprogress)
        elif operand == "*":
             total *= calculate(operand,first,next,is_inprogress)
        elif operand == "/":
             total /= calculate(operand,first,next,is_inprogress)
        else:
            print("Invalid input")
        continue_calcualtion = input("Would you like to continue (Y/N): ").lower()
        is_inprogress = True
    print(f"The result is = {total}")
    
main()
    