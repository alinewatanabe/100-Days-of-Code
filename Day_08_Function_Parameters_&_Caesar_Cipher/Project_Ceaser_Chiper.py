import os
import time

def encrypt(plain_text, shift_amount):
    cipher_txt = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_txt += new_letter
    print(f"The encode text is {cipher_txt}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Error = True

while(Error == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    
    if(direction == "encode"):
        encrypt(plain_text = text, shift_amount = shift)
        Error = False
    elif(direction == "decode"):
        decrypt(cipher_text = text, shift_amount = shift)
        Error = False
    else:
        print("Error. There isn't the option selected.\nTry Again!")
        time.sleep(2)
        os.system("cls")
        Error = True