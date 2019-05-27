# type nul > $database.db

import sqlite3
import pandas as pd
import sys
import codecs

'''
Database Schma
	Databases: players.db, test.db
	1 table for each class eg. MistweaverMonk
	Fields
		rank INTEGER
		name TEXT
		server TEXT
		iLVL INTEGER
		crit INTEGER
		haste INTEGER
		mastery INTEGER
		versatility INTEGER
'''

'''
USEAGE
	call establishConnection(database)
	call addPlayer(rank, name, server, iLVL, crit, haste, mastery, versatility)

	__main__
		prints all of the databases in the table
'''

# Allow all of db.py to access Connection
connection = None
#connection = sqlite3.connect("players.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS players(rank INTEGER, name TEXT, server TEXT, iLVL INTEGER, crit INTEGER, haste INTEGER, mastery INTEGER, versatility INTEGER);")
connection.commit()

# player = (1, 'FurplePence', 'Tichondrius', 408, 15, 6, 78, 10)
def addPlayer(player):
	cursor = connection.cursor()
	# TODO: Check if player is already in the DB
	sql = 'INSERT INTO players(rank, name, server, iLVL, crit, haste, mastery, versatility) VALUES(?,?,?,?,?,?,?,?)'
	cursor.execute(sql, player)
	connection.commit()

def printDB():
	cursor = connection.cursor()
	print(pd.read_sql_query("SELECT * FROM players", connection))
	cursor.close()

def establishConnection(database):
	connection = sqlite3.connect(database)

def commitConnection():
	connection.commit()

def closeConnection():
	connection.close()

if __name__ == "__main__":
	# TODO: make this dynamic based on DB
	# TODO: make this work for all tables
	cursor = connection.cursor()
	result = pd.read_sql_query("SELECT * FROM players", connection)
	cursor.close()

	fileName = "out.txt"
	if len(sys.argv) == 2:
		fileName = sys.argv[1]
	file = codecs.open(fileName, "w", "utf-8")

	result.to_csv(fileName, sep='\t', encoding='utf-8')
