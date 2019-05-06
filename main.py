# taskkill /IM "chromedriver.exe" /F

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import get_player_stats as stats
import db

driver = webdriver.Chrome()

driver.get("https://www.worldofwargraphs.com/pve-stats/best-players/monk/mistweaver")

NUM_RESULTS = 10 #102
playerXPaths = []
playerLinks = []
players = []

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

i = 2
while i < 2+NUM_RESULTS:
	playerXPaths.append("//*[@id=\"content\"]/div/div[4]/div[2]/div[1]/table/tbody/tr[{}]/td[5]/a".format(i))
	i += 1

for i in range(len(playerXPaths)):
	print(playerXPaths[i])
	playerLinks.append(driver.find_element_by_xpath(playerXPaths[i]).get_attribute('href'))


for i in range(len(playerLinks)):
	print(playerLinks[i])
	stats.addPlayerStats(playerLinks[i])
	
db.printDB()
db.closeConnection()
# time.sleep(5)
driver.quit()


'''
class Player:
	def __init__(self, name, iLVL, azeriteTraits, crit, haste, mastery, vers, talents):
		self.name = name
		self.iLVL = iLVL
		self.azeriteTraits = azeriteTraits
		self.crit = crit
		self.haste = haste
		self.mastery = mastery
		self.vers = vers
		self.talents = talents
'''
'''
# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
	# we have to wait for the page to refresh, the last thing that seems to be updated is the title
	WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

	# You should see "cheese! - Google Search"
	print(driver.title)

finally:
	driver.quit()
'''