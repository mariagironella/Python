'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

'''
This function indetifies if two colors are Blue.
Then it returns True or False.
'''
def color(colorOne, colorTwo):
    if (colorOne and colorTwo == "Blue"):

        return True

    else:
        return False


x = "Blue"
y = "Red"
color(x,y)
print(color(x,y))


#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.

'''
This function converts gallons to cups.
Then it returns the number of cups.
'''
def conversion(numOne):
    cups = numOne * 16
    return cups
    
z = 2
conversion(z)
print(conversion(z))

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.
def sumOfNumbers(numOne, numTwo, numThree):
    answer = numOne + NumTwo + numThree
    return answer

