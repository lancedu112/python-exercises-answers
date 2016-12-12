def factorial(x):
	n = 1
	while x >= 1:
		n = n * x
		x = x - 1
	return n
		
x = int(raw_input("Please Enter your number: "))

print factorial(x)