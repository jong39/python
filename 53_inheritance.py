class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return "My name is {0}".format(self.name) #  =====> ????


class Korean(Person):
	pass #pass라는 명령어로 Person class를 상속 받는다. 


first_korean = Korean("Johnny Choi", 20)
print(first_korean.name)
print(first_korean)