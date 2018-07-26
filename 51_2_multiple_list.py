name = ["Tiger", "Wood", "Johnny", "choi", "Kevin"]
position = ["MF", "DF", "CF", "WF", "GK"]
number = [10, 15, 20, 25, 30]

players = [[name, position, number] for name, position, number in zip(name, position, number)]
print(players)