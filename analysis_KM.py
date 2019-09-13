#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    19 April 2019

    File I/O grade calculator demo. Intended to be fairly user friendly.

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
    return int(good_value)

def mean(number_list):
    number_sum = 0
    for i in number_list:
        number_sum = i + number_sum
    number_mean = number_sum / len(number_list)
    return number_mean

def variance(number_list, mean_input):
    numbers_squared = []
    for i in number_list:
        numbers_squared.append((mean_input - i) ** 2)
    return (mean(numbers_squared))

def std_deviation(variance_input):
    return (variance_input ** (.5))

def write_file(filename, list_data):
    with open(filename, 'w') as file_object:
        for i in range(len(list_data)):
            file_object.write(str(list_data[i])+"\n")

def read_file_to_list(filename):
    new_list = []
    with open(filename) as file_object:
        for line in file_object:
            new_list.append(int(line.rstrip()))
    return new_list

def get_grades():
    grades = []
    for i in range(10):
        new_grade = 0
        while new_grade < 1 or new_grade > 100:
            print("Please enter a grade for student "+str(i+1)+", 1 to 100:")
            new_grade = int_input()
        grades.append(new_grade)
    return grades

def print_grades(grades):
    grade_mean = mean(grades)
    grade_variance = variance(grades, grade_mean)
    grade_std_deviation = std_deviation(grade_variance)
    print("\n")
    print("Mean: " + str(grade_mean) + "\n")
    print("Variance: " + str(grade_variance)+"\n")
    print("Standard Deviation: " + str(grade_std_deviation)+ "\n")

def main():
    grades = get_grades()
    write_file('scores.txt', grades)
    print_grades(read_file_to_list('scores.txt'))

main()
