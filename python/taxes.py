import sys
import math
#inport random
import threading
import time
from functools import reduce

#print("This is 5 + 2 =", 5 + 2)

#name = input("What is your name?")
#print("Hi", name)

#v1 = (
#    1 + 2 + 3
#)
#print(v1)

#v1 = 1 + 2\
#    + 3
#print(v1)

#v3 = v4 = 1


income = input("What is your income : ")
hold_income = income = int(income)

taxes = 0

if(income > 510301) :
    taxes += (income - 510301) * 0.37
    income = 510301

if(income > 204101) :
    taxes += (income - taxes - 204101) * 0.35
    income = 204101

if(income > 160726) :
    taxes += (income - taxes - 160726) * 0.32
    income = 160726

if(income > 84201) :
    taxes += (income - taxes - 84201) * 0.24
    income = 84201

if(income > 39476) :
    taxes += (income - taxes - 39476) * 0.22
    income = 39476

if(income > 9701) :
    taxes += (income - taxes - 9701) * 0.12
    income = 9701

if(income > 0) : 
    taxes += (income - taxes - 0) * 0.10
    income = 0

print("The amount of taxes you will pay is %.2f: " % taxes)
print("Your income after taxes is : %.2f" % (hold_income - taxes))
print("This is equivilent to a %.2f flat tax" % (taxes / hold_income))




