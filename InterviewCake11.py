import collections

# So this works as an arbitrarily-nested default dict because 
# the defaultdict constructor accepts a function that it calls
# whenever the key is not present in the dict. 
def nested_dict():
	return collections.defaultdict(nested_dict)

# Store a web page as a recursive dictionary structure
visited = nested_dict()

# The * signifies the end of the url
def store_url(url):
	d = visited
	for c in url:
		d = d[c]

	d['*'] = True

store_url("abcd")

print(visited['a']['b']['c']['d']['*'])
