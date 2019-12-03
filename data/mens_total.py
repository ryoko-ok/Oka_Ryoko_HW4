import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = [] # first row -> not data

with open('data/JPN_mens_total.csv') as csvfile: 
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("This is The Number of Japanese Total Medals(Men)")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("Gold")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("Silver")
				silvers.append(row[7])
			else: 
				print("Bronze")
				bronzes.append(row[7])

			print(line_count)
			line_count += 1

# now we can see our medal counts
print(len(golds))
print(len(silvers))
print(len(bronzes))

labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Then Number of Japanese Olympic Medals(Men)")
plt.xlabel("Medal Counts Since 1956 to 2014")
plt.show()





