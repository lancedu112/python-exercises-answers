import sys
netAmount = 0
while True:
	s = raw_input("Please enter your bank transaction log start with D or W: ")
	if not s:
		break
	values = s.split(" ")
	operation = values[0]
	amount = int(values[1])
	if operation == "D":
		netAmount += amount
	elif operation == "W":
		netAmount -= amount
	else:
		pass
		
print netAmount