# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

n = 100
sumS = 0
squareS = 0
for i in range(1, n+1):
	sumS += i**2

squareS = (n*(n+1)/2)**2
print(squareS - sumS)