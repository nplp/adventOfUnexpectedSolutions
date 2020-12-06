import re
import math
	
with open("input","r") as file:
	inputFile = file.read().splitlines()
	maxRow = 127
	maxColumn = 7
	highestValue = 0
	seats = [["free" for i in range(8)] for j in range(128)]
	print seats
	for seat in inputFile:
		top = 127
		bottom = 0
		right = 7
		left = 0
		for symbol in seat:
			print "symbol:" + symbol
			if(symbol == "B"):
				bottom += int(math.ceil(float(top - bottom)/2))
			elif (symbol == "F"):
				top -= int(math.ceil(float(top - bottom)/2))
			elif (symbol == "L"):
				right -= int(math.ceil(float(right - left)/2))
			elif (symbol == "R"):
				left += int(math.ceil(float(right - left)/2))
			print "top: "+ str(top)
			print "bottom: "+ str(bottom)
			print "right: "+ str(right)
			print "left: "+ str(left) 	
		result = 8 * bottom + left
		seats[bottom][left] = "taken"
		if(result > highestValue):
			highestValue = result
	print highestValue
