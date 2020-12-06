import re
from collections import Counter

with open("input","r") as file:
	inputFile = file.read()
	split = re.split(r"(?:\r?\n){2,}", (inputFile))
	result = 0
	resultparttwo = 0
	for group in split:
		group = group.rstrip()
		participants = len(group.split('\n'))
		group = group.replace('\n','')
		combined = []
		dictionary = Counter(group)
		for key in dictionary:
			if(dictionary[key] == participants):
				combined.append(key)				
		result += len(set(group))
		resultparttwo += len(combined)
	print result
	print resultparttwo
