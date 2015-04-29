import random, os
os.system("clear")
print("Welcome to Rock, Paper, Scissors!\n")
while (True):
        choices = ['rock', 'paper', 'scissors']
        aihand = random.choice(choices)
        userhand = input("\nrock, paper or scissors? ")

        print("You said " + userhand + " and your opponent chose " + aihand + "...\n")

        if(aihand == userhand):
                print ("It's a Draw!")
        elif (aihand == "rock" and userhand == "scissors"):
                print ("You Lose!")
        elif (aihand == "rock" and userhand == "paper"):
                print ("You Win!")
                break
        elif (aihand == "scissors" and userhand == "rock"):
                print ("You Win!")
                break
        elif (aihand == "scissors" and userhand == "paper"):
                print ("You Lose!")
        elif (aihand == "paper" and userhand == "rock"):
                print ("You Lose!")
        elif (aihand == "paper" and userhand == "scissors"):
                print ("You Win!")
                break
        else:
                print ("Command not recognized!")
