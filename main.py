# main script for wowStats
# type nul > players.db
# taskkill /IM "chromedriver.exe" /F


import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import get_player_stats as stats
import db

'''
# Kill webdriver processes that weren't exited properly
# taskkill /IM "chromedriver.exe" /F
os.system("START \"\" taskkill /IM \"chromedriver.exe\" /F")
# Give the system some time to execute the command
time.sleep(.5)
'''

driver = webdriver.Chrome()

driver.get("https://www.worldofwargraphs.com/pve-stats/best-players/monk/mistweaver")

NUM_RESULTS = 100
playerXPaths = []
playerLinks = []

i = 2
while i < 2+NUM_RESULTS:
	playerXPaths.append("//*[@id=\"content\"]/div/div[4]/div[2]/div[1]/table/tbody/tr[{}]/td[5]/a".format(i))
	i += 1

for i in range(len(playerXPaths)):
	print(playerXPaths[i])
	playerLinks.append(driver.find_element_by_xpath(playerXPaths[i]))


for i in range(len(playerLinks)):
	print("Player ", i+1, "/", NUM_RESULTS, sep="")
	print("Player Profile Link:",playerLinks[i].get_attribute('href'))
	# playerLinks[i].click()
	stats.addPlayerStats(playerLinks[i].get_attribute('href'))

	#TODO: GET AZERITE TRAITS FROM raider.io???

driver.quit()
db.printDB()
db.commitConnection()
db.closeConnection()