# This is a binary search!

def binary_search(lst, num):

	first = 0
	last = len(lst) - 1

	while first <= last:
		# The two slashes represent integer division
		# One slash returns a float regardless!
		midpoint = (first + last) // 2

		if lst[midpoint] == num:
			return midpoint
		elif num < lst[midpoint]:
			last = midpoint - 1
		else:
			first = midpoint + 1

	# If we get over here, we didn't find it.
	return None
