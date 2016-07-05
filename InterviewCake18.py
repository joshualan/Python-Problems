# So the thing with this is that we're returning a function that uses closures.
# Now, the weird thing with closures is that it tries to access the variable,
# not the value. So since the int in the for loop was removed, we no longer 
# have access to it and its undefined.
