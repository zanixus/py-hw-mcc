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
population=[[13, 6, 13, 8, 10, 4, 8, 5], [4, 5, 4, 7, 6, 13, 6, 6, 11, 8], [13, 12, 7, 15, 15, 4, 10], [5, 15, 10, 15, 4, 13, 10], [14, 11, 6, 13, 11, 6]]

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
print(mean(popsum(population)))
print("Adjusted population is: ")
population=[[13, 6, 13, 8, 10, 4, 8, 5, 10, 11, 15], [4, 5, 4, 7, 6, 13, 6, 6, 11, 8, 14, 12, 11, 13, 11, 11, 15], [13, 12, 7, 15, 15, 4, 10], [5, 15, 10, 15, 4, 13, 10], [14, 11, 6, 13, 11, 6]]
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
