# Here is a program that shows basic math operations
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Tell the user what the program will do...

print ("This program will perform mathematical calculations")

# 'num1' and 'num2' will hold numbers typed in from the keyboard
# and they will be stored as something called a 'float' which
# is another way to say 'decimal'

num1 = float(input("What is the first number? \n"))
num2 = float(input("What is the second number? \n"))

# * is the symbol we use for multiplication
# / is the symbol we use for division
# + is the symbol we use for addition
# - is the symbol we use for subtraction

def add(n1, n2, r):
	return round(n1 + n2, r)

def subtract(n1,n2, r):
	return round(n1 - n2, r)

def multiply(n1, n2, r):
	return round(n1 * n2, r)

def quotient(n1, n2, r):
	return round(n1 / n2, r) 

answer1 = add(num1, num2, 10)
answer2 = subtract(num1, num2, 10)
answer3 = multiply(num1, num2, 10)
answer4 = quotient(num1, num2, 10)


# round the answer to 5 decimal places
# add 'str' so that it can be treated as a sentence

print (f"The addition will give: {str(answer1)}")
print (f"The subtaction will give: {str(answer2)}")
print (f"The multiplication will give: {str(answer3)}")
print (f"The division will give: {str(answer4)}")

# This is a way to gracefully exit the program
input("Press ENTER to quit the program")