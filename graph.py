import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('players.db')
cur = conn.cursor()

query = '''SELECT crit, haste, mastery, versatility FROM players order by haste'''
cur.execute(query)
data = cur.fetchall()

crit_values = []
haste_values = []
mastery_values = []
versatility_values = []

for row in data:
	crit_values.append(row[0])
	haste_values.append(row[1])
	mastery_values.append(row[2])
	versatility_values.append(row[3])

def normalize(values):
	total = 0
	for val in values:
		total += val
	avg = total/len(values)
	print(avg)
	weighted_values = []
	for val in values:
		weighted_values.append(val/avg)

	print(values)
	print(weighted_values)
	return weighted_values

crit_values = normalize(crit_values)
haste_values = normalize(haste_values)
mastery_values = normalize(mastery_values)
versatility_values = normalize(versatility_values)

plt.plot(crit_values, haste_values, color='r',linestyle="",marker="o")
plt.plot(crit_values, mastery_values, color='b',linestyle="",marker="o")
plt.plot(crit_values, versatility_values, color='g',linestyle="",marker="o")

plt.title('haste, mastery, versatility vs critical strike')
plt.legend(['haste','mastery','versatility'])

plt.show()

'''

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Haste', 'Crit'))

plt.show()

'''