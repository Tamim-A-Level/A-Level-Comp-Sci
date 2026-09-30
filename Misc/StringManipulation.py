text = "Computer Science"
print(len(text))
# 16

print(text[0])
# C

print(text[-1])
# e

print(text[0:8])
# Computer

firstName = "Alex"
lastName = "Smith"

fullName = firstName + " " + lastName
print(fullName)
# Alex Smith

print(text.upper())
# COMPUTER SCIENCE

print(text.lower())
# computer science

if "Science" in text:
    print("Found")

position = text.find("Science")
print(position)
# 9

newText = text.replace("Science", "Studies")
print(newText)
# Computer Studies

username = "  alex123  "
print(username.strip())
# alex123

message = "banana"
print(message.count("a"))
# 3

password = "abc123"

print(password.isalpha())
# False

print(password.isdigit())
# False

print("abc".isalpha())
# True

print("123".isdigit())
# True

postcode = input("Enter your postcode: ")

if len(postcode) == 6:
    print("Valid length")
else:
    print("Invalid length")