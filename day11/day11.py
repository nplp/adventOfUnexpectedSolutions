def empty_to_occupied(x,y,seats):
	minX = x-1
	maxX = x+1
	if minX <= 0:
		minX = 0
	if maxX >= len(seats[0]):
		maxX = len(seats[0])-1
	minY = y-1
	maxY = y+1
	if minY <= 0:
		minY = 0
	if maxY >= len(seats):
		maxY = len(seats)-1
	for checkX in range(minX,maxX+1):
		for checkY in range(minY,maxY+1):
			if seats[checkY][checkX] == '#':
				return False		
	return True

def occupied_to_empty(x,y,seats):
 	minX = x-1
	maxX = x+1
        if minX <= 0:
                minX = 0
        if maxX >= len(seats[0]):
                maxX = len(seats[0])-1
        minY = y-1
	maxY = y+1
        if minY <= 0:
                minY = 0
        if maxY >= len(seats):
                maxY = len(seats)-1
       	numberOfOccupied = 0
        for checkX in range(minX,maxX+1):
        	for checkY in range(minY,maxY+1):
			if seats[checkY][checkX] == '#':
				numberOfOccupied +=1
                                if numberOfOccupied > 4:
					return True                
        return False


def empty_to_occupied2(x,y,seats):
	symbols = []
	symbols.append(left(x,y,seats))
	symbols.append(leftUp(x,y,seats))
	symbols.append(up(x,y,seats))
	symbols.append(rightUp(x,y,seats))
	symbols.append(right(x,y,seats))
	symbols.append(rightDown(x,y,seats))
	symbols.append(down(x,y,seats))
	symbols.append(leftDown(x,y,seats))
	
	for symbol in symbols:
		if symbol == '#':
			return False
	return True

def occupied_to_empty2(x,y,seats):
        symbols = []
        symbols.append(left(x,y,seats))
        symbols.append(leftUp(x,y,seats))
        symbols.append(up(x,y,seats))
        symbols.append(rightUp(x,y,seats))
        symbols.append(right(x,y,seats))
        symbols.append(rightDown(x,y,seats))
        symbols.append(down(x,y,seats))
        symbols.append(leftDown(x,y,seats))

	num = 0
        for symbol in symbols:
                if symbol == '#':
			num +=1
	if num > 4:
		return True             

        return False



def left(x,y,seats):
	for checkX in reversed(range(0,x)):
		if checkX == 90:
			print checkX
		if seats[y][checkX] == '#':	
			return '#'
		elif seats[y][checkX] == 'L':
			return 'L'
	return '.'

def right(x,y,seats):
        for checkX in range(x+1,len(seats[0])):
                if seats[y][checkX] == '#':
                        return '#'
                elif seats[y][checkX] == 'L':
                        return 'L'
        return '.'

def up(x,y,seats):
        for checkY in reversed(range(0,y)):
                if seats[checkY][x] == '#':
                        return '#'
                elif seats[checkY][x] == 'L':
                        return 'L'
        return '.'

def down(x,y,seats):
        for checkY in range (y+1,len(seats)):
                if seats[checkY][x] == '#':
                        return '#'
                elif seats[checkY][x] == 'L':
                        return 'L'
        return '.'

def leftUp(x,y,seats):
	hej = True
	while(hej):
		x = x-1
		y = y-1
		if(x < 0 or y < 0):
			break
		if seats[y][x] == '#':
            		return '#'
                elif seats[y][x] == 'L':
                        return 'L'
        		
	return '.'

def rightUp(x,y,seats):
        hej = True
        while(hej):
		x = x+1
		y = y-1
                if(x >= len(seats[0]) or y < 0):
                        break
                if seats[y][x] == '#':
                	return '#'
                elif seats[y][x] == 'L':
                	return 'L'
                
        return '.'


def rightDown(x,y,seats):
        hej = True
        while(hej):
		x = x+1
		y = y+1
                if(x >= len(seats[0]) or y >= len(seats)):
                        break
                if seats[y][x] == '#':
                        return '#'
                elif seats[y][x] == 'L':
                        return 'L'
                
        return '.'

def leftDown(x,y,seats):
        hej = True
        while(hej):
                x = x-1
		y = y+1
		if(x < 0 or y >= len(seats)):
                        break
                if seats[y][x] == '#':
                	return '#'
                elif seats[y][x] == 'L':
                        return 'L'
                
        return '.'



def isArrayFullOfFalse(arr):
	for x in arr:
		for y in x:
			if y == True:
				return False
	return True
		

def arrayFullOfFalse(xRange,yRange):
	return [[False for i in xRange] for j in yRange]
	

with open("input","r") as file:
	lines = file.read().splitlines()
	xRange = range(len(lines))
	yRange = range(len(lines[0]))
	numSeats = 0
	seats = [['x' for i in xRange] for j in yRange]
	for index,line in enumerate(lines):
		for symbolindex,symbol in enumerate(line):
			if(symbol == 'L'):
				seats[symbolindex][index] = '#'
			else:
				seats[symbolindex][index] = symbol

	hej = True
	while(hej):
		should_be_occupied = arrayFullOfFalse(xRange,yRange)
		should_be_empty = arrayFullOfFalse(xRange,yRange)
		for x in xRange:
			for y in yRange:
				if seats[y][x] == 'L':
					should_be_occupied[y][x] = empty_to_occupied2(x,y,seats)
				elif seats[y][x] == '#':
					should_be_empty[y][x] = occupied_to_empty2(x,y,seats)
		for x in xRange:
			for y in yRange:
				if should_be_occupied[y][x] == True:
					seats[y][x] = '#'
				if should_be_empty[y][x] == True:
					seats[y][x] = 'L'
		if isArrayFullOfFalse(should_be_occupied) and isArrayFullOfFalse(should_be_empty):
			#we are winning, count the #
			for korv in seats:
                		for nice in korv:
                        		if nice == '#':
						numSeats += 1
			break
	print numSeats

















