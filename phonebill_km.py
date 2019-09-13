#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    13 Feb 2019

    This is a quick 15-line Python program to append lowest, highest
    and average amounts of minutes spend on a list of phone bills.
    It uses a for loop, list slicing and a function call to append
    new data to the existing phonebill list. Nikolai, you're grounded.

"""
def low_high(minutes_list, list_index, sort_high):
    sorted_list = minutes_list[list_index][1][:]
    sorted_list.sort(reverse=sort_high)
    return sorted_list[0]
phonebill = [
  ["Kiera", [11,21,13,14,15,60,38], "508-111-1110"],
  ["Lorenzo", [20,12,33,26,37,62,70],"508-111-1111"],
  ["Mabel", [31,27,43,7,52,68,5],"508-111-1112"],
  ["Nikolai", [8,7,212,28,114,30,39],"508-111-1113"]
  ]
for i in range(len(phonebill)):
    phonebill[i].append(low_high(phonebill, i, False))
    phonebill[i].append(low_high(phonebill, i, True))
    phonebill[i].append((sum(phonebill[i][1][:]) / (len(phonebill[i][1][:]))))
print(phonebill)
