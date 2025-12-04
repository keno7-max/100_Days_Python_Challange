from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
print(logo)

def caesar(encode_or_decode, orginal_text, shift_amount):
    caesar_text = ""
    for char in orginal_text:
    
        if char not in alphabet :
            caesar_text += char 
        else :
            old_index = alphabet.index(char)

            if encode_or_decode == 'encode':
                new_index = old_index + (shift_amount % 26)
            elif encode_or_decode == 'decode':
                new_index = old_index - (shift_amount % 26)

            caesar_text += alphabet[(new_index % 26)]

    print(f"Here's the {encode_or_decode}d result: {caesar_text}")


go_again = False       
while not go_again : 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 

    caesar(direction, text, shift) 
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    if again == 'yes' :
       go_again = False
    else :
        go_again = True
        print("Goodbye!")

