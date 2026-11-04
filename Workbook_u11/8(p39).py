def multiplication(table,startnum,endnum,pupilName):
    print("Hi, " + pupilName + " ... here is your times table")
    for i in range(startnum,endnum+1):
        print(i*table)

name=input("What is your name: ")
print("Enter times table, start number, and end number")
times=int(input())
start=int(input())
end=int(input())
multiplication(times,start,end,name)