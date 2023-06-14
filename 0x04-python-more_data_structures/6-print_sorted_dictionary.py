#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newdict = {}
    for item in sorted(a_dictionary):
        print("{}: {}".format(item, a_dictionary.get(item)))
