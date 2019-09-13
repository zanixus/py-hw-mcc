import random

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
