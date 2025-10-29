from config.morse_caesar_config import full_charset, morse_code_dict

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in full_charset:
            position = full_charset.index(char) + shift_amount
            position %= len(full_charset)
            encrypted_text += full_charset[position]
        else:
            encrypted_text += char

    morse_text = []
    for char in encrypted_text.upper():
        morse_char = morse_code_dict.get(char, char)
        morse_text.append(morse_char)
    morse_result = " ".join(morse_text)

    return morse_result
