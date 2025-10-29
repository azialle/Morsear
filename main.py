from core.encryptor import encrypt
from core.decryptor import decrypt
from utils.display import print_invalid, print_exit, print_encrypted, print_decrypted

exit_program = False
while not exit_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()

    if direction == "encode":
        string_input = input("Type the message you want to encrypt with Morsear: ")
        shift_num = int(input("Type the shift number: "))
        encrypted_text = encrypt(string_input, shift_num)
        print_encrypted(encrypted_text)

    elif direction == "decode":
        morsear_input = input("Type your Morsear message to decrypt: ")
        shift_num = int(input("Type the shift number: "))
        decrypted_text = decrypt(morsear_input, shift_num)
        print_decrypted(decrypted_text)

    else:
        print_invalid()

    start_again = input("\nWould you like to try again? Type 'yes' to continue or 'no' to exit: ").lower()
    if start_again == "no":
        exit_program = True
        print_exit()
    elif start_again == "yes":
        exit_program = False
    else:
        print_invalid()
