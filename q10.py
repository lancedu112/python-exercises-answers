s = raw_input("Please Enter some random words: ")
words = [x for x in s.split(" ")]
print " ".join(sorted(list(set(words))))



