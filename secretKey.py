az_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
          'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}


def hash(string):
    final = 0
    for i in string:
        i = str(i)
        if i.isalpha():
            final += az_map[i.lower()] + 1
        elif i.isnumeric():
            final += int(i)
        else:
            final += 1
    return final


def shiftUp(letter, num):

    if letter.isalpha():
        isCap = letter.isupper()
        position = az_map[letter.lower()]

        for i in az_map:

            if az_map[i] == (position+num) % 26:
                if isCap:
                    return i.upper()
                else:
                    return i.lower()
    else:
        return letter
    return "Error"


def shiftDown(letter, num):

    if letter.isalpha():
        isCap = letter.isupper()
        position = az_map[letter.lower()]

        for i in az_map:

            if az_map[i] == (position-num) % 26:
                if isCap:
                    return i.upper()
                else:
                    return i.lower()
    else:
        return letter
    return "Error"


def encrypt(string, code):
    string = str(string)
    a = str(code)
    final = ''
    for i in range(len(string)):
        current_letter = string[i]
        current_index = i % len(a)
        current_num = int(a[current_index])
        final += shiftUp(current_letter, current_num)
    return final


def decrypt(string, code):
    string = str(string)
    a = str(code)
    final = ''
    for i in range(len(string)):
        current_letter = string[i]
        current_index = i % len(a)

        current_num = int(a[current_index])
        final += shiftDown(current_letter, current_num)
    return final


text = input("What's the text? ")
code = hash(input("What's your password? "))
print(f"Hash: {code}")
encrypted = encrypt(text, code)
print(f"Encrypted text: {encrypted}")
code = hash(input("What's the password? "))
print(f"Hash: {code}")
decrypted = decrypt(encrypted, code)
print(f"Decrypted text: {decrypted}")
