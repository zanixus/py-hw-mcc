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
##Here is the code to generate the  population/samples:
import random
population=[]
for i in range(5):
    sample = []
    n = random.randint(5,10)
    for num in range(n):
        sample.append(random.randrange(400,1600))
    population.append(sample)

print(population)
