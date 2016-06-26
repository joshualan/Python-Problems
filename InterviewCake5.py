  def find_combinations(denominations, amount):
    memo = {}
    
    def find(index, amt):
        curr = denominations[index]
        combinations = []
                    
        if ((index,amt) in memo):
            return memo[(index,amt)]
        
        if (curr > amt):
            memo[(index,amt)] = None
            return None
        elif (curr == amt):
            memo[(index,amt)] = [[curr]]
            return [[curr]]
        
        for i in range(index, len(denominations)):
            # First, try to find a sub-amount using the denomination
            # we're on as a base. Example, if amount is $4 and denom
            # is $1, then we try to find an sub-amount of $3 ($4-$1)
            curr = denominations[index]
            result = find(i, amt - curr)
             
            if result is not None:
                result = [[curr] + c for c in result]
                combinations.extend(result)
             
            # Then, try to find a full amount for everything past the
            # current denomination
            if (i > index):
                curr = denominations[i]
                result = find(i, amt - curr)
                
                if result is not None:
                    result = [[curr] + c for c in result]
                    combinations.extend(result)
            
        if (len(combinations) == 0):
            memo[(index,amt)] = None
            return None
        
        memo[(index,amt)] = combinations    
        return combinations
    
    print(find(0, amount))
    
find_combinations([1,2,3], 4)
