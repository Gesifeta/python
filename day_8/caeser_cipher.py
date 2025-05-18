def caeser_cipher():
   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
   encrypted = ''
   decrypted = ''
   method = input("Type 'encode' to encrypt, and 'decode' to decrypt ")
   if method.lower() == 'encode':
      message = input("Enter the message to encode ")
      shift =  int(input("Type number of shifts "))
    #   loop thru the message and replace it with the next shifts from the letter
      for char in message:
         if char == ' ':
            encrypted += ' '
         else:
            encrypted += letters[letters.index(char) - (shift)]
      print("here is your encrypted = ", encrypted)
   elif method.lower() == 'decode':
      message = input("Enter the message to decode ")
      shift =  int(input("Type number of shifts "))
      for char in message:
          if char == ' ':
              decrypted += ' '
          elif char != ' ':
              if letters.index(char)+shift >len(letters)-1:
                  decrypted += letters[((letters.index(char) + shift) - (len(letters)-1))-1]
              else:
                  decrypted += letters[letters.index(char) + shift]
      print("Here is your decode message: ", decrypted)
   else:
      print("invalid input")
caeser_cipher()
      

      

      
   
