#Example #1
# The print function prints its parameter to standard out 
# and appends a line seperartor string to the end. 
print("Hello World")

#Example #2
# The print method may print its parameter without appending 
# a line seperator string to the end using the end parameter 
print("Hello World",end = " ")
print("Hello World")

#The print function may be given Strings as well as any of 
# the primitive and object types 
print(100)
print(True)
print(100.75)

# We can pass one or more parameters when using the print function
# BY default, they will be seperated by a space
print(100,True,100.75)

# The default space can be modified and can be made to change to 
# any characters, integer, or string using the sep parameter 
print(100,True,100.75,sep ="-")


# The sep and end parameters may be used together in one print statement 
print(100, True, 100.75, sep ="-", end="!")

# The string % modulo operator can be used with the print function 
# for formatring . 
print("\nHello %s %s. You are %d years old." %("Christopher","Velasco", 19))
print("\nHello %s %s. You are %.2f years old." %("Christopher","Velasco", 19.5))

# The input function can be used to get data from standard in 
# The returned object will always be a string 
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print(first,last)

age = input("Enter your age: ")
print("Hello %s %s. You are %s years old" %(first,last,age))

#This line of code will generate a TypeError because age is a string
#not a float
#print("Hello %s %s. You are %.2f years old."%(first,last,age))
print(type(first), type(last), type(age))

#We must typecat the return object if we want to work with 
#it in a form other than String. 
intage = int(input("PLease enter your age: "))
print("Hello %s %s. You are %d years old" %(first,last,intage))
floatage = float(input("PLease enter your age: "))
print("Hello %s %s. You are %.2f years old" %(first,last,floatage))


# The split function can be used to get multiple values from standard
# if a seperator isn't given to the function, then a white space is used.
fname, lname = input("Enter your first and last name seperated by a space: ").split()
print(fname,lname)

# A separator, like a comma, may be provided. 
fname, lname,tn = input("Enter your first and last name and telephone number seperated by a comma: ").split(",")
print("Hello %s %s. Your phone number is %s." %(fname,lname,tn))

#We can take in variable number of inputs at a time.
x = [int(x) for x in input("ENter multiple numbers seperated by a space: ").split()]
print("Numbers are: ", x)

#My Code For the Practice

#Ask the user for input
first, last, age = input("Enter your name and age seperated by a space: ").split()

#Print Out the Information in String Module
print("Hello %s %s. Your age is %s." %(first,last,age))