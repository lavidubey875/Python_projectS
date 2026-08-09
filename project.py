import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr =input("enter thr choice:").strip().upper()
youDict ={"S":1,"W":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"Gun"}
you = youDict[youstr]

print(f"You chose {dict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("Draw")


else:
    if(computer==-1 and you==1):
     print("you Win!")

    elif(computer==-1 and you==0):
     print("You lose!")

    elif(computer== 1 and you==-1):
     print("You lose!")

    elif(computer==0 and you==-1):
     print("You Win!")   

    elif(computer==0 and you==1):
     print("you Lose!")

    else:
     print("something went wrong")    