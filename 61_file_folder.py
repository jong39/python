import os

if not os.path.isdir("log"):
	os.mkdir("log")
if not os.path.exists("./log/count_log.txt"):
	f = open("./log/count_log.txt", "w", encoding="utf-8")
	f.write("Log starts: \n")
	f.close()

with open("./log/count_log.txt", "a", encoding="utf-8") as f:
	import random, datetime
	for i in range(1, 11):
		stamp = str(datetime.datetime.now())
		value = random.random() * 100000
		log_line = stamp + "\t" + str(value) + " created \n"
		f.write(log_line)

