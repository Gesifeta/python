PLACEHLOLDER ="[name]"

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    new_letter = letter.read()
    for name in names:
        striped_name = name.strip()
        a_letter= new_letter.replace(PLACEHLOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as my_letter:
            my_letter.write(a_letter)
            print(a_letter)