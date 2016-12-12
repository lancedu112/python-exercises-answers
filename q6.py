import math
C = 50
H = 30
value = []
items = [x for x in raw_input("Pleas Enter some comma-separated numbers : ").split(',')]
for D in items:
	value.append(str(int(round(math.sqrt(2 * C * float(D) / H)))))
	
print ','.join(value)