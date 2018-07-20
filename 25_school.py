print("when were you born?")
year_born = input()
age = 2018 - int(year_born)
if int(age > 30):
	print("You are old", age)
else:
	print("You are yong", age)

