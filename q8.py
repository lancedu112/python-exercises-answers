items = [x for x in raw_input("Please Enter some comma-separated words : ").split(',')]

items.sort()

print ','.join(items)