# Interview Cake Question 1

# O(N^2) Solution
def get_max_profit_n2(stock_prices):
	max_profit = None
	
	for idx, val1 in enumerate(stock_prices):
		# Create a duplicate list without the current value
		for val2 in stock_prices[idx+1:]:
			profit = val2 - val1
			if max_profit is None or profit > max_profit:
				max_profit = profit 
	
	return max_profit
			
# O(N) Solution
def get_max_profit(stock_prices):
	lowest_price = stock_prices[0]
	max_profit = None
	
	for current_price in stock_prices[1:]:
		lowest_price = min(lowest_price, current_price)
			
		profit = current_price - lowest_price
		if max_profit is None or profit > max_profit:
			max_profit = profit
	
	return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices_yesterday))
