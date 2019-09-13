#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    06 May 2019

    Python trip itinerary calculator. Needs zip codes csv.
    This program uses lists and dictionaries to calculate distance
    between destinations. It prints outputs in km and attempts
    to handle user input error.

"""


import csv
import math
from math import radians, sin, cos, acos
###
###     begin code by ProfJBS here
###
def calcDistance(start, end):
    """Function accepts start and end positions"""
    """Each start and end position is a 2 element list of """
    """latitude and longitude.  The function"""
    """calculates and returns the distance beyween the start"""
    """and end positions"""
    slat = radians(start[0])
    slon = radians(start[1])
    elat = radians(end[0])
    elon = radians(end[1])
    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return (dist)

def calcDistanceOfJourney(journey, GPS):
    """Function accepts a list of the names"""
    """of the cities to visit and a dictionary of"""
    """the latitude and longitude"""
    sum = 0
    for i in range(len(journey) - 1):
        sum = sum + calcDistance(GPS[journey[i]], GPS[journey[i + 1]])
        #print(sum)
    sum = sum + calcDistance(GPS[journey[len(journey) - 1]], GPS[journey[0]])
    return(sum)
##the latitude and longitude of the cities
coordinates = {
        "Boston":[42.3656 , -71.0096],
        "Chicago":[41.9742, -87.9073],
        "Atlanta":[33.6407, -84.4277],
        "Dallas":[32.8998, -97.0403],
        "Los Angeles":[33.9416, -118.4085],
        }
##
##  begin code by KMM here
##
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

def read_csv(filename, index):
    with open(filename) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)
        csvlist = []
        for row in reader:
            csvdata = row[index]
            csvlist.append(csvdata)
    return csvlist

def check_city(trip, city_master, state_master):
    index = -1
    for k, v in trip.items():
        city = k
        state = v
    for i in range(len(city_master)):
        if city == city_master[i] and state == state_master[i]:
            index = i
    return index

def itinerary():
    print("Please enter the amount of cities you will visit.")
    stops = int_input()
    itinerary = []
    for i in range(stops):
        citystate = {}
        print("Please enter a city. This is destination " + str(i+1) + ".")
        city = input()
        print("What state is " + str(city) + " in?")
        state = input()
        citystate[city.title()] = state.upper()
        itinerary.append(citystate)
    return itinerary

def main():
    plan = itinerary()
    lat = read_csv('zip_codes_states.csv', 1)
    lon = read_csv('zip_codes_states.csv', 2)
    cities = read_csv('zip_codes_states.csv', 3)
    states = read_csv('zip_codes_states.csv', 4)
    #build a list of strings in order for the trip. use index
    trip = []
    order = []
    coord = {}
    for i in range(len(plan)):
        loc = []
        index = check_city(plan[i], cities, states)
        if index > -1:
            trip.append(cities[index])
            loc.append(float(lat[index]))
            loc.append(float(lon[index]))
            order.append(loc)
            coord[cities[index]] = loc
        else:
            for k, v in plan[i].items():
                print ("Location "+ k + ", " + v +\
                        " not found in master list. Trip location dropped.")
    #build a dict of cityname:[lat, long] to use as "GPS". use index
    print(coord)
    trip_length = len(order)
    for i in range(trip_length):
        if i < trip_length -1:
            length = calcDistance(order[i], order[i + 1])
            print("Length of trip from " + str(trip[i]) + \
                    " to " + str(trip[i + 1] + ": " + str(length)) + " km")
    total_distance = calcDistanceOfJourney(trip, coord)
    print("Total length of trip: " + str(total_distance) + " kilometers")

main()
