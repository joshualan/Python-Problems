input = [1, 10, -5, 1, -100]

def find_highest_product(list_of_ints):
    negatives = []
    
    highest_product = []
    
    highest_product.append(list_of_ints[0])
    
    sorted_insert(highest_product, list_of_ints[1])
    sorted_insert(highest_product, list_of_ints[2])
    
    if (list_of_ints[1] < 0):
        sorted_insert(negatives, list_of_ints[1])
    if (list_of_ints[2] < 0):
        sorted_insert(negatives, list_of_ints[2])
    
    for i in list_of_ints[3:]:
        if (i > 0 and i > highest_product[0]):
            # Insert the number into its rightful place and then remove
            # the smallest
            sorted_insert(highest_product, i)
            highest_product = highest_product[1:]
        elif (i < 0):
            sorted_insert(negatives, i)
            # Insert the number in its sorted place and remove the
            # highest number
            negatives = negatives[:2]
    
    # There's a chance that a product of negatives might be higher than the
    # lowest two positives so test for that
    product = highest_product[0] * highest_product[1] * highest_product[2]
    
    if (len(negatives) < 2):
        neg_product = 0
    else:
        neg_product = negatives[0] * negatives[1] * highest_product[2]
    
    if product < neg_product:
        return neg_product
    else:
        return product
    
    # Inserts an int into its proper place into an array of length 3 or less
def sorted_insert(lst, num):
    if (len(lst) == 0):
        lst.append(num)
    elif (num < lst[0]):
        lst.insert(0, num)
    elif (len(lst) > 1 and num < lst[1]):
        lst.insert(1, num)
    elif (len(lst) > 2 and num < lst[2]):
        lst.insert(2, num)
    else:
        lst.append(num)
        
print(find_highest_product(input))
