#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():

    ans1 = None
    while ans1 not in ("y", "n"):
        print("Is the car silent when you turn the key?")
        ans1 = raw_input("Press [Y]Yes or [N]No")
        if ans1 == "y":
            ans2 = None
            while ans2 not in ("y", "n"):
                print("Are the battery terminals corroded?")
                ans2 = raw_input("Press [Y]Yes or [N]No")
                if ans2 == "y":
                    print("Clean terminals and try starting again")
                elif ans2 == "n":
                    print("Replace cables and try again")
                else:
                    print("You have made a wrong selection. Please Press Y or N")
        elif ans1 == "n":
            ans2 = None
            while ans2 not in ("y", "n"):
                print("Does the car make a clicking noise")
                ans2 = raw_input("Press [Y]Yes or [N]No")
                if ans2 == "y":
                    print("Replace the battery")
                elif ans2 == "n":
                    ans3 = None
                    while ans3 not in ("y", "n"):
                        print("Does the car crank up but fail to start?")
                        ans3 = raw_input("Press [Y]Yes or [N]No")
                        if ans3 == "y":
                            print("Check spark plug connections")
                        elif ans3 == "n":
                            ans4 = None
                            while ans4 not in ("y", "n"):
                                print("Does the engine start and then die?")
                                ans4 = raw_input("Press [Y]Yes or [N]No")
                                if ans4 == "y":
                                    ans5 = None
                                    while ans5 not in ("y", "n"):
                                        print("Does your car have fuel injection?")
                                        ans5 = raw_input("Press [Y]Yes or [N]No")
                                        if ans5 == "y":
                                            print("Get it in for Service!")
                                        elif ans5 == "n":
                                            print("Check to insure the choke is opening and closing")
                                        else:
                                            print("You have made a wrong selection. Please press Y or N")
                                elif ans4 == "n":
                                    print("Engine is not getting enough fuel. Clean fuel pump.")
                                else:
                                    print("You have made a wrong selection. Please press Y or N")
                        else:
                            print("You have made a wrong selection. Please press Y or N")

                else:
                    print("You have made a wrong selection. Please press Y or N")
        else:
            print("You have made a wrong selection. Please press Y or N")

    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

diagnose_car()