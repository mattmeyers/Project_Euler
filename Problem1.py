# Find the sum of all the multiples of 3 and 5 below 1000.

# Solution 1
sumA = 0
sumB = 0
sumC = 0

cardA = 999 // 3
cardB = 999 // 5
cardC = 999 // 15

for x in range(0, cardA):
    sumA += (3 + x*3)


for x in range(0, cardB):
    sumB += (5 + x*5)

for x in range(0, cardC):
    sumC += (15 + x*15)

print(sumA + sumB - sumC)

# Solution 2
sum = 0
for x in range(1, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum += x
print(sum)

