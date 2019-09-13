#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    4 Mar 2019

    This is a Python script that makes a list of 52 lists.
    Each of the 52 lists has a number in it that ranges from 70-100 inclusive.
    It then checks each list element in all 52 lists to see which
    number is the highest in each respective list, and tallys
    it with the increment operator and else/if statements.

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
year_data = years()
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
