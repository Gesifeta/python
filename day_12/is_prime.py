def is_prime(num):
    is_prime=True
    value = num-1
    if num == 0 or num == 2:
        return True
    
    while value > 1: 
        
        if num % value == 0:
            is_prime =False
            break
        value -= 1
    return is_prime
