def SumInverse(sum, numberLength):
    if sum == 0:
        return 1
    if sum == 0:
        return 0
    n = 10**numberLength
    numbers = []
    counter = 0
    for i in range(0,n):
        x = 0
        for digit in str(i):
            x = x + int(digit)
        if x == sum:
            numbers.append(str(i))
            counter += 1
    print(numbers)
    print(counter)
