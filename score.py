#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    16 Feb 2019

Chapter 7: SAT Score Analysis
You have been asked to analyze SAT scores (which may be 400 - 1600).  
You will be analyzing a population (a list) which consists of a number of
samples (lists) of student scores. 
"""
import random
population=[]
for i in range(5):
    sample = []
    n = random.randint(5,10)
    for num in range(n):
        sample.append(random.randrange(400,1600))
    population.append(sample)

def mean(number_list):
    number_sum = 0
    for i in number_list:
        number_sum = i + number_sum
    number_mean = number_sum / len(number_list)
    return number_mean

def popsum(population):
    popsum = []
    for i in range(len(population)):
        for j in range(len(population[i])):
            popsum.append((population[i][j]))
    return popsum

print("Population is:")
print(population)
print("Number of scores counted is: ")
print(len(popsum(population)))
print("Total value of all scores counted is: ")
print(sum(popsum(population)))
print("Average of all scores is: ")
score_average = mean(popsum(population))
print(score_average)
print("Adjusted population is: ")
for i in range(len(population)):
    for j in range(len(population[i])):
        print(population[i][j])
print(population)
print("After removal of max and min values the population is: ")
for i in range(len(population)):
    population[i].remove(max(population[i]))
    population[i].remove(min(population[i]))
print(population)
print("Adjusted number of scores counted is: ")
print(len((popsum(population))))
print("Adjusted total value of all scores counted is: ")
print(sum(popsum(population)))
print("Adjusted average of all scores is: ")
print(mean(popsum(population)))
