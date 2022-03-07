'''
Created on Mar 6, 2022

In this kkkljlj

@author: Maria Gironella
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.

score = 0

#Ask the user question one. And store the users answer.
question1 = input("What is the powerhouse of the cell?")
print(question1)

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if question1.upper() == "A":
    print("Correct")

else:
    print("Incorrect, the correct answer is A.")
    
#Ask the user question two. And store the users answer.
question2 = input("How many states comprise the United States?")
print(question2)
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if question2.upper() == "C":
    print("Correct")
   
else:
    print("Incorrect, the correct answer is C.")
#Ask the user question three. And store the users answer.
question3 = input("In y=mx+b, what does m stand for?")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if question3.upper() == "A":
    print("Correct")
   
else:
    print("Incorrect, the correct answer is A.")
#Ask the user question four. And store the users answer.
question4 = input("In English, a person, place or thing is called:")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if  question4.upper() == "C":
    print("Correct")
   
else:
    print("Incorrect, the correct answer is C.")
#Calculate the percentage the user got. And store it in a variable called p
p = (score / 4) * 100
print(p)
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a " + str(score) + "/4. Or a " + str(p) + "%.")