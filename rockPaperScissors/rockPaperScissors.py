'''
Created on Apr 10, 2022

Objective: The Objective of this program is to make a Rock, Paper, Scissors game for the user to play against the computer. The tasks to complete are:
There should be a loop to repeat the game. And the game should go as follows:
    Welcome the user with "Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit"
    Create variables to keep track of score
    Begin a loop to repeat rounds until somebody wins. Someone wins when they have won 2 rounds. (Rounds are outlined below).
    Once someone has won, print "Thanks for playing!", print out the final scores, and if the user wins: print "You win!"; if the cpu wins: print "CPU wins!"
    Repeat the whole game once someone wins. And until the user chooses to quit.
        Includes:
        Have the user choose rock, paper, scissors, or q
        Generate a random choice from the computer
    Repeat the rounds until someone wins.

@author: Maria Gironella
'''

#import random
import random
#Make a boolean variable called keepPlaying to track whether they want to keep playing and set to to True
keepPlaying = True
#LOOP: Make a game loop that continues while keepPlaying is true.
while(keepPlaying):
    #Print out a statement to welcome the user to the game
    print("Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit.")
    #Make variables called userScore and cpuScore to track score, set to 0
    userScore = 0
    cpuScore = 0
    #LOOP:Make a round loop that continues while the userScore or spuScore is less than 2.
    while(userScore < 2 and cpuScore < 2):
        #Use input() to get a choice from the user (Rock, paper, or scissors, or quit).
        #Store the choice in a variable.
        #Use .lower() to make the users choice all lower case
        user = input("Please choose (rock, paper, scissors): ").lower()
        #Make a list of choices, then use random.choice() to get a random choice for the cpu.
        #Store the choice in a variable
        cpuChoice = ["rock", "paper", "scissors"]
        cpu = random.choice(cpuChoice)
        #Make a if/elif/else statement to check the users input against the cpu's choice:
        #NOTE: you will have to compare the users choice and the cpu choice to "rock", "paper", and "scissors" separately and combine with logical operators.
        
        #if the user won, add one to the users score, then print out the scores.
        #"User: [#], CPU: [#]"
        '''
        Check the users input against the computers choice to see who won the round:
        if the user won, add one to the users score, then print out the scores: "User: [#], Computer [#]”
        else if the computer won, add one to the computer’s score, then print out the scores: "User: [#], Computer [#]"
        else if it was a draw, print "DRAW", then print out the scores: "User: [#], Computer [#]"
        else if the user entered "q", then end the round, and the game loop.
        else the user didn't enter an accepted input, and prompt them to try again: "Not an option try again."
        '''
        if((user == "rock" and cpu == "scissors") or (user == "paper" and cpu == "rock") or (user == "scissors" and cpu == "paper")):
            userScore = userScore + 1
            print("User: " + str(userScore) + "CUP: " + str(cpuScore))
        #else if (elif) the cpu won, add one to the computer's score, then print out the scores . . .
        elif((user == "rock" and cpu == "paper") or (user == "paper" and cpu == "scissors") or (user == "scissors" and cpu == "rock")):
            cpuScore = cpuScore + 1
            print("User: " + str(userScore) + "CUP: " + str(cpuScore))
        #else if tie, print "DRAW", then print out the scores . . .
        elif((user == "rock" and cpu == "rock") or (user == "paper" and cpu =="paper") or (user == "scissors" and cpu == "scissors")):
            print("DRAW")
            print("User: " + str(userScore) + "CUP: " + str(cpuScore))
            
        #else if the user entered 'q', then end the round, and the game loop.
        #Use the break statement to end the round. . . Make keepPlaying equal False.
        elif(user == 'q'):
            keepPlaying = False
            break
        
        #else the user didn't enter an accepted input, print "Not an option, try again."
        else:
            print("Not an option, try again.")
        
    #print out thank you message 
    print("Thanks for playing!")
    #print out who won:
    
    #if userScore is 2, then the user won
        #code
    '''
    If user won print out "You win!" and if CPU won, print out "CPU wins!".
    '''
    if(userScore == 2):
        print("You win!")
    #elif the cpuScore is 2, then the cpu won
        #code
    elif(cpuScore == 2):
        print("CPU wins!")
    #print out the final scores
    print("User: " + str(userScore) + "CUP: " + str(cpuScore))
        
        
        
        
        
        
        
        
        
        