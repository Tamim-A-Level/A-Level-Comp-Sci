#bubble sort compairs the first two numbers and switches the order if the first is smaller than the second after it checks then it move on. By the end of the first cycle the biggest number is at the end . multiple cycles might be needed 



numbers=[10,2,12,7,5]
switch=True
while switch:
    switch=False
    for i in range(len(numbers)-1):
                

        if numbers[i] > numbers[i+1]:
            a=numbers[i+1]
            numbers[i+1]=numbers[i]
            numbers[i]=a
            print(numbers)
            switch=True
 




