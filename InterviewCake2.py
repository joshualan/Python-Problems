# Interview Cake Question 2
# Author's Note: these are pretty fun trying to get it to O(n)

def get_products_of_all_ints_except_at_index_n2(integers):
    # Create the result list with a default value of 1 in it.
    products = [1] * len(integers)
    
    # Iterate through the list and multiply each number in products by
    # the every number
    for idx1, val1 in enumerate(integers):
        products = [val1 * val2 if idx1 != idx2 else val2 for idx2, val2 in enumerate(products)]
        
    return products
    
def get_products_of_all_ints_except_at_index(integers):
    # Create a two arrays: one containing the products after an index
    # and one containing the products before an index
    products = [1] * len(integers)
    
    product = integers[0]
    
    for index, val in enumerate(integers):
        if index == 0:
            continue
            
        products[index] *= product
        product *= val
            
    product = integers[-1]    
    for index, val in enumerate(integers[::-1]):
        index = len(integers) - 1 - index
        
        if index == (len(integers) - 1):
            continue
        
        products[index] *= product
        product *= val
        
    return products
        
print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))

print(get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9]))
