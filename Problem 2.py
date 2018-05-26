# Find the sum of the even terms in the Fibonacci Sequence less than four million.

# Solution 1
fibNum1 = 1
fibNum2 = 2
fibNum3 = fibNum1 + fibNum2
sum = 2

while fibNum3 < 4000000:
    if (fibNum3 % 2 == 0):
        sum += fibNum3
    fibNum1 = fibNum2
    fibNum2 = fibNum3
    fibNum3 = fibNum1 + fibNum2

print(sum)
