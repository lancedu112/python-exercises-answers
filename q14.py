s = raw_input("Please enter a sentence include Upper and lower case: ")
d = {"UPPER CASE" : 0 , "LOWER CASE" : 0}
for c in s:
	if c.isupper():
		d["UPPER CASE"] += 1
	if c.islower():
		d["LOWER CASE"] += 1
	else:
		pass
		
print "UPPER CASE" , d["UPPER CASE"]
print "LOWER CASE" , d["LOWER CASE"]
