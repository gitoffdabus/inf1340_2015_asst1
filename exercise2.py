#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    no_of_sides = raw_input("Please provide the number of sides of a shape that you are thinking about: ")
#   if statement is used to provide answers to the possible inputs of the user
    if no_of_sides == "3":
        print("triangle")
    elif no_of_sides == "4":
        print("quadrilateral")
    elif no_of_sides == "5":
        print("pentagon")
    elif no_of_sides == "6":
        print("hexagon")
    elif no_of_sides == "7":
        print("heptagon")
    elif no_of_sides == "8":
        print("octagon")
    elif no_of_sides == "9":
        print("nonagon")
    elif no_of_sides == "10":
        print("decagon")
    else:
        print("Error")
# Error is printed if the user provides an illegal input i.e. a number outside 3-10
#name_that_shape()
"""
Test Case 1
user input = 1
expected output = Error
Error: None

Test Case 2
user input = 2
expected output = Error
Error: None

Test Case 3
user input = 3
expected output = Error
Error: None

Test Case 4
user input = 4
expected output = quadrilateral
Error: None

Test Case 5
user_input = 5
expected output = pentagon
Error: None

Test Case 6
user_input = 6
expected output = hexagon
Error: None

Test Case 7
user input = 7
expected output = heptagon
Error: None

Test Case 8
user input = 8
expected output = octagon
Error: None

Test Case 9
user input = 9
expected output = nonagon
Error: None

Test Case 10
user input = 10
expected output = Error
Error: None

Test Case 11
user input = "three"
expected output = Error
Error: None

Test Case 12
user input = 4.5
expected output = Error
Error: None

Test Case 13
user input = 4.0
expected output = Error
Error: None

"""

