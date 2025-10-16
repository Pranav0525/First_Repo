import random

computer = random.choice([1, 0, -1])
you = input("Enter you choice:  ").lower()
you = you.replace(" ", "")
youDict = {"rock" : 1, "scissor" : 0, "paper" : -1}
reverseDict = {1 : "rock", 0 : "scissor", -1 : "paper"}
younum=youDict[you]

print(f"You chose {reverseDict[younum]}\n Computer chose {reverseDict[computer]}")

if (computer == younum):
    print("It's a Draw!")
else:   
    if (computer == -1 and younum == 1):
        print("YOU LOSE!")
    elif (computer == -1 and younum == 0):
        print("YOU WIN!")
          
    elif (computer == 1 and younum == -1):
        print("YOU WIN!")
    elif (computer == 1 and younum == 0):
        print("YOU LOSE!")
          
    elif (computer == 0 and younum == 1):
        print("YOU WIN!")   
    elif (computer == 0 and younum == -1):
        print("YOU LOSE!")
          
    else:
        print("Something Went Wrong  T_T")