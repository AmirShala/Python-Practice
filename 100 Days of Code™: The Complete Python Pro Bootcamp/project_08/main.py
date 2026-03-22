"""
Caesar Cipher Program – Documentation
====================================

Overview
--------
This script implements a Caesar Cipher tool that can encode (encrypt) or decode (decrypt)
messages by shifting letters in the alphabet.

Features
--------
- Encode and decode functionality
- Handles large shift values using modulo
- Keeps non-alphabet characters unchanged
- Runs in a loop until the user exits

Function
--------
- caesar(original_text, shift_amount, encode_or_decode):
  Shifts each letter in the text based on the given shift.
  If "decode" is selected, the shift is reversed.

Program Flow
------------
1. Display logo from the art module
2. Ask user for:
   - encode/decode
   - message
   - shift number
3. Process input using the caesar function
4. Repeat until user chooses to exit

Example
-------
Input:
    encode
    hello
    2

Output:
    jgnnq

"""

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


