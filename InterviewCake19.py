# So the funny thing is, I didn't get it. I did think of the solution at one
# point but I stumbled on the complexity. So the trick was to use the
# accounting method. This method is to find the order of something by finding
# the TOTAL cost of each item passing through the system, instead of the 
# operation itself. 

# So using this method, we have two stacks. Let's call one the in_stack
# and the out_stack. Every time we enqueue, we put it in the in_stack.
# When we dequeue for the first time, we put everything in the in_stack 
# in the out_stack. Since it's a stack, the out_stack will have it in the
# proper order! Whenever we dequeue again, we just pop it off the out_stack
# if it isn't empty. Otherwise, we empty the in_stack into the out_stack
# again. 

# How is this O(m)? Let's use the accounting method. Each item gets 1 push
# and 1 pop total! O(1) + O(1) = O(1)! If we have m items, we have O(m)
# total. How cool is that? 

# This trick is handy when we're looking at the cost for 'm' function calls 
# and not just one function call.
