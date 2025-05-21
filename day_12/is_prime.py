def is_prime(num):
    counter = num
    if num == 0:
        return True
    if num == 2:
        return True
    while counter >1:
     
        if num % counter == 0:
            if num == counter:
                return True
            return False 
        counter -= 1
    return True
    
