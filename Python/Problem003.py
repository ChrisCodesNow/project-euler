'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt, floor

def is_factor(number, factor):
	return number % factor == 0

# Recursively get max prime factor of the number
def max_prime_factor(number):

	factors = set()	# store all factors

	# GET ALL FACTORS FROM 1 TO SQRT(NUMBER)
	max_possible_factor = floor(sqrt(number))
	for i in range(1, max_possible_factor + 1):
		if(is_factor(number, i)):
			factor1 = i
			factor2 = number / i
			
	print(sorted(factors))

	# GET RID OF EVEN NON-PRIME FACTORS


# MAIN
print(max_prime_factor(100))		