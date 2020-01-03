def jumpingOnClouds(c):
    #create a count jumps variable
    countJumps = 0
    index = 0
    #if can jump by 2, do that, otherwise jump by 1 and add jump to counter while not at the end yet
    while index != len(c) - 1:
        if c[index + 2] != 1 and index + 2 <= len(c) - 1:
            index = index + 2
            countJumps = countJumps + 1
        else:
            index = index + 1
            countJumps = countJumps + 1
    return countJumps

n = int(input())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)
print(result)