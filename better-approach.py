def fun2(sum, numberLength):
    
    if sum == 0:
        return 1
    if numberLength == 0:
        return 0
    if sum > int(numberLength)*9:
        return 0
   
    num = 0
 
    for i in range(0, 10) :
        if (sum-i >= 0) :
            num = num + fun2(sum-i, numberLength-1)

    print(num)
