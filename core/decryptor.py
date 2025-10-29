from config.morse_caesar_config import full_charset
from config.morse_caesar_config import reverse_morse_dict


def decrypt(morse, shift_amount):
    decoded_text = decode_morse(morse)

    decrypted_text = ""
    for text in decoded_text:
        if text in full_charset:
            position = full_charset.index(text) - shift_amount
            position %= len(full_charset)
            decrypted_text += full_charset[position]
        else:
            decrypted_text += text

    return decrypted_text


def decode_morse(morse_message):
    words = morse_message.strip().split("/")

    decoded_text = []
    for word in words:
        letters = word.split()
        decoded_word = "".join(reverse_morse_dict.get(letter, "?") for letter in letters)
        decoded_text.append(decoded_word)
    return " ".join(decoded_text)