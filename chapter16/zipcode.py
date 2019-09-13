#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    05 May 2019

    Python zip code validator. Prints information for zip codes that a user
    has input. Reads a csv file.

"""
import csv
def int_input():
    good_input = False
    while good_input == False:
        good_value = input()
        try:
            val = int(good_value)
            good_input = True
        except ValueError:
            print("Error: characters entered. Please enter whole numbers.")
    return int(good_value)

def read_csv(filename, index):
    with open(filename) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)
        # find index here, use enumerate
        csvlist = []
        for row in reader:
            csvdata = row[index]
            csvlist.append(csvdata)
    return csvlist

def get_zip():
    zip = []
    quit = False
    while quit == False:
        print("Please enter a zip code. Enter 0 to finish.")
        new_zip = int_input()
        zip.append(str(new_zip).zfill(5))
        if new_zip == 0:
            zip.pop()
            quit = True
    print(zip)
    return zip

def check_zip(zip_input, zip_master):
    index = -1
    for i in range(len(zip_master)):
        if zip_input == zip_master[i]:
            index = i
    return index

def main():
    zip_input = get_zip()
    zips = read_csv('zip_codes_states.csv', 0)
    cities = read_csv('zip_codes_states.csv', 3)
    states = read_csv('zip_codes_states.csv', 4)
    counties = read_csv('zip_codes_states.csv', 5)
    print()
    for i in range(len(zip_input)):
        index = check_zip(zip_input[i], zips)
        if index != -1:
            print("Zip code: " + zip_input[i])
            print("City:     " + cities[index])
            print("State:    " + states[index])
            print("County:   " + counties[index])
        else:
            print("Zip code " + zip_input[i] +" not found in master list.")
        print()

main()
