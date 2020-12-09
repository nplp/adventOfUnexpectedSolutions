with open("input","r") as file:
	numbers = [long(l) for l in file.read().splitlines()]

	pointer = 25
	invalidNumber = 0
	for index, number in enumerate(numbers,start = pointer):
		value = numbers[pointer]
		result = False	
		for num1 in numbers[pointer-25:pointer]:
			for num2 in numbers[pointer-25:pointer]:
				if(num1 != num2 and num1+num2 == value):
					result = True
		if(result == False):
			invalidNumber = value
			break
		else:
			pointer+=1
	print invalidNumber

	countSum = 0
	startIndex = 0
	notfinished = True
	while(notfinished):
		countSum = 0
		highestValueInLoop = 0
		lowestValueInLoop = 1000000000
		for number in numbers[startIndex:]:
			if(number > highestValueInLoop):
				highestValueInLoop = number
			if(number < lowestValueInLoop):
				lowestValueInLoop = number
			countSum += number
			if(countSum == invalidNumber):
				print lowestValueInLoop + highestValueInLoop
				exit()
			if(countSum > invalidNumber):
				startIndex+=1
				break
		

