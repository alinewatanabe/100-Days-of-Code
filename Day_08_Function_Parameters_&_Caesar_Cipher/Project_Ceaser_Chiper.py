import os
import time

def ceaser(direction, text, shift):
    txt = ""
    for letter in text:
        position = alphabet.index(letter)
        if(direction == "encode"):
            new_position = position + shift
            Error = False
        elif(direction == "decode"):
            new_position = position - shift
            Error = False
        else:
            print("Error. Try Again")
            time.sleep(2)
            os.system("cls")
            Error = True
        new_letter = alphabet[new_position]
        txt += new_letter
    print(f"The {direction}d text is {txt}")
    return Error

        
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Error = True

while(Error == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    
    Error = ceaser(direction = direction, text = text, shift = shift)