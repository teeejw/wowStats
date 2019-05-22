import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('players.db')
cur = conn.cursor()

query = '''SELECT rank, crit, haste, mastery, versatility FROM players order by haste'''
cur.execute(query)
data = cur.fetchall()

rank_values = []
crit_values = []
haste_values = []
mastery_values = []
versatility_values = []

for row in data:
	rank_values.append(row[0])
	crit_values.append(row[1])
	haste_values.append(row[2])
	mastery_values.append(row[3])
	versatility_values.append(row[4])

def normalize(values):
	total = 0
	for val in values:
		total += val
	avg = total/len(values)

	weighted_values = []
	for val in values:
		weighted_values.append(val/avg)
	return weighted_values
'''

look at rank 1-4 top->bottom

categorize by which is top?
map
	c1 h2 m3 v4
	c1 h2 v3 m4
	.
	.
	v1 m2 c3 h4
	v1 m2 h3 c4



crit_values = sorted(normalize(crit_values))
haste_values = sorted(normalize(haste_values))
mastery_values = sorted(normalize(mastery_values))
versatility_values = sorted(normalize(versatility_values))

'''
crit_values = normalize(crit_values)
haste_values = normalize(haste_values)
mastery_values = normalize(mastery_values)
versatility_values = normalize(versatility_values)

plt.plot(rank_values, crit_values, color='k', linestyle="", marker="o")
plt.plot(rank_values, haste_values, color='r', linestyle="", marker="o")
plt.plot(rank_values, mastery_values, color='m', linestyle="", marker="o")
plt.plot(rank_values, versatility_values, color='g', linestyle="", marker="o")
'''

plt.plot(crit_values, rank_values, color='k', linestyle="", marker="o")
plt.plot(haste_values, rank_values, color='r', linestyle="", marker="o")
plt.plot(mastery_values, rank_values, color='m', linestyle="", marker="o")
plt.plot(versatility_values, rank_values, color='g', linestyle="", marker="o")
'''

plt.title('critical strike, haste, mastery, versatility by rank')
plt.legend(['critical strike', 'haste','mastery','versatility'])
plt.xlabel('Player Rank')
plt.ylabel('normalized stat values')

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