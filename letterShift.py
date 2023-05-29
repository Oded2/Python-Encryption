az_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
          'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def encrypt(message, shift):
    final_string = ''

    for letter in message:
        upper = str(letter).isupper()
        letter = str(letter).lower()
        if str(letter).isalpha():
            position = az_map[letter]
            shifted = position + shift
            if shifted > 26:
                shifted -= 26

            for a in az_map:
                if az_map[a] == shifted:
                    if upper:
                        final_string += str(a).upper()
                    else:
                        final_string += str(a)

        else:
            final_string += letter
    return final_string


def decrypt(message, shift):
    final_string = ''

    for letter in message:
        upper = str(letter).isupper()
        letter = str(letter).lower()
        if str(letter).isalpha():
            position = az_map[letter]

            shifted = position - shift
            if shifted < 1:
                shifted += 26

            for a in az_map:
                if az_map[a] == shifted:

                    if upper:
                        final_string += str(a).upper()
                    else:
                        final_string += str(a)

        else:
            final_string += letter
    return final_string
