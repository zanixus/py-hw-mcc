#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    19 April 2019

    This is a file I/O demo for Python. It generates a list of 52 lists. Each of the
    52 lists contains 7 int values for temperature. These values are written to a file.
    Each line of the file are comma-seperated values of list elements, 52 lines total.

    The file is then read back into a list and data processing is done to determine
    which day of the week had the hottest(highest) temperature.


"""
import random

def weeks():
    week = []
    for i in range(7):
        week.append(random.randint(70, 100))
    return week

def years():
    year = []
    for i in range(52):
        year.append(weeks())
    return year

def write_file(filename, list_data):
    with open(filename, 'w') as file_object:
        for i in range(len(list_data)):
            data_to_write = str(list_data[i])[1:-1]
            file_object.write(data_to_write + "\n")

def read_file_to_int_list(filename):
    new_list = []
    with open(filename) as file_object:
        for line in file_object:
            append_line = line.split(", ")
            append_line[6] = (append_line[6].rstrip())
            append_line = list(map(int, append_line))
            new_list.append(append_line) #magic numbers and data type conversion?
    return new_list                      #not very Pythonic. oh well

def calc_hottest(year_data):
    hottest = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(year_data)):
        week_log = year_data[i]
        sun = week_log[0]
        mon = week_log[1]
        tue = week_log[2]
        wed = week_log[3]
        thu = week_log[4]
        fri = week_log[5]
        sat = week_log[6]
        if (sun >= mon and sun >= tue and sun >= wed
            and sun >= thu and sun >= fri and sun >= sat):
            hottest[0] += 1
        elif (mon >= sun and mon >= tue and mon >= wed
            and mon >= thu and mon >= fri and mon >= sat):
            hottest[1] += 1
        elif (tue >= sun and tue >= mon and tue >= wed
            and tue >= thu and tue >= fri and tue >= sat):
            hottest[2] += 1
        elif (wed >= sun and wed >= mon and wed >= tue
            and wed >= thu and wed >= fri and wed >= sat):
            hottest[3] += 1
        elif (thu >= sun and thu >= mon and thu >= tue
            and thu >= wed and thu >= fri and thu >= sat):
            hottest[4] += 1
        elif (fri >= sun and fri >= mon and fri >= tue
            and fri >= wed and fri >= thu and fri >= sat):
            hottest[5] += 1
        elif (sat >= sun and sat >= mon and sat >= tue
            and sat >= wed and sat >= thu and sat >= fri):
            hottest[6] += 1
    print(year_data)
    print(hottest)

def main():
    write_file("52weeks.txt", years())
    calc_hottest(read_file_to_int_list("52weeks.txt"))

main()
#calc_hottest()
