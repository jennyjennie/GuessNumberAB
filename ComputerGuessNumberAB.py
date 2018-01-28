# Author: Jenny Ho, 2018/1/28
# This program guesses the secret number thought by the users.

import random

N = 4 # Number of digits to be guessed.

def ConvertIntToList(n):
	# Turn a given number to a list. ex: return [1, 2, 3, 4] for n = 1234.
	digits = []
	while n > 0:
		d = (n % 10)
		digits.insert(0, d)
		n = n // 10
	return digits

def HasDuplicateItem(digits):
	# Check if there is any duplicate item in a list. ex: return True when digits = [1, 1, 2, 3] 
	for i in range(len(digits)):
		n = digits[i]
		removed = digits[:i] + digits[i+1:]
		if n in removed:
			return True
	return False
			
def GenerateAllDigits(n):
	# Generate all possible lists of digits for the given number of digits n. 
	# Neither duplicate items nor 0 exists in each list.
	dRange = {2: (12, 98), 3:(123, 987), 4:(1234, 9876), 5:(12345, 98765),
			  6:(123456, 987654), 7:(1234567, 9876543), 8:(12345678, 98765432), 9:(123456789, 987654321)}
	if n not in dRange:
		return []
	start, end = dRange[n]
	i = start
	allDigits = []
	while i <= end:
		digits = ConvertIntToList(i)
		if 0 not in digits and not HasDuplicateItem(digits):
			allDigits.append(digits)
		i += 1
	return allDigits

def MatchDigits(guess, answer):	
	# Find the matching results for the given two lists of digits. 
	# We need to find out 2 matching results. One is same digits at the same positions (denoted as 'A'),
	# and the other at different position (denoted as 'B').
	a = 0
	for i in range(len(guess)):
		if guess[i] == answer[i]:
			a += 1
	n = 0
	for i in range(len(guess)):
		if guess[i] in answer:
			n += 1
	b = n - a
	return (a, b)		

# Main program. 	
possibleDigits = GenerateAllDigits(N)

# Loop until there is only one item left in the list of possible digits.
while len(possibleDigits) > 1:
	# Pick the first digits as a guess.
	guess = possibleDigits[0]
	print('Computer guess: ', guess)
	# Remove the guess from the list of possible digits. 
	del possibleDigits[0]
	# Ask the users to input the matching result (number of A and B).
	s = input("Tell me AB: ")
	a, b = int(s[0]), int(s[1])
	# The following loop removes the items not having the same A and B when matching against the guess.
	newDigits = []
	for item in possibleDigits:
		if MatchDigits(guess, item) == (a, b):
			newDigits.append(item)
	possibleDigits = newDigits	
	
# Show the result.	
print('The answer is', possibleDigits[0])		

