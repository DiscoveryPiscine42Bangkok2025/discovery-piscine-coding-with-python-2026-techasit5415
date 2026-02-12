#!/usr/bin/env python3

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
ans = (num1 * num2)
print ((str)(num1) + " x " + (str)(num2) + " = " + (str)(ans))

if ans < 0 :
    print ("The result is negative.")
elif ans > 0:
    print ("The result is positive.")
else :
    print ("The result is positive and negative.")
