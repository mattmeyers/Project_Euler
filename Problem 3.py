# What is the largest prime factor of 600851475143?

num = 600851475143
factors = []

for x in range(2, num):
    while (num % x == 0 and num != 1):
        factors.append(x)
        num = num / x
    if num == 1:
        break


print(max(factors))