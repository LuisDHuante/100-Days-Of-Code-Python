import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = '''
                                                    _               
                                                   | |              
   ___ __ _  ___  ___  __ _ _ __    ___ _   _ _ __ | |__   ___ _ __ 
  / __/ _` |/ _ \/ __|/ _` | '__|  / __| | | | '_ \| '_ \ / _ \ '__|
 | (_| (_| |  __/\__ \ (_| | |    | (__| |_| | |_) | | | |  __/ |   
  \___\__,_|\___||___/\__,_|_|     \___|\__, | .__/|_| |_|\___|_|   
                                         __/ | |                    
                                        |___/|_|                   
'''


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")



should_end = False
while not should_end:
    os.system ("cls")
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    os.system ("cls")
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    os.system ("cls")
    if restart == "no":
        should_end = True
        os.system ("cls")
        print("Thanks for using the Caesar Cypher")
