def condense_meeting_times(lst):
    lst = [list(block) for block in lst]
    sorted_list = binary_sort(lst)
    return condense_lst(sorted_list)
    

def condense_lst(lst):
    condensed = list(lst)
    i = 0
    maximum = len(lst) - 1
    
    while(i < maximum):
        curr = condensed[i]    
        nxt = condensed[i+1]
        
        while (nxt and hasOverlap(curr, nxt)):
            curr[0] = min(curr[0], nxt[0])
            curr[1] = max(curr[1], nxt[1])
            del condensed[i+1]
            maximum -= 1
            if (i < maximum):
                nxt = condensed[i+1]
            else:
                nxt = None
            
        i += 1

    return condensed
            
# Do a binary sort which is an n*log(n) 
def binary_sort(lst):
    sorted_list = [list(lst[0])]
    
    for block in lst[1:]:
        i = binary_search(sorted_list, block)
        curr = sorted_list[i] 
                
        if (curr[1] < block[1]):
            sorted_list.insert(i, block)
        else:
            sorted_list.insert(i + 1, block)
            
    return sorted_list

# A helper function that calls the actual binary search
# function.
def binary_search(lst, meeting):
    return bsrch(lst, meeting, 0, len(lst) - 1)

# Binary search function that returns the index of where
# to insert/edit the entry
def bsrch(lst, block, min, max):
    curr = int((min + max) / 2) 
    
    if (hasOverlap(lst[curr], block) or 
        min == max):        
        return curr

    if (lst[curr][1] > block[1]):
        return bsrch(lst, block, min, curr-1)
    else:
        return bsrch(lst, block, curr+1, max)

def hasOverlap(block1, block2):
    
    if (block1[0] <= block2[0] <= block1[1] or
        block1[0] <= block2[1] <= block1[1] or
        block2[0] <= block1[0] <= block2[1] or
        block2[0] <= block1[1] <= block2[1]):
        return True
    
    return False

# condensed = [(0, 1), (3, 8), (9, 12)]
input1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# condensed = [(1, 10)]
input2 =  [(1, 10), (2, 6), (3, 5), (7, 9)]

print(condense_meeting_times(input1))
