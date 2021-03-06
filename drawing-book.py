import os
import sys
#d2b0n

def pageCount(n, p):
    turnFront = p // 2
    answer = []
    answer.append(turnFront)

    if numPages % 2 == 1:
        turnBack = (n - p) // 2
        answer.append(turnBack)

    elif n == p:
        turnBack = 0
        answer.append(turnBack)

    else:
        turnBack = 1 + (n - p - 1) // 2
        answer.append(turnBack)

    return min(answer)


numPages = int(input())

targetPage = int(input())

result = pageCount(numPages, targetPage)

print(result)