#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    16 Feb 2019

    Letter frequency: a tiny "Pythonic" program that iterates over an alphabet,
    and prints the amount of times the alphabet characters appear in the string.
    This is a very input safe program that will reject all whitespace
    and non-char input. Uses isalpha() to bounce improper input.
"""
def string_input():
    good_value = ''
    while (good_value.isalpha() == False):
        print("Please enter a string, letters A-Z only.")
        print("Numbers, special characters and spaces will be rejected.")
        good_value = input()
    return good_value.lower()
string = string_input()
alphabet = [
           'a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z'
           ]
for i in range (len(alphabet)):
    print(alphabet[i], ': ', string.count(alphabet[i]), sep='')
