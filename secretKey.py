az_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
          'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def hash(string):
    final = 0
    for i in string:
        final += az_map[i.lower()]

    return final


def shift(letter, num):
    isCap = letter.isupper()
    position = az_map[letter.lower()]
    position = isMax(position, 26)
    for i in az_map:
        if az_map[i] == position + num:
            if (isCap):
                return i.upper()
            else:
                return i.lower()

    return "Error"


def isMax(num, max_num):
    if (num < max_num):
        return num
    final = 1
    for i in range(num):
        final += 1
        if max_num < final:
            final = 0
    return final


def encrypt(string, code):
    string = str(string)
    a = str(code)
    final = ''
    for i in range(len(string)):
        current_letter = string[i]
        current_num = int(a[isMax(i, len(a))])
        final += shift(current_letter, current_num)
    return final


a = encrypt("abcdefghijklmnopqrstuvwxyz", 24)

print("Encrypted: " + a)
