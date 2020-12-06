import re
import math
	
def find_my_seat(seats): 
    return [x for x in range(seats[0], seats[-1]+1)  
                               if x not in seats] 

with open("input","r") as file:
	inputFile = file.read().splitlines()
	highestValue = 0
	seats = []
	for seat in inputFile:
		row = int(seat[0:7].replace("F","0").replace("B","1"),2)
		column = int(seat[7:].replace("L","0").replace("R","1"),2)
		result = row * 8 + column
		seats.append(result)
		if(result > highestValue):
			highestValue = result
	print highestValue
	seats.sort()
	print find_my_seat(seats)[0]
