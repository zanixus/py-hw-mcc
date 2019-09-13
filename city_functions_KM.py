#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    CTIM-285 W01 / Professor Janet Brown-Sederberg
    17 May 2019

    version 1.0: initial release
"""
def city_country(city, country, population = 0):
    return_string = (city.title() + ", " + country.title())
    if population:
        return (return_string + " - population " + str(population))
    else:
        return return_string
