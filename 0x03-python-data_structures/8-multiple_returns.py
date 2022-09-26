#!/usr/bin/python3
def multiple_returns(sentence):
    res = len(sentence)
    char = sentence[0] if res > 0 else "None"
    new = res, char
    return(new)
