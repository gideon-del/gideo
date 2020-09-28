import random

def usersChoice(user):
    user=user.lower()
    return user
computer = random.randint(0, 2)
def  computerChoice(computer):
    if computer==1 :
        computer= "paper"
    elif computer==0 :
        computer = "rock"
    elif computer == 2 :
        computer = "scissors"
    else:
        computer = "Something went wrong"
    return computer
#print(computerChoice(computer))
def determineWinner(user, computer):
    if user == computer :
        return "it is a tie"
    elif user == "paper":
        if computer=="scissors":
            return "Computer win"
        else:
            return "You win"
    elif user == "scissors" :
        if computer== "paper":
            return "You win"
        else:
            return "Computer win"
    elif user == "rock" :
        if computer == "scissors" :
            return "You win"
        else:
            return "Computer win"
    else :
        return "Invalid input"
#print(game)
user_score = 0
computer_score = 0
i = 0
while i < 3:
    user=input("Enter rock paper or scissors: ")
    computer= random.randint(0,2)
    print(computerChoice(computer))
    game= determineWinner(usersChoice(user),computerChoice(computer))
    print(game)
    if game == "You win" :
        user_score += 1
    elif game == "Computer win" :
        computer_score += 1
    else:
        print("Nobody wins this round")
    i += 1
if  user_score > computer_score :
    print("You scored " + str(user_score) + " and computer scored " + str(computer_score) +". You win")
elif user_score < computer_score :
    print("You scored " + str(user_score) + " and computer scored " + str(computer_score) +". Computer wins")
else:
    print("You scored " + str(user_score) + " and computer scored " + str(computer_score) +". it is a tie")
round2= input("would you like to play another round: ")
round2 = round2.lower()
user_score2 = 0
computer_score2 =0
total_user_score = user_score + user_score2
total_computer_score = computer_score + computer_score2
if round2 == "yes" :
    g = 0
    while g < 3:
     user=input("Enter rock paper or scissors: ")
     computer= random.randint(0,2)
     print(computerChoice(computer))
     game= determineWinner(usersChoice(user),computerChoice(computer))
     print(game)
     if game == "You win" :
        user_score2 += 1
     elif game == "Computer win" :
        computer_score2 += 1
     else:
        print("Nobody wins this round")
     g += 1
    if  user_score2 > computer_score2 :
     print("You scored " + str(user_score2) + " and computer scored " + str(computer_score2) +". You win")
    elif user_score < computer_score2 :
     print("You scored " + str(user_score2) + " and computer scored " + str(computer_score2) +". Computer wins")
    else:
     print("You scored " + str(user_score2) + " and computer scored " + str(computer_score2) +". it is a tie")
    total_user_score = user_score + user_score2
    total_computer_score = computer_score + computer_score2
    if total_user_score > total_computer_score:
        print("Your total score is " + str(total_user_score) + " and the computer total score is " + str(total_computer_score) + ". You win")
    elif total_user_score < total_computer_score:
        print("Your total score is " + str(total_user_score) + " and the computer total score is " + str(total_computer_score) + ". Computer win")
    else:
        print("Your total score is " + str(total_user_score) + " and the computer total score is " + str(total_computer_score) + ". it is a tie")
else:
    print("Thanks for playing")


