class Person(object):
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def about_me(self):
		# print("My name is %s and then my age is $s" % (self.name, str(self.age)))
		print("My name is", self.name, " and then my age is ", str(self.age))


class Employee(Person):
	def __init__(self, name, age, gender, salary, hire_date):
		super().__init__(name, age, gender)
		self.salary = salary
		self.hire_date = hire_date

	def do_work(self):
		print("Let's get some work done!")

	def about_me(self):
		super().about_me()
		print("My salary is ", self.salary, "and then my hire date is " , self.hire_date)


my_person = Person("Johnny", 34, "M")
my_emp = Employee("Tiger", "23", "M", 50000, "2016/3/4")
my_person.about_me()
my_emp.about_me()
# print(my_person.about_me())

 
 