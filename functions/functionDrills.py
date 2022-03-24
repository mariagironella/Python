'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
from pickle import TRUE
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
'''
This functions subtracts the second inputed number from the first.
Then is returns the answer.
'''
def subtraction(num1, num2):
    answer = num1 - num2
    
    return answer

a = 4
b = 2
subtraction(a,b)
print(subtraction(a,b))

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.
'''
This function divided an integer by 2 then multiplies it by 77 then adds 10000.
Then is returns and prints the answer.
'''
def mathematicalFunction(num1):
    answer = ((num1 / 2) * 77) + 10000
    print(answer)
    return answer


#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.
'''
This function compares two numbers and determines if they are equal.
Then it returns either True or False.
'''
def areTwoNumsEqual(num1, num2):
    if (num1 == num2):
        return True
    else:
        return False

c = 1
d = 1
areTwoNumsEqual(c,d)
print(areTwoNumsEqual(c,d))

#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.
'''
This function determines which parameter is larger, or if they are the same.
Then it returns the larger parameter.
'''
def whichIsLarger(par1, par2):
    if (par1 >= par2):
        return par1
    else:
        return par2

e = 6
f = 8
whichIsLarger(e,f)
print(whichIsLarger(e,f))
#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
'''
This function adds two string variable together.
Then it returns the combined string.
'''
def addingString(string1, string2):
    combString = string1 + string2
    return combString

g = "Two peas "
h = "in a pod"
addingString(g,h)
print(addingString(g,h))

#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
'''
This function determines if the fist number is equal to the second or third number.
Then returns True if it is or False if it is not.
'''
def compNums(num1, num2, num3):
    if (num1 == num2 or num1 == num3):
        return True 
    else:
        return False
    
i = 8
j = 4
k = 8
compNums(i,j,k)
print(compNums(i,j,k))

#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.
'''
This function prints my name.
It does not return anything
'''
def myName():
    print("Maria")
    return 



#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.
'''
The function determines if the given color is my favorite color. If correct it prints "That's my favorite color!" and if not, it prints "That is not my favorite color."
It does not return anything
'''
def favColor(color):
    if (color == "purple"):
        print("That's my favorite color!")
    else:
        print("That is not my favorite color.")
    return

l = "blue"
favColor(l)


#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.
'''
The function runs a loop, printing the positive integer, until the integer equals zero.
It does not return anything.
'''
def zeroLoop(posInt):
    while (posInt > 0):
        posInt = posInt - 1
        print(posInt)
        
        
        
    
m = 12
zeroLoop(m)

