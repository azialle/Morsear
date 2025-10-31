from config.morse_caesar_config import morse_code_dict

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    morse_values_list = list(morse_code_dict.keys())

    for char in original_text:
        if char == ' ':
            encrypted_text += ' '
        elif char in morse_values_list:
            position = morse_values_list.index(char) + shift_amount
            position %= len(morse_values_list)
            encrypted_text += morse_values_list[position]
        else:
            encrypted_text += char

    morse_text = []
    for char in encrypted_text:
        morse_char = morse_code_dict.get(char, char)
        morse_text.append(morse_char)
    morse_result = " ".join(morse_text)

    return morse_result
