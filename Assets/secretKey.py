az_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
          'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

charMap = {'!': 0, '@': 1, '#': 2, '$': 3, '%': 4,
           '^': 5, '&': 6, '*': 7, '(': 8, ')': 9, ' ': 10, '.': 11, ',': 12, '[': 13, ']': 14, '|': 15, '/': 16, '\\': 17, '-': 18,
           '+': 19, '=': 20, '_': 21, '`': 22, '~': 23, '?': 24, '<': 25, '>': 26, '{': 27, '}': 28,
           "'": 29, '"': 30, ';': 31, ':': 32}


def hash(string):
    final = 0
    for i in string:
        multiplier = 1
        i = str(i)
        if i.isalpha():
            if i.isupper():
                multiplier = 2

            final += (az_map[i.lower()] + 1)*multiplier

        elif i.isnumeric():
            final += int(i)
        elif i in charMap:
            final += charMap[i]
        else:
            final += 1
    return final


def shiftUp(letter, num):

    if letter.lower() in az_map:
        isCap = letter.isupper()
        position = az_map[letter.lower()]

        for i in az_map:

            if az_map[i] == (position+num) % 26:
                if isCap:
                    return i.upper()
                else:
                    return i.lower()
    elif letter in charMap:
        position = charMap[letter]
        length = len(charMap)
        for i in charMap:
            if charMap[i] == (position + num) % length:
                return i
    else:
        return letter
    return "Error"


def shiftDown(letter, num):

    if letter.lower() in az_map:
        isCap = letter.isupper()
        position = az_map[letter.lower()]

        for i in az_map:

            if az_map[i] == (position-num) % 26:
                if isCap:
                    return i.upper()
                else:
                    return i.lower()
    elif letter in charMap:
        position = charMap[letter]
        length = len(charMap)
        for i in charMap:
            if charMap[i] == (position - num) % length:
                return i
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
