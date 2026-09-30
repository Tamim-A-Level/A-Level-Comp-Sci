"""
Create a program that retrieves the membership details for a Rock Climbing Club. 
The program should take a range of details and then repeat them back, with headings, for
confirmation. 
Firstname, surname, age, rock climbing level (L1,L2,L3)
Once confirmed, the program stores these details; otherwise, it clears them and allows a new input.
Extensions: 
1. Allow entry of more than one membership 
2. Store membership details to a file 
3. Retrieve details from a file 
4. Allow searching for stored users
"""

def new():
    fname=input("Enter first name: ")
    sname=input("Enter second name: ")
    level=(input("Level(L1,L2,L3): "))
    age=int(input("Enter age: "))
    if age <=15 :
        print("You are to young")

    else:
        filename=fname+sname
        a=open(filename+".txt","a")
        a.write(fname+" "+sname+" ,"+level+", you are "+str(age))



def notnew():
    fname=input("Enter first name: ")
    sname=input("Enter second name: ")
    filename=fname+sname
    a=open(filename+".txt","r")
    print(a.readline())
b=input("Do you have an acount(Y/N):")
if b.lower()=="y":
    notnew()
else:
    new()
