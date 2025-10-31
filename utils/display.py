from colorama import Fore, init

art = """                                                 
 ▄    ▄  ▄▄▄▄  ▄▄▄▄▄   ▄▄▄▄  ▄▄▄▄▄▄   ▄▄   ▄▄▄▄▄ 
 ██  ██ ▄▀  ▀▄ █   ▀█ █▀   ▀ █        ██   █   ▀█
 █ ██ █ █    █ █▄▄▄▄▀ ▀█▄▄▄  █▄▄▄▄▄  █  █  █▄▄▄▄▀
 █ ▀▀ █ █    █ █   ▀▄     ▀█ █       █▄▄█  █   ▀▄
 █    █  █▄▄█  █    ▀ ▀▄▄▄█▀ █▄▄▄▄▄ █    █ █    ▀

"""


init(autoreset=True)

def print_encrypted(morse_result):
    print(f"{Fore.GREEN}Encrypted message: {Fore.YELLOW}{morse_result}")

def print_decrypted(decrypted_text):
    print(f"{Fore.CYAN}Decrypted message: {Fore.MAGENTA}{decrypted_text.lower()}")

def print_invalid():
    print(f"{Fore.RED}That's invalid! Try again.")

def print_exit():
    print(f"\n{Fore.YELLOW}Thank you for using MORSEAR. Stay encrypted! 🔐")
