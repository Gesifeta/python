
def calculate_love_score(husband, wife):
    true = 0
    love = 0
    husband =input("Please enter your full name")
    wife =input("Please enter your spouse full name")
    words =  husband + wife
    #  count numbers for true
    for char in words.lower():
        if char == 't' or char == 'r'  or char == 'u' or char == 'e':
            true += 1
      #  count numbers for true
    for char in words.lower():
        if char == 'l' or char == 'o'  or char == 'v' or char == 'e' :
            love += 1
    print(str(true)+str(love))
calculate_love_score("angela yu", "jack bauer")