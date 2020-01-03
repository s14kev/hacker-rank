def findDigits(n):
    #convert to string then convert digits back to int (list)
    stringify = str(n)
    digitlist = []
    divisorsCounter = 0
    for element in stringify:
        if element != '0':
            digitlist.append(int(element))
    #check if each list element is divisor
    #if it is, add 1 to the number of divisors counter
    for digit in digitlist:
        if n % digit == 0:
            divisorsCounter = divisorsCounter + 1
    #return number of divisors counter
    return(divisorsCounter)

t = int(input())

for t_itr in range(t):
    n = int(input())
    result = findDigits(n)
    print(result)