def findDigits(n):
    #convert to string then convert digits back to int (list)
    #check if each list element is divisor
    #if it is, add 1 to the number of divisors counter
    #return number of divisors counter

t = int(input())

for t_itr in range(t):
    n = int(input())
    result = findDigits(n)
    print(result)