# def addnumbers(numbers):
#     sum=0
#     for i in range(len(numbers)):
#         sum=sum+numbers[i]
#     return sum
# marks=[3,6,2,8,1]
# total=addnumbers(marks)
# print(total)

def addnumbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0]+addnumbers(numbers[1:])

marks=[3,6,2,8,1]
total=addnumbers(marks)
print(total)