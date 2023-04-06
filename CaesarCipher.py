# coding = utf-8
# Author: Celine
# Date: 2023/4/5 23:05
import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
'''
# Solution1: create encrypt() and decrypt() function
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > (len(alphabet) - 1):
                new_position %= len(alphabet)
            shifted_char = alphabet[new_position]
            cipher_text += shifted_char
        else:
            cipher_text += char
    print(f"The decoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift_amount
            if abs(new_position) > (len(alphabet) - 1):
                new_position %= len(alphabet)
            shifted_char = alphabet[new_position]
            plain_text += shifted_char
        else:
            plain_text += char
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
'''


# Solution 1.1: Combine 3 functions into 1 function, called Caesar() with text, shift and direction
def Caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if abs(new_position) > (len(alphabet) - 1):
                new_position %= len(alphabet)
            shifted_char = alphabet[new_position]
            end_text += shifted_char
        else:
            end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")


is_continue = True
while is_continue:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    Caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if result == "no":
        is_continue = False
        print("Goodbye")

