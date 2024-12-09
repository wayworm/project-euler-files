# Power Digit Sum
# 2^15 = 32768
#The sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#What is the sum of the digits of 2^1000

#Simple problem, but of a technical hiccup, if you use numpy you get an overflow error for high exponent values,

#default python power operation doesn't have this problem.

val = 2**1000

sum = 0
#print(val)
for i in str(val):
    sum += int(i)

print(sum)