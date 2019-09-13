#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    CTIM-285 W01 / Professor Janet Brown-Sederberg
    17 May 2019

    Python class demo: chapter 9-4, restaurant

    version 1.0: initial release
"""
class Restaurant():

    def __init__(self, name, cuisine_type, hours):
        self.name = name
        self.cuisine_type = cuisine_type
        self.hours = hours
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + " is known for their " + self.cuisine_type + ".")

    def open_restaurant(self):
        print(self.name + " is open " + self.hours+ ".")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant('Club Diner', 'scrapple sandwich', '24 hours a day')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(302)
print("Number of customers served: " + str(restaurant.number_served))
for i in range(49):
    restaurant.increment_number_served(1)
print("Number of customers served: " + str(restaurant.number_served))
