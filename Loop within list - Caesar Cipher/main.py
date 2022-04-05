from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# write a function to run caesar cipher encryption
def caesar(input_text, shift, cipher_direction):
    output_text = ""

    # shift right for encode, shift left for decode
    if cipher_direction == "decode":
        shift *= -1
    
    # handle symbols/numbers/spaces other than alphabet
    for char in input_text:
        if char not in alphabet:
            output_text += char
        else:
            pos = alphabet.index(char)
            pos += shift
            pos = pos % len(alphabet) # loop within list to handle index error
            output_text += alphabet[pos]
    
    print(f"Here's the {cipher_direction}d result: {output_text}")


# print welcome logo
print(logo)

# program continues to run until otherwise
restart = "yes"
while restart == "yes":
    
    # enforce correct direction input
    direction = ""
    while (direction != "encode") and (direction != "decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(input_text=text, shift=shift, cipher_direction=direction)
    restart = input("Do you want to restart the cipher program? 'Yes' or 'No'.\n").lower()

print("Your message has been encrypted and destroyed. Goodbye.")