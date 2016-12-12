l = []

items = [x for x in raw_input("Please Enter 4 digit binary numbers with comma: ").split(",")]

for y in items:
    z = int(y, 2)
    if not z % 5:
	l.append(y)

print ",".join(l)




