#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    13 Feb 2019

    Mrs. Mallard's Ducks: a quick exercise to demonstrate list handling.
"""
ducks = ["Pack", "Nack", "Lack", "Quack", "Kack", "Ouack", "Jack", "Mack"]
print(ducks)
ducks.sort()
print(ducks)
ducks.append("Zach") #zach is a rebel, he uses an "h" to spell his name
print(ducks)
corner = ducks.pop(5)
print(ducks)
ducks.insert(2, "Tack")
print(ducks)
ducks.sort(reverse=True)
print(ducks)
ducks.insert(2, corner)
print(ducks)
ducks.append("Back")
print(ducks)
del ducks[0] #time to leave Zach, you are no native child of Mrs. Mallard
print(ducks)
timeOut = ducks.pop()
print(ducks)
del ducks[0]
print(ducks)
ducks.append(timeOut)
print(ducks)
ducks.pop() # Back is popped straight into the bit bucket
print(ducks)
print(len(ducks))
print(ducks)
ducks.sort()
print(ducks)

