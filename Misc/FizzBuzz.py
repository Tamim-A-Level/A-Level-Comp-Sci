def prime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

count = int(input("Enter the count: "))
Fizz = int(input("Enter the Fizz number: "))
Buzz = int(input("Enter the Buzz number: "))

for i in range(1, count + 1):
    if prime(i):
        print("OOPS")
    elif i % Fizz == 0 and i % Buzz != 0:
        print("Fizz")
    elif i % Fizz != 0 and i % Buzz == 0:
        print("Buzz")
    elif i % Fizz == 0 and i % Buzz == 0:
        print("FizzBuzz")
    else:
        print(i)

        
