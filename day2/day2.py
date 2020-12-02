import re
import itertools
with open("input","r") as file:
	input = file.readlines()
	valids = 0
	validsNewPolicy = 0
	for word in input:
		minmax = re.findall("[0-9]+-[0-9]+\s",word)[0]
		numbers = re.findall("[0-9]+",minmax)
		min =  int(numbers[0])
		max = int(numbers[1])
		passwordSign = re.findall("[a-z]:",word)[0][0]
		password = re.findall("[a-z]+$",word)[0]
		instances = 0
		for letter in password:
			if letter == passwordSign: instances +=1
		if instances >= min and instances <= max: valids+=1
		if (passwordSign == password[min-1] and passwordSign != password[max-1]):
			validsNewPolicy += 1
		if (passwordSign != password[min-1] and passwordSign == password[max-1]):
			validsNewPolicy +=1
print valids
print validsNewPolicy 
