print("""Which car do you want:
1:Economy
2:Saloon
3:Sports
""")
answer=input()
if answer == "1" or answer == "2" or answer == "3":
    answer2=input("Do you wish to continue(y/n)")
    if answer2.lower() == "y":
        print("confirmed")
    else:
        print("Bye")
else:
    print("Invalid")