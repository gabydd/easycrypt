"""Easily encrypt and decrypt text"""
import random


def chunked_string(letter_list: str) -> str:
    """Return a string made up of uppercase letters from a letter_list
    chunked into groups of 5
    
    >>> chunked_string([])
    """

    string = ""
    for i in range(len(letter_list)):
        if (i + 1) % 5 == 0:
            string += letter_list[i].upper() + " "
        else:
            string += letter_list[i].upper()
    return string


def get_int(prompt: str = None) -> int:
    """Return a user inputted integer"""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("invalid input")


def get_str(prompt: str = None) -> str:
    """As"""
    string = input(prompt)
    letters = ""
    for char in string:
        if "A" <= char.upper() <= "Z":
            letters += char.upper()
    return letters


def get_key() -> str:
    while True:
        key = get_str("A key is any string of letters (1-500 chars): ")
        if 0 < len(key) < 501:
            print("Using encryption key: {}\n".format(chunked_string(key)))
            return key
        print("invalid length")


def gen_key(length: int) -> str:
    """Genetate a length long list of letters"""
    key = ""
    for _ in range(length):
        key += chr(random.randrange(65, 91))
    return key


def main_menu():
    """Print the easycrypt menu and return a valid user inputted choice"""

    print(
        """Please choose from one of the following menu options:
1. Encrypt plaintext.
2. Decrypt ciphertext.
3. Generate key.
4. Exit."""
    )
    while True:
        choice = get_int("> ")
        if 0 < choice < 5:
            return choice
        print("Invalid choice. Try again.")


def encrypt_menu() -> tuple[str, str]:
    """"""
    plaintext = get_str("Please enter text to encrypt: ")
    print("This is the plaintext: {}\n".format(chunked_string(plaintext)))
    return plaintext, get_key()


def key_gen_menu() -> int:
    """Print the key generation menu and return a user inputted length"""

    print("Generate an encryption key comprised of random characters (max 500).")
    while True:
        length = get_int("Enter the desired length of key: ")
        if 0 < length < 501:
            return length
        print("invalid length")


def decrypt_menu() -> tuple[str, str]:
    ciphertext = get_str("Please enter text to decrypt: ")
    print("This is the ciphertext: {}\n".format(chunked_string(ciphertext)))
    return ciphertext, get_key()


def combine_letters(first, second, sign):
    char_total = ord(first) + sign*(ord(second) - 64)
    if char_total > 90:
        return chr(char_total - 26)
    if char_total < 65:
        return chr(char_total + 26)
    return chr(char_total)
    

def easycrypt(text: str, key: str, decrypt: bool = False) -> str:
    sign = 1
    if decrypt:
        sign = -1
    encrypted_message: str = ""

    for i in range(len(text)):
        encrypted_message += (combine_letters(text[i], key[i], sign))
    return encrypted_message


def fill_plaintext(plaintext: str):
    letters_needed = 5 - len(plaintext) % 5
    if letters_needed == 5:
        letters_needed = 0
    return plaintext + gen_key(letters_needed)


def fill_key(key: str, text: str):
    while len(key) < len(text):
        key += (key[-1])
    return key


def main():
    """Run's the whole easycrypt with nice menu's"""
    print(
        """----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------"""
    )

    while True:
        choice = main_menu()
        if choice == 1:
            print()
            plaintext, key = encrypt_menu()
            plaintext = fill_plaintext(plaintext)
            key = fill_key(key, plaintext)
            print("Your message has been encrypted:")
            print(chunked_string(easycrypt(plaintext, key)))
            print()

        elif choice == 2:
            print()
            cyphertext, key = decrypt_menu()
            fill_key(key, cyphertext)
            print("Your message has been decrypted:")
            print(chunked_string(easycrypt(cyphertext, key, True)))

        elif choice == 3:
            print()
            length = key_gen_menu()
            key_string = ""
            for letter in gen_key(length):
                key_string += letter
            print(key_string)
            print()

        elif choice == 4:
            break

    print("\nThank you for using EasyCrypt. Goodbye.")


if __name__ == "__main__":
    main()
