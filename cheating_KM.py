#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    9 Mar 2019

    This is a Python script to compare a list of grades. It compares two dictionaries,
    grabs their keys and values, and if they are identical, prints a message.
    This program matches the output profile exactly given the default dataset
    from the assignment (Noah [b,a,a], ...), but it is set up to run with a randomly
    generated dictionary value set.

"""
import random
##
## dataset generator code by ProfJBS begins below
##the students in the class
##the most popular names in 2018
students = \
["Noah",\
"Liam",\
"Benjamin",\
"Oliver",\
"William",\
"James",\
"Elijah",\
"Lucas",\
"Mason",\
"Michael",\
"Olivia",\
"Emma",\
"Ava",\
"Charlotte",\
"Mia",\
"Sophia",\
"Isabella",\
"Harper",\
"Amelia",\
"Evelyn"
 ]

##needed to build the test results
test_results = [] 
answers = ['a', 'b', 'c', 'd'] 
num_questions = 3  ##You may change the number for testing, a smaller number
                  	         ##will made testing the correctness of your code easier
##this code will build a dictionary of length 20 of 
##key - student name
##value - a list of num_questions length of randomly selected
##values from the list answers above
for student in students:
  result = []
  for i in range(num_questions):
    result.append(random.choice(answers))
  test = {}
  test[student] = result
  test_results.append(test)
##
## homework solution code by KMM begins below
##
def grade_compare(dict1, dict2):
  for i in dict1.keys():
    orig = i#bad idea usually, but our dictionary only has one key:value pair
  for j in dict2.keys():
    copier = j
  for val1 in dict1:
    for val2 in dict2:
      if dict1[val1] == dict2[val2] and orig != copier:
        print(copier+" "+str(dict2[val2])+ " copied "+orig+" "+str(dict1[val1]))
print("Raw Data:")
print(test_results)
print("Names and Answers of Each Student")
for i in range(len(test_results)):
  print(students[i] +" " +str(test_results[i][students[i]]))
print("Names and Answers of Students Who Copied")
for i in range(len(test_results)):
  for j in range(len(test_results)):
    grade_compare(test_results[j], test_results[i])
