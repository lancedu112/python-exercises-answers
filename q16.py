values = raw_input("Please enter a sequence of comma-seperated numbers: ")
numbers = [x for x in values.split(",") if int(x)%2 != 0]
print ",".join(numbers)