import re

def newValidationArray():
	return [
		["byr:",False,False],
		["iyr:",False,False],
		["eyr:",False,False],
		["hgt:",False,False],
		["hcl:",False,False],
		["ecl:",False,False],
		["pid:",False,False]
		]

def matchFunction(category,value):
	if(category == 'byr'):
                if(int(value) >= 1920 and int(value) <= 2002):
			return True
        if(category == "iyr"):
                if(int(value) >= 2010 and int(value) <= 2020):
			return True
        if(category == "eyr"):
                if(int(value) >= 2020 and int(value) <= 2030):
                        return True
        if(category == "hgt"):
                if(value.find("cm") != -1):
                        val = re.split("cm",value)[0]
                        if(int(val) >=150 and int(val) <= 193):
				return True
                if(value.find("in") != -1):
                        val = re.split("in",value)[0]
                        if(int(val) >= 59 and int(val) <= 76):
                                return True
        if(category == "hcl"):
                if(re.findall(r"#[0-9a-f]",value) !=-1 and len(value) == 7):
			return True
        if(category == "ecl"):
                if(value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"):
			return True
        if(category == "pid"):
                if(len(value) == 9 and value.isdigit()):
			return True
	return False
	
with open("input","r") as file:
	input = file.read()
	result = 0
	moreStrictResult = 0
	passInfo = re.split(r"(?:\r?\n){2,}",(input.strip()))
	for port in passInfo:
		valid = newValidationArray()
		okPassport = True
		for match in valid:
                	if(port.find(match[0]) != -1):
				match[1] = True
                for match in valid:
                	if(match[1] == False):
                        	okPassport = False
                                break
		passport = port.split()
		okMoreStrictPassport = True
		if(len(passport) > 8 or len(passport) <7):
			print "wrong length"
			okMoreStrictPassport = False
		if(len(passport) == 7):
			for korv in passport:
				if(korv.find("cid") != -1):
					okMoreStrictPassport = False
		for item in passport:
			category = item.split(":")[0]
			value = item.split(":")[1]
			if(category != "cid"):
				strict = matchFunction(category,value)
				if(strict == False):
					okMoreStrictPassport = False
					break
		if(okMoreStrictPassport):
			moreStrictResult +=1
		if(okPassport):
			result +=1
	print result
	print moreStrictResult
