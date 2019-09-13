#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    16 Feb 2019

    Grade analysis script. Reuses functions from the old script.
    The functions copy tuple information into lists internally and return
    valid values. A list of tuples is used in the main program body.

    Version 1.0: initial release
"""
def mean(tuple_list):
    number_sum = 0
    for i in range (len(tuple_list)):
        number_sum = tuple_list[i][1] + number_sum
    number_mean = number_sum / len(tuple_list)
    return number_mean

def variance(tuple_list, mean_input):
    grade_list = []
    list_position = 0
    for i in range (len(tuple_list)):
        grade_list.insert(list_position, tuple_list[i][1])
        list_position += 1
    numbers_squared = []
    list_position = 0
    for i in grade_list:
        numbers_squared.insert(list_position, (mean_input - i) ** 2)
        list_position += 1
    get_variance = 0
    for i in numbers_squared:
        get_variance = i + get_variance
    return (get_variance / len(numbers_squared))

def std_deviation(variance_input):
    return (variance_input ** (.5))

students = [
           ('abbey', 95), ('ben', 66), ('charlotte', 87),
           ('david', 90), ('emma', 73), ('frank', 82),
           ('georgia', 65), ('harry', 77), ('isabelle', 81), ('jeb', 86)
           ]
grade_mean = mean(students)
grade_variance = variance(students, grade_mean)
grade_std_deviation = std_deviation(grade_variance)
print("\n")
print("Mean: " + str(grade_mean) + "\n")
print("Variance: " + str(grade_variance)+"\n")
print("Standard Deviation: " + str(grade_std_deviation)+ "\n")
