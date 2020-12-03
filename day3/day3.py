import numpy
with open("input","r") as file:
	input = file.read().splitlines()
	moveX = [1,1,1,1,2]
	moveY = [1,3,5,7,1]
	result = [0,0,0,0,0]
	maxYIndex = len(input[0]) - 1
	maxXIndex = len(input) -1
	i = 0	
	while i < len(moveX):
		x = 0
		y = 0
		while (1==1):
			x+=moveX[i]
			y+=moveY[i]
			if(y > maxYIndex):
				y = y-maxYIndex-1
			if(x > maxXIndex):
				break
			if(input[x][y] == "#"):
				result[i] += 1
		i +=1
	print result[1]
	print numpy.prod(result)
