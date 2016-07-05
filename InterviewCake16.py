import math

def max_duffel_bag_value(cake_tuples, capacity):
	
	# Check for a cake with a weight of 0 because that means infinite value
	for cake_weight, cake_value in cake_tuples:
		if cake_weight == 0 and cake_value > 0:
			return math.inf

	memo = {0: 0}

	# Recursive function that'll use the memo to save calculation
	def find_max_value(capacity):
		if capacity in memo:
			return memo[capacity]

		max_value = 0

		for cake_weight, cake_value in cake_tuples:
			# If this cake is less than the capacity, its a potential steal!
			if cake_weight <= capacity:
				max_value = max(
					max_value, 
					cake_value + find_max_value(capacity-cake_weight))

		memo[capacity] = max_value
		return max_value

	return find_max_value(capacity)

assert max_duffel_bag_value([(0,150), (1,300), (4,50)],200) == math.inf
assert max_duffel_bag_value([(3, 40), (5,70)],9) == 120	
