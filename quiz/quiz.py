'''
Created on Mar 6, 2022

The objective of this program is to quiz the used on basic high school trivia. It will also tell the user if their answer is correct and calculate their overall score.

@author: Maria Gironella
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.

score = 0

#Ask the user question one. And store the users answer.
print("1. What is the powerhouse of the cell")
question1 = input("Enter a letter. A)mitochondria B)nucleus C)ribosome")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if question1.upper() == "A":
    score = score + 1
    print("Correct")

else:
    print("Incorrect, the correct answer is A.")
    
#Ask the user question two. And store the users answer.
print("2. How many states comprise the United States?")
question2 = input("Enter a letter. A)13 B)45 C)50")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if question2.upper() == "C":
    score = score + 1
    print("Correct")
    
else:
    print("Incorrect, the correct answer is C.")
#Ask the user question three. And store the users answer.
print("3. In y=mx+b, what does m stand for?")
question3 = input("Enter a letter. A)slope B)output C)I don't understand math")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if question3.upper() == "A":
    score = score + 1
    print("Correct")
   
else:
    print("Incorrect, the correct answer is A.")
#Ask the user question four. And store the users answer.
print(" 4. In English, a person, place or thing is called:")
question4 = input("Enter a letter. A)verb B)adjective C)noun")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if  question4.upper() == "C":
    score = score + 1
    print("Correct")
   
else:
    print("Incorrect, the correct answer is C.")
#Calculate the percentage the user got. And store it in a variable called p
p = (score / 4) * 100

#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a " + str(score) + "/4. Or a " + str(p) + "%.")