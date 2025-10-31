from config.morse_caesar_config import morse_code_dict
from config.morse_caesar_config import reverse_morse_dict


def decrypt(morse, shift_amount):
    decoded_text = decode_morse(morse)

    decrypted_text = ""
    morse_values_list = list(morse_code_dict.keys())

    for char in decoded_text:
        if char == ' ':
            decrypted_text += ' '
        elif char in morse_values_list:
            position = morse_values_list.index(char) - shift_amount
            position %= len(morse_values_list)
            decrypted_text += morse_values_list[position]
        else:
            decrypted_text += char

    return decrypted_text


def decode_morse(morse_message):
    words = morse_message.strip().split("/")

    decoded_text = []
    for word in words:
        letters = word.split()
        decoded_word = "".join(reverse_morse_dict.get(letter, letter) for letter in letters)
        decoded_text.append(decoded_word)
    return " ".join(decoded_text)