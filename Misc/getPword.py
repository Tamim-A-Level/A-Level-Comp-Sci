def getPword(attempt):
    global double
    if attempt == 1:
        p=input("Enter your password: ")
        if len(p)>8 or len(p)<6:
            double=p
            getPword(2)
        else:

double=""
getPword(1)
