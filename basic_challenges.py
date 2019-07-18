# Find the range
# def find_range(nums):
#     num_min = None
#     num_max = None

#     if nums == []:
#         pass
#     elif len(nums) == 1:
#         num_min = nums[0]
#         num_max = nums[0]
#     else:
#         num_min = min(nums)
#         num_max = max(nums)

#     return (num_min, num_max)

# print(find_range([5]))

# #FizzBuzz
# def fizzbuzz():
#     for num in range(1,21):
#         if num%3 == 0 and num%5 == 0:
#             print("fizzbuzz")
#         elif num%3 == 0:
#             print("fizz")
#         elif num%5 == 0:
#             print("buzz")

#         else:
#             print(num)

# # fizzbuzz()

# def find_longest_word(words):
#     longest_word_length = 0
#     for word in words:
#         if len(word) > longest_word_length:
#             longest_word_length = len(word)
#     return longest_word_length

# print(find_longest_word(["Balloonicorn", "Hackbright","Supercalifragilid"]))

#decorder
# A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

# Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

# For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

def decode(s):
    secret_word = ""

    for idx, char in enumerate(s):
        if char.isdigit():
            secret_idx = idx + 1 + int(char)
            secret_word += s[secret_idx]

    return secret_word

print(decode("0h1ae2bcy"))