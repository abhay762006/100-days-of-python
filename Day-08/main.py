from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(original_text, shift_amount,shift):
    temp =" "

    for letter in original_text:
        if letter not in alphabet:
            temp += letter

        else:

            shift_amount = shift + alphabet.index(letter)
            shift_amount = shift_amount % len(alphabet)
            temp +=  alphabet[shift_amount]
    print(f"Your encode is:{temp}")


def decrypt(original_text, shift_amount,shift):
    temp = ""
    for letter in original_text:
        shift_amount = alphabet.index(letter) - shift
        temp += alphabet[shift_amount]
    print(f"Your decode is:{temp}")


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift,shift=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift,shift=shift)
    else:
        print("Please type 'encode' or 'decode'")



while True:
    user = input("Welcome to Caesar Cipher, To run program text 'yes' otherwise text 'no'\n ").lower()
    if user == "yes":
        caesar()
    else:
        break
