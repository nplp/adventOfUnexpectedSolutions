import numpy

def search_backwards(jolts,previousIndex,forks):
	tempForks = 0
	if(previousIndex -1 >= 0 and jolts[previousIndex] - jolts[previousIndex-1] in range(1,4)):
		tempForks +=1
	if(previousIndex -2 >= 0 and jolts[previousIndex] - jolts[previousIndex-2] in range(1,4)):
                tempForks +=1
	if(previousIndex -3 >= 0 and jolts[previousIndex] - jolts[previousIndex-3] in range(1,4)):
                tempForks +=1	
	if(tempForks == 0):
		tempForks +=1
	forks.insert(0,tempForks)



def calculate_island(startIndex, endIndex, forks):
	strrr = ""
	for value in forks[startIndex:endIndex]:
		strrr = strrr +	str(value) + " "
	return strrr


with open("input","r") as file:
	jolts = [int(l) for l in file.read().splitlines()]
	jolts.sort()
	deviceJolts = jolts[len(jolts)-1] + 3
	jolts.append(deviceJolts) 
	joltDiff1 = 0
	joltDiff2 = 0
	joltDiff3 = 0
	previous = 0
	combinations = []
	forks = []
	for jolt in jolts:
		if(jolt - previous == 1):
			joltDiff1 += 1
			previous = jolt
		if(jolt - previous == 2):
			joltDiff2 += 1
			previous = jolt
		if(jolt - previous == 3):
			joltDiff3 +=1
			previous = jolt


	print joltDiff1*joltDiff3
	jolts.insert(0,0)
	for i in reversed(xrange(len(jolts))):
		search_backwards(jolts,i,forks)
		
	result = 1
	islandStartIndex = -1
	islandEndIndex = -1
	for index,num in enumerate(forks):
		if(num != 1 and islandStartIndex == -1 and forks[index-1] == 1):
			islandStartIndex = index
			for index2 in range(index+1,len(forks)):
				if(forks[index2] == 1 or index2 == len(forks)-1):
					islandEndIndex = index2
					island_value = calculate_island(islandStartIndex,islandEndIndex,forks)
					if(island_value == "2 3 3 "):
						result *= 7
					if(island_value == "2 3 "):
						result *= 4
					if(island_value == "2 "):
						result *= 2
					break
		islandStartIndex = -1
		islandEndIndex = -1
	print result

