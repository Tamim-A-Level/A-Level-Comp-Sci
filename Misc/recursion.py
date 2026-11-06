# i=1
# while i <=10:
#     print(i)
#     i=i+1
def count(i):
    if i >1000000:
        return
    print(i)
    count(i+1)
count(1)