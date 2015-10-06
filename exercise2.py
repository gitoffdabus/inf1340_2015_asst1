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
    """
    For a given number of sides in a regular polygon, returns the shape name
    Inputs:
    Expected Outputs:
    Errors:
    """

    no_of_sides = input("Please provide the number of sides of a shape that you are thinking about: ")

    if no_of_sides == 3:
        print("The polygon you are thinking about is a TRIANGLE")
    elif no_of_sides == 4:
        print("The polygon you are thinking about is a QUADRILATERAL")
    elif no_of_sides == 5:
        print("The polygon you are thinking about is a PENTAGON")
    elif no_of_sides == 6:
        print("The polygon you are thinking about is a HEXAGON")
    elif no_of_sides == 7:
        print("The polygon you are thinking about is a HEPTAGON")
    elif no_of_sides == 8:
        print("The polygon you are thinking about is an OCTAGON")
    elif no_of_sides == 9:
        print("The polygon you are thinking about is an ENNEAGON")
    elif no_of_sides == 10:
        print("The polygon you are thinking about is a DECAGON")
    else:
        print("Error")

    #"""
    #name_that_shape()r a given number of sides in a regular polygon, returns the shape name

    #Inputs:

    #Expected Outputs:

    #Errors:
   # """

    #print("Error")


name_that_shape()