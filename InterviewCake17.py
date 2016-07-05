# This isn't a python problem but the point is that declarations are hoisted
# to the top of Javascript functions. This means that if you declare a variable
# and assign it after you try using it, you will get 'undefined'. We found it's
# declaration below the page but the assignment doesn't get hoisted so we know
# it exists but not what it is.
