letter=input("Enter letter grade: ")
letter = letter.upper()
match letter:
    case "A**":
        print("Grade: 9")
    case "A*":
        print("Grade: 8")
    case "A":
        print("Grade: 7")
    case "B":
        print("Grade: 6")
    case "C":
        print("Grade: 5")
    case "D":
        print("Grade: 4")
    case "E":
        print("Grade: 3")
    case "F":
        print("Grade: 2")
    case "G":                        
        print("Grade: 1")
    case _:
        print("INVALID")