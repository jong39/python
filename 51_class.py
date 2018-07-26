class SoccerPlayer(object):
	def __init__(self, name, position, back_number):
		self.name = name
		self.position = position
		self.back_number = back_number

	def change_back_number(self, new_number):
		print("Back number has changed from %d to %d" % (self.back_number, new_number))
		self.back_number = new_number

	def __str__(self):
		return "Hello, My name is %s. I play in %s in center" % (self.name, self.position)




johnny = SoccerPlayer("Johnny", "MF", 10)
print(johnny)

print("Current backnumber?", johnny.back_number)
johnny.change_back_number(5)
print("Current backnumber?", johnny.back_number)
