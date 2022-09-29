#!/usr/bin/python3
def roman_to_int(roman_string):
    # Fail checks, none, not a string
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    # Dictionary for roman numerals
    r_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    int_value_of_roman_string = 0
    legizew = list(roman_string)
    # Concat 4 and 9s
    if len(legizew) > 1:
        idx = 0
        for i in legizew:
            try:
                if legizew[idx] == 'I' and legizew[idx + 1] == 'V':
                   legizew[idx:idx + 2] = [''.join(legizew[idx:idx + 2])]
            except IndexError:
                pass
            try:
                if legizew[idx] == 'I' and legizew[idx + 1] == 'X':
                    legizew[idx:idx + 2] = [''.join(legizew[idx:idx + 2])]
            except IndexError:
                pass
            idx += 1
    # Search in dict for correct numbers and add
    for k, v in r_dict.items():
        for index in legizew:
            if index == k:
                int_value_of_roman_string += v
    return int_value_of_roman_string
