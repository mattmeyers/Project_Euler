# What is the 10 001st prime number?

curNum = 3
primeList = [2]
while (len(primeList) < 10001):
    composite = False
    for i in primeList:
        if (curNum % i == 0):
            composite = True
            break

    if (composite == False):
        primeList.append(curNum)

    curNum += 2

print(primeList[-1])
