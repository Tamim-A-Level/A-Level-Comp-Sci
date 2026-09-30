def bubblesortscore():

    swap=True
    while swap:
        swap=False
        for i in range(len(scores)-1):
                    

            if scores[i] > scores[i+1]:
                a=scores[i+1]
                c=football_teams[i+1]
                scores[i+1]=scores[i]
                football_teams[i+1]=football_teams[i]
                scores[i]=a
                football_teams[i]=c
                swap=True
    for i in range(len(scores)):
        print(football_teams[i]+" has "+str(scores[i])+" points")

def bubblesortnames():

    swap=True
    while swap:
        swap=False
        for i in range(len(scores)-1):
                    

            if football_teams[i] > football_teams[i+1]:
                a=football_teams[i+1]
                c=scores[i+1]
                football_teams[i+1]=football_teams[i]
                scores[i+1]=scores[i]
                football_teams[i]=a
                scores[i]=c
                swap=True
    for i in range(len(scores)):
        print(football_teams[i]+" has "+str(scores[i])+" points")

football_teams=["Manchester United","Bournemouth","Birmingham City","Bradford City","Aston Villa","Barnsley","Arsenal","Blackburn Rovers","Blackpool","Bolton Wanderers"]
scores=["","","","","","","","","",""]
winningt=""
winnings=0
for i in range(len(scores)):
    point=int(input("How many points does "+football_teams[i]+" have: "))
    scores[i]=point

    print((football_teams[i])+" has "+str(scores[i])+" points.")
    print("")
for i in range(len(football_teams)):
    if scores[i] > winnings:
        winningt=football_teams[i]
        winnings=scores[i]
print("")
print("The team with the highest score is "+winningt+ " with "+str(winnings)+ " points.")

start=int(input("\nHow would you like it sorted\nBy points(1)\nBy Names(2)\nExit(3)\n:"))
end=0
while end==0:
    if start== 1:
        bubblesortscore()
    elif start== 2:
        bubblesortnames()
    else:
        end=-1
        print("Bye")
