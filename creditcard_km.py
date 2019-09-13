#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    05 Apr 2019

    This is a modular Python script that checks the validity of a credit card number.
    It checks length and rejects bad input and non-digit strings.
    It uses the Luhn algorithm to check credit card validity, and will tell
    you what type of credit card it is when given a proper number.
    If the user enters the wrong format, it will trap them in a loop to ensure
    they enter a value that can be checked against the Luhn algorithm to see
    if it is valid.

"""
def int_input():
    good_input = False
    while good_input == False:
        good_value = input()
        try:
            val = int(good_value)
            good_input = True
        except ValueError:
            print("Error: characters entered. Please enter whole numbers.")
    return good_value

def get_number():
    cc = ""
    while len(cc) < 13 or len(cc) > 16:
        print("Please enter a valid credit card number, 13-16 digits.")
        print("The number must begin with 4, 5, 6, or 37.")
        cc = int_input()
        is_valid = valid_length(cc)
        if is_valid == False:
            cc = ""
    return cc

def valid_length(cc):
    is_valid = False
    if len(cc) < 13 or len(cc) > 16:
       is_valid = False 
    if cc[0] == "4":
        is_valid = True
    if cc[0] == "5":
        is_valid = True
    if cc[0] == "6":
        is_valid = True
    if cc[0] == "3" and cc[1] == "7":
        is_valid = True
    return is_valid

def check_luhn(cc):
    second_num = len(cc) % 2
    cc_sum = 0
    counter = enumerate([int(i) for i in cc])
    for i, num in counter:
        if i % 2 == second_num:
            num *= 2
            if num > 9:
                num -= 9
        cc_sum += num
    return cc_sum % 10 == 0

def main():
    cc = get_number()
    card_type = "unknown"
    if cc[0] == "4":
        card_type = "Visa"
    if cc[0] == "5":
        card_type = "MasterCard"
    if cc[0] == "6":
        card_type = "Discover"
    if cc[0] == "3" and cc[1] == "7":
        card_type = "American Express"
    is_valid = check_luhn(cc)
    if is_valid == True:
        print("This is a valid " + card_type + " credit card number.")
    else:
        print("This is not a valid credit card number.")

main()
