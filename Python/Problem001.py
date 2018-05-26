'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Deterime if the number is a multiple of multiple.
def is_multiple(number, multiple):
	return number % multiple == 0



# Find sum
limit = 1000
sum = 0
for i in range(1, limit):
	if is_multiple(i, 3) or is_multiple(i, 5):
		sum += i

print(sum)