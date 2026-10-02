value = int(input ("Enter order value: "))
price = 5.00
print ("Do you want to pay £5.00 for next day delivery? ")
postageCode = input("""
Enter 1 for next day delivery
Enter 2 for 2nd class post
""")

if value >= 15 and postageCode == 2 :
    postageCharge = 0
else:
    if value < 15 and postageCode == 2 :
        postageCharge = 3.50

totalCharge = value + postageCharge
print (postageCharge, totalCharge)