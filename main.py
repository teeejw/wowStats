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

NUM_RESULTS = 1 #102
playerXPaths = []
playerLinks = []

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
	playerLinks.append(driver.find_element_by_xpath(playerXPaths[i]))


for i in range(len(playerLinks)):
	print("Player Profile Link:",playerLinks[i].get_attribute('href'))
	stats.addPlayerStats(playerLinks[i].get_attribute('href'))
	'''
	print("********************************TESTING********************************")
	#stats.test(playerLinks[i])
	playerLinks[i].click()
	#driver.find_elements_by_class_name("item-specs")

	#/html/body/div[1]/div/div[3]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[1]/a/div/div[1]/div[3]
	#print(driver.find_element_by_xpath("//*[@id=\"iziModal3159703\"]/div/div/div[3]/div[2]"))


	#iziModal3159703 > div > div > div.List.List--gutters.List--top
	#iziModal3159703 > div > div > div.List.List--gutters.List--top\
	#//*[@id="iziModal3159703"]/div/div/div[3]/div[2]
	'''
	
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