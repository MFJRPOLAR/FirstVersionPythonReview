# Expression in Python evaluate to true or false.
#Expressions use the comparission operators: <,
# >, <=, >=, ==, !=
x= 4 
print(x<5)
print(x>5)
print(x==5)
print(x!=5)

# Python supports the if, if-else, if-elif-else, and
# nested if decision structures. 

#The if decision structure tests its condition
#and if the is true, it executes the code 
#block  its given.
if (x<5):
    print("x is less than 5 is true")

#Here is the shorthand version of the if decision.
# THe shorthand version may be used when there is only
# one statement to be executed.
if (x<5): print("x is less than 5 is true.")

#The if-else decision structure tests its condition 
# and if the condition is true, it executes the code block
# it's given. If the condition is false, the code block
# given to the else is executed.
if (x==5):
    print("x is equal to 5 is true.")
else:
    print("x is equal to 5 is false.")

# Here is the shorthand version of the if-else decision.
print('x is equal to 5 is true.') if (x == 5) else print("x is equal to 5 is false.")

# The if-elif-else decision structure tests multiple
# conditions. The code block given to the condition that's
# true is executed if none of the condition are true,
# the code block given to the else is executed. 
if (x>5):
    print("x is greater than 5 is true.")
elif (x==5):
    print("x is equal to 5 is true")
elif (x<5):
    print("x is less than 5 is true.")
else:
    print("None of the conditions are true")


if (x>5):
    print("x is greater than 5 is true.")
elif (x==5):
    print("x is equal to 5 is true")
elif (x<5):
    print("x is less than 5 is true.")
elif (x!=5):
    # This code block won't be executed even
    # though its condition is true because only
    # the first true code bloack will be executes
    print("x is not equal to 5 is true.")
else:
    print("None of the conditions are true")

# A nested if decision is an if statemnet that is the target 
# of another if statement.
if (x < 5):
    print("x is less than 5 is true.")
    if (x!=5):
        print("x is not equal to 5 is true.")

# Comparision operator may be chained together.
a = 5
b = 10 
c = 15

if a < b < c:
    print("b is greater than a and less than c")


# Python supports the match-case decision structures. This 
# decision structure is useful when many conditions need to be tested 
# It requires Python 3.10 or newer.
grade = 'A'

match grade: 
    case 'A':
        print("Super Work!")
    case 'B':
        print("Good Job!")
    case 'C':
        print("You made it.")
    case 'D','F': 
        print("Oh, Dear....")
    case _:
        print("Invalid grade.")

#Python supports the ternary operator
result = 'x is equal to 5 is true' if (x==5) else 'x is equal to 5 is false.'
print(result)
print('x is equal to 5 is true' if (x==5) else 'x is equal to 5 is false.')

#The ternary operator may be written using tuples.
#(false value, true value) [expression to test]
# x = 5
result = ('x is equal to 5 is false.','x is equal to 5 is true')[x ==5]
print(result)

# The ternary operator may be written using dictionaries.
result = {True: 'x is equal to 5 is true', False: 'x is equal to 5 is false.'}[x==5]
print(result)

# Expression in Python may also use the logic operators:
# and, or, and not. 
num = 150

# This if-else decision structure tests if num is between 1 and 100.
if (num >= 1 and num <= 100):
    print('num is between 1 and 100')
else:
    print('num is not between 1 and 100')

# This if-else decision structure tests if num is not between 1 and 100.
if (num < 1 or num >100):
    print('num is not between 1 and 100')
else:
    print('num is between 1 and 100')

foundIt = False 

# This if-else decision structure tests if foundIt is False
if (not foundIt):
    print('foundIt is false.')
else:
    print("foundIt is True")

# My Code

#Grade
grade = "C"

if grade == "A":
    print("Super Work!")
elif grade == 'B':
    print("Good Job!")
elif grade == 'C':
    print("You made it.")
elif grade == 'D' and 'F': 
    print("Oh, Dear....")
else:
    print("Invalid grade.")


