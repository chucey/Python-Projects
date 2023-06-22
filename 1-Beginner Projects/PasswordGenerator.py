import string
import secrets

def contains_uppper(passwrd: str) -> bool:
    for char in passwrd:
        if char.isupper():
            return True
    return False

def contains_symbols(passwrd: str) -> bool:
    for char in passwrd:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combo_length: int = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combo_length)]

    return new_password

if __name__ == '__main__':
    for i in range(6):
        new_pass = generate_password(3, True, True)
        specs: str = f'U: {contains_uppper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} {specs}')