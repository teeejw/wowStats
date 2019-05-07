# type nul > players.db

import sqlite3

# Set up DB and Connection
connection = sqlite3.connect("players.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS players(name TEXT, server TEXT, iLVL INTEGER, crit INTEGER, haste INTEGER, mastery INTEGER, versatility INTEGER);")

# player = ('FurplePence', 408, 15, 6, 78, 10)
def addPlayer(player):
	cursor = connection.cursor()
	sql = 'INSERT INTO players(name, server, iLVL, crit, haste, mastery, versatility) VALUES(?,?,?,?,?,?,?)'
	cursor.execute(sql, player)

def printDB():
	cursor = connection.cursor()
	results = cursor.execute('SELECT * FROM players')

	for r in results:
	    print(r)
	cursor.close()

def closeConnection():
	connection.close()

