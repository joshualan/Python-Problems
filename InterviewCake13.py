def find_rotation_point(lst):

	first = 0
	last = len(lst) - 1
	
	while first <= last:
		mid = (first + last) // 2

		# If the next point has a lesser value than the current one
		# (i.e. "zebra", "ask"), then we found our rotation point.

		next = 0 if mid == len(lst) - 1 else mid + 1

		if lst[mid] > lst[next]:
			return mid + 1
	
		# If the word at the middle is still less than the word at the end,
		# the rotation point is in the first half.
		if lst[mid] < lst[last]:
			last = mid
		else:
			first = mid

	# If we get over here, we didn't find it.
	return None

# Rotate the words to make sure it finds asymptote every time
def find_rotation_point_test(lst, rotation_word):
	for i in range(len(lst)):
		# rotate the list
		wrds = lst[i:] + lst[:i]

		assert lst[find_rotation_point(lst)] == rotation_word

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

words_even = words[:-1]

find_rotation_point_test(words, "asymptote")
find_rotation_point_test(words_even, "asymptote")
