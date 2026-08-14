'''
0 for rock
1 for paper
2 for scissor
'''
import random
computer = random.choice([0,1,2])
youstr = input("enter your choice:")
youDict = {"r":0 , "p":1 , "s":2}
reversedict = {0 :"rock" , 1 : "paper" , 2: "scissor"}
you = youDict[youstr]
print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(computer==you):
    print("its a draw")
else:
    if(computer==0 and you==1):
        print("you win")
    elif(computer==0 and you==2):
        print("you loose")
    elif(computer==1 and you==0):
        print("you loose")
    elif(computer==1 and you==2):
        print("you win")
    elif(computer==2 and you == 0):
        print("you win")
    elif(computer==2 and you==1):
        print("you lose")
    
    
