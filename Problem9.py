# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# We can use Euclid's formula to avoid brute forcing the solution.  For m>n>0, let a=m^2-n^2, b=2mn, and c=m^2+n^2.  Plug this into the given equation a+b+c=1000 to get m^2+nm-500=0.  Using the discriminant shows that any n will satisfy this equation, so I guessed n=5 and got lucky.  Solving the quadratic gave m=20.  Hence, a=375, b=200, and c=425.
#
# TODO: Figure out why n=5

print(375*200*425)
