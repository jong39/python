import csv

sample_data = []
header = []
rownum = 0

with open("sample.csv", "r", encoding="utf-8") as p_file:
	csv_data = csv.reader(p_file)
	for row in csv_data:
		# print(row[2])
		if rownum == 0:
			header = row
		title = row[2]
		if title.find("Director") != -1:
			sample_data.append(row)
		rownum += 1

# print(sample_data)
# for row in sample_data:
#     print(row[2])

with open("sample_write.txt", "w", encoding="utf-8") as pw_file:
	writer = csv.writer(pw_file, delimiter=",", quotechar="'", quoting=csv.QUOTE_ALL)
	writer.writerow(header)
	for row in sample_data:
		writer.writerow(row)