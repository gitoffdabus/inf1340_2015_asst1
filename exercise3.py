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
# ans1, ans2, ans3, ans4, ans5 are the variables used to collect user response to the queries
        ans1 = raw_input("Is the car silent when you turn the key? Press [Y]Yes or [N]No")
# if statement is used to provide a response to the user for a final answer or a possible further query
        if ans1 == "Y":
            ans2 = raw_input("Are the battery terminals corroded? Press [Y]Yes or [N]No")
            if ans2 == "Y":
                print("Clean terminals and try starting again.")
            elif ans2 == "N":
                print("Replace cables and try again.")
            else:
                print("Error")
        elif ans1 == "N":
                ans2 = raw_input("Does the car make a clicking noise? Press [Y]Yes or [N]No")
                if ans2 == "Y":
                    print("Replace the battery.")
                elif ans2 == "N":
                        ans3 = raw_input("Does the car crank up but fail to start? Press [Y]Yes or [N]No")
                        if ans3 == "Y":
                            print("Check spark plug connections.")
                        elif ans3 == "N":
                                ans4 = raw_input("Does the engine start and then die? Press [Y]Yes or [N]No" + " ")
                                if ans4 == "Y":
                                        ans5 = raw_input("Does your car have fuel injection?Press [Y]Yes or [N]No" + " ")
                                        if ans5 == "Y":
                                            print("Get it in for service.")
                                        elif ans5 == "N":
                                            print("Check to ensure the choke is opening and closing.")
                                        else:
                                            print("Error")
                                elif ans4 == "N":
                                    print("Engine is not getting enough fuel. Clean fuel pump.")
                                else:
                                    print("Error")
                        else:
                            print("Error")
                else:
                    print("Error")
diagnose_car()

"""
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Test Case 1
    Input_1: Y
    Expected Output1: Are the battery terminals corroded?
    Errors: None
    Input_2: Y
    Expected Output_1: Clean terminals and try starting again.
    Errors: None

    Test Case 2
    Input_1: Y
    Expected Output_1: Are the battery terminals corroded?
    Error: None
    Input_2: N
    Expected Output_2: Replace cables and try again.
    Error: None

    Test Case 3
    Input_1: N
    Expected Output_1: Does the car make a clicking noise?
    Error: None
    Input_2: Y
    Expected Output_2: Replace the battery.
    Error: None

    Test Case 4
    Input_1: N
    Expected Output_1: Does the car make a clicking noise?
    Error: None
    Input_2: N
    Expected Output_2: Does the car crank up but fail to start?
    Error: None
    Input_3: Y
    Expected Output_3: Check spark plug connections.
    Error: None

    Test Case 5
    Input_1: N
    Expected Output_1: Does the car make a clicking noise?
    Error: None
    Input_2: N
    Expected Output_2: Does the car crank up but fail to start?
    Error: None
    Input_3:N
    Expected Output_3: Does the engine start and then die?
    Error: None
    Input_4: N
    Expected Output_4: Engine is not getting enough fuel. Clean fuel pump.
    Error: None

    Test Case 6
    Input_1: N
    Expected Output_1: Does the car make a clicking noise?
    Error: None
    Input_2: N
    Expected Output_2: Does the car crank up but fail to start?
    Error: None
    Input_3: N
    Expected Output_3: Does the engine start and then die?
    Error: None
    Input_4: Y
    Expected Output_4: Does your car have fuel injection?
    Error: None
    Input_5: N
    Expected Output_5: Check to ensure the choke is opening and closing.
    Error: Get it in service
    Solution: Yes and No are reversed on last two outcome nodes. Switch order and problem fixed.

    Test Case 7
    Input_1: N
    Expected Output_1: Does the car make a clicking noise?
    Error: None
    Input_2: N
    Expected Output_2: Does the car crank up but fail to start?
    Error: None
    Input_3: N
    Expected Output_3: Does the engine start and then die?
    Error: None
    Input_4: Y
    Expected Output_4: Does your car have fuel injection?
    Error: None
    Input_5: N
    Expected Output_5: Check to ensure the choke is opening and closing.
    Error: None

    Test Case 8
    Input_1: N
    Expected Output_1: Does the car make a clicking noise?
    Error: None
    Input_2: N
    Expected Output_2: Does the car crank up but fail to start?
    Error: None
    Input_3: N
    Expected Output_3: Does the engine start and then die?
    Error: None
    Input_4: Y
    Expected Output_4: Does your car have fuel injection?
    Error: None
    Input_5: Y
    Expected Output_5: Get it in service.
    Error: None

    """

