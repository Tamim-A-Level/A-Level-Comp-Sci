

litre=11
print("Enter dimentions of the room in meters\n")
hight=int(input("Hight: "))
length=int(input("Length: "))
width=int(input("Width: "))
coats=int(input("How many coats do you want: "))
area_needed=2*(hight*length)+2*(hight*width)+(hight*width)
amount_of_paint=(area_needed/litre)*coats
print(amount_of_paint)


# this is a new
