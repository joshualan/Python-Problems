# A memoizer for the Fibonacci stuff!
memo = {0: 0, 1: 1, 2: 1, "largest": 2}

def find_fib(n):
	if n in memo:
		return memo[n]
	else:
		# Start the calculation from largest to save some cycles
		curr = memo["largest"] + 1

		while curr <= n:
			memo[curr] = memo[curr-1] + memo[curr-2]
			curr += 1

		memo["largest"] = n
		return memo[n]

assert find_fib(20) == 6765
assert find_fib(30) == 832040
