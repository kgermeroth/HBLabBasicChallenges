# First day coding challenges

def find_range(nums):
	""" Takes a list of numbers, returns the smallest and largest number """

	num_min = None
	num_max = None

	if nums == []:
		pass

	elif len(nums) == 1:
		num_min = nums[0]
		num_max = nums[0]

	else:
		num_min = min(nums)
		num_max = max(nums)

	return (num_min, num_max)


def fizzbuzz():
	""" Counts from 1 to 20 in fizzbuzz fashion.

	Loops through 1 - 20. If number is divisible by 3, say 'fizz'.
	If number divisible by 5, say 'buzz'. Divisible by both, say 'fizzbuzz'.
	Otherwise say the number. """

	for num in range(1,21):
		if num%3 == 0 and num%5 == 0:
			print("fizzzbuzz")

		elif num%3 == 0:
			print("fizz")
	
		elif num%5 == 0:
			print("buzz")

		else:
			print(num)


def find_longest_word(words):
	""" Returns the length of the longest word in a list of words"""

	longest_word_length = 0

	for word in words:
		if len(word) > longest_word_length:
			longest_word_length = len(word)

	return longest_word_length


def decode(s):
	""" Decodes a string to reveal secret message.

	Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

	For example:

	>>> decode('0h1ae2bcy')
	'hey'

	"""


	secret_word = ""

	for idx, char in enumerate(s):
		if char.isdigit():
			secret_idx = idx + 1 + int(char)
			secret_word += s[secret_idx]

	return secret_word


# run doc tests
if __name__ == "__main__":
	import doctest

	result = doctest.testmod()

	if result.failed == 0:
		print("All tests passed! :)")