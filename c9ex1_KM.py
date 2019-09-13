#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    CTIM-285 W01 / Professor Janet Brown-Sederberg
    17 May 2019

    Python class demo: chapter 9-1, restaurant

    The Club Diner of Bellmawr, NJ is in fact open 24 hours a day,
    "scrapple" is a breakfast meat,
    made from pork meat, skins, hearts, liver, and cornmeal.
    It is a Pennsylvania Dutch recipe and can be be found at Market Basket
    and Wegmans in New England for the grimly curious, and is rare outside of
    eastern PA near Philly, southern NJ and Baltimore, MD.
    Tastes good on a toasted kaiser roll.

    version 1.0: initial release
"""
class Restaurant():

    def __init__(self, name, cuisine_type, hours):
        self.name = name
        self.cuisine_type = cuisine_type
        self.hours = hours

    def describe_restaurant(self):
        print(self.name + " is known for their " + self.cuisine_type + ".")

    def open_restaurant(self):
        print(self.name + " is open " + self.hours+ ".")

restaurant = Restaurant('Club Diner', 'scrapple sandwich', '24 hours a day')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
