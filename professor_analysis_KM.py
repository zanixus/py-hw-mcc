#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    16 Feb 2019

    Grade analysis script that handles tuple input.
"""
def mean(number_list):
    number_sum = 0
    for i in number_list:
        number_sum = i + number_sum
    number_mean = number_sum / len(number_list)
    return number_mean

def variance(number_list, mean_input):
    print(number_list)
    numbers_squared = []
    list_position = 0
    for i in number_list:
        list_position = 0
        numbers_squared.insert(list_position, (mean_input - i) ** 2)
        list_position += 1
    return (mean(numbers_squared))

def std_deviation(variance_input):
    return (variance_input ** (.5))

abbey = 72
ben = 84
charlotte = 70
david = 85
emma = 88
frank = 81
georgia = 77
harry = 77
isabelle = 87
jeb = 63
grades = [abbey, ben, charlotte, david, emma,
         frank, georgia, harry, isabelle, jeb]
print(grades)
grade_mean = mean(grades)
grade_variance = variance(grades, grade_mean)
grade_std_deviation = std_deviation(grade_variance)
print("\n")
print("Mean: " + str(grade_mean) + "\n")
print("Variance: " + str(grade_variance)+"\n")
print("Standard Deviation: " + str(grade_std_deviation)+ "\n")
