words = "the quick brown fox jumps over the lazy dog".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# print(stuff)

stuff_dict = {i:j for i,j in enumerate(words) }
print(stuff_dict)




