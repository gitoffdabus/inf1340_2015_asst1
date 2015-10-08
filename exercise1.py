#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#calculate cost of total shares
#calculate commission costs
#deduct the amount she paid her stockbroker

number_of_shares = 2000
initial_share = 900
sales_share = 942.75
commission_percentage = .03

# Commission paid to the broker for purchasing the shares
initial_commission = (number_of_shares * initial_share) * commission_percentage

# Total cost of purchasing the shares
initial_cost = (number_of_shares * initial_share) + initial_commission

# Commission paid to the broker for selling the shares
sales_commission = (number_of_shares * sales_share) * commission_percentage

# Total cost of selling the shares
sales_price = (number_of_shares * sales_share) - sales_commission

# Calculation of money left with Lakshmi
money = sales_price - initial_cost
print ("Lakshmi is at a balance of %d after selling her stock and paying her broker twice" %money)
print("Thus, Lakshmi suffered a loss")

"""
Test Case 1
no input required
expected output:-25065
actual output: -25065
Error: None

"""