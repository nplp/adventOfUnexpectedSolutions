import re

class resultclass:
	correctColors = []

class node:
	def __init__(self,name,children):
		self.id = id
		self.children = children
		self.visited = false
	def visit():
		self.visited = true
		#if(self.id == 'shiny gold'):
		#	return true
		#elif(self.children != null):
		#	for(child in self.children):
		#		result = child.visit()
		#		if(result == True):
		#			correctcolors.append(self.id)		
		#else:
		#	return False


with open("sample","r") as file:
	allrules = file.read().splitlines()
	rules = {}

	for rule in allrules:
		parts = rule.split('bags contain')
		part1 = parts[0].strip()
		parts2 = parts[1]
		rules[part1] = []
		for part in parts2.split(','):
			extract = re.sub('^([^a-z]*)',"", part)
			extract = extract.rstrip(' bag.')
			extract = extract.rstrip(' bags.')
			rules[part1].append(extract)
	
	#tuples = [(k, v) for k, v in rules.items()] 
  	tuples = []
	for k in rules.keys():
		if(len(rules.get(k)) != 1):
			tuples.append(rules.get(k))

	print tuples
	graph = {name: set() for tup in tuples for name in tup}
	has_parent = {name: False for tup in tuples for name in tup}
	for parent, child in tuples:
    		graph[parent].add(child)
    		has_parent[child] = True

	# All names that have absolutely no parent:
	roots = [name for name, parents in has_parent.items() if not parents]

	 #traversal of the graph (doesn't care about duplicates and cycles)
	def traverse(hierarchy, graph, names):
    		for name in names:
       			hierarchy[name] = traverse({}, graph, graph[name])
    			return hierarchy

