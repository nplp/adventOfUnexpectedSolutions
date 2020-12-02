import itertools
with open("../input.txt","r") as file:
	input = [int(line) for line in file.readlines()]
	print input
	for x,y in itertools.combinations(input,2):
		if(x+y == 2020):
			print x*y
			break
	for x,y,z in itertools.combinations(input,3):
                if(x+y+z == 2020):
                        print x*y*z
                        exit()
