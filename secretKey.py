

# az_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
#           'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
az_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
          'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}


def hash(string):
    final = 0
    for i in string:
        final += az_map[i.lower()]

    return final


def shiftUp(letter, num):
    isCap = letter.isupper()
    position = az_map[letter.lower()]

    for i in az_map:

        if az_map[i] == isMax(position + num, 26):
            if (isCap):
                return i.upper()
            else:
                return i.lower()

    return "Error"


def shiftDown(letter, num):

    isCap = letter.isupper()
    position = az_map[letter.lower()]

    for i in az_map:

        if az_map[i] == isMin(position-num, 26):
            if (isCap):
                return i.upper()
            else:
                return i.lower()

    return "Error"


def isMax(num, max_num):

    final = 0
    for i in range(num):
        final += 1
        if final >= max_num:
            final = 0
    return final


def isMin(num, max_num):

    final = 0
    if (num > 0):
        for i in range(num):
            final += 1
            if final >= max_num:
                final = 0
        return final
    else:
        final = max_num
        for i in range(max_num):
            final -= 1
            if (final == 0):
                final = max_num

        return final


def encrypt(string, code):
    string = str(string)
    a = str(code)
    final = ''
    for i in range(len(string)):
        current_letter = string[i]
        current_index = isMax(i, len(a))

        current_num = int(a[current_index])
        final += shiftUp(current_letter, current_num)
    return final


def decrypt(string, code):
    string = str(string)
    a = str(code)
    final = ''
    for i in range(len(string)):
        current_letter = string[i]
        current_index = isMax(i, len(a))

        current_num = int(a[current_index])
        final += shiftDown(current_letter, current_num)
    return final


a = encrypt("abcdefghijklmnopqrstuvwxyz", 1)
print(f"a: {a}")
b = decrypt(a, 1)
print(f"b: {b}")
