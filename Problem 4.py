# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPal(num):
	if (len(num) == 1):
		return True

	if(num[0] != num[-1]):
		return False
	else:
		if(len(num) == 2):
			return True
		num = num[1:-1]
	return checkPal(num)

def main():
	maxX = maxY = maxPal = 0
	x = 999
	y = 999

	while(x > 99):
		while(y > 99):
			prod = x*y
			if(checkPal(str(prod)) and prod > maxPal):
				maxX = x
				maxY = y
				maxPal = prod
			y -= 1
		x -= 1
		y = x
	print("{} is the product of {} and {}".format(maxPal,maxX,maxY))

main()