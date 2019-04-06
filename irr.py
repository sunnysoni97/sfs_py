import csv

with open('C:\Users\divya\Desktop\zoes_sleep_csv.csv','r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for line in csv_reader:
		diff=0
		count=0
		for x in range(1,814):
			if line['day up'] == 1:
				diff = line['Diff(min)'] + diff
				count = count + 1
		print(count)
