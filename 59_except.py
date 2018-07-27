for i in range(10):
	try:
		print(i, 10 // i)
	except ZeroDivisionError:
		# print(e)
		print("Can not be divided by 0")

print("============")

for i in range(10):
	try:
		print(i, 10 // i)
	except ZeroDivisionError as err:
		print(err)
		print("Can not be divided by 0")

print("============")

string_ex = "123abc"
for value in string_ex:
	try:
		# value.isdigit()
		print(int(value))
	except Exception as err:
		print(err)
print("============")

# try except else

for i in range(10):
	try:
		result = 10 / i
	except ZeroDivisionError as e:
		print(e)
		print("Can not be divided by 0")
	else:
		print(result)

print("============")

# try except finally

try:
	for i in range(1, 10):
		result = 10 // i
		print(i, result)
except ZeroDivisionError:
	print("Can not be divided by 0")
finally:
	print("Completed.")

print("============")

# raise

while True:
	value = input("Please input integer: ")
	for digit in value:
		if digit not in "0123456789":
			raise ValueError("This is no number!")
	print(int(value))
















