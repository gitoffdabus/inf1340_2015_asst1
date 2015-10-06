#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#Interactively queries the user with yes/no questions to identify a
#possible issue with a car.

# Inputs:
def diagnose_car():
    ans1 = None
    print ("Is the car silent when you turn the key?")
    ans1 = raw_input("Press [Y]Yes or [N]No")
    if ans1 == "y":
        print ("Are the battery terminals corroded?")
        ans2 = raw_input("Press [Y]Yes or [N]No")
        if ans2 == "y":
            print ("Clean terminals and try starting again.")
        else:
            print ("Replace cables and try again.")
    else:
        print ("Does the car make a clicking noise?")
        ans3 = raw_input("Press [Y]Yes or [N]No")
        if ans3 == "y":
            print ("Replace the battery.")
        else:
            print ("Does the car crank up but fail to start?")
            ans4 = raw_input("Press [Y]Yes or [N]No")
            if ans4 == "y":
                print ("Check spark plug connections.")
            else:
                print ("Does the engine start and then die?")
                ans5 = raw_input("Press [Y]Yes or [N]No")
                if ans5 == "y":
                    print ("Does your car have fuel injection?")
                    ans6 = raw_input("Press [Y]Yes or [N]No")
                    if ans6 == "y":
                        print ("Get it in for service.")
                    else:
                      print ("Check to ensure the choke is opening and closing.")
                else:
                    print ("Engine is not getting enough fuel. Clean fuel pump.")



diagnose_car()

"""
Test Case 1
user_input = n, n, n, y, y
expected output = Check to ensure the choke is opening and closing.
actual output = Get it in for service

Reason = Yes and No nodes are reversed in last column. Had to switch ordering of statements.

Test Case 2
user_input = n, n, n, n
expected output = Engine is not getting enough fuel. Clean fuel pump.
actual output = Program ends after the prompt, "Does the engine start and then die?"

Reason = else statement for "Engine is not getting enough fuel. Clean fuel pump." was not properly indented.

Test Case 3
user_input = other than "y" or "n"
expected output = ?
actual output = registers as "n"

fixing problem:
make ans1 = None
run again - input "y"
stop program and run again
input other than "y" or "n"
assumes input is "n"


 """