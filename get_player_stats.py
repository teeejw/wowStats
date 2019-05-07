from bs4 import BeautifulSoup
from urllib.request import urlopen

import db

# tmp_page = 'https://worldofwarcraft.com/en-us/character/us/tichondrius/Furplepence'

def addPlayerStats(page):
	page = urlopen(page)
	soup = BeautifulSoup(page, 'html.parser')

	# Name
	nameSearch = soup.find("a", class_="Link CharacterHeader-name")
	name = nameSearch.contents[0]
	print(name)

	# Server
	serverSearch = soup.find_all("div", class_="CharacterHeader-detail")
	server = serverSearch[2].contents[0]
	server = server[1:] # remove leading \xa0 char
	print("Server:", server)

	# iLVL
	iLVLSearch = soup.find_all("div", class_="Media-text")
	iLVL = iLVLSearch[1].contents[0]
	iLVL = iLVL.split()[0] # xxx ilvl --> xxx
	print("iLVL:", iLVL)

	# Crit
	critSearch = soup.find("div", class_="color-stat-CRITICALSTRIKE")
	critSearch = critSearch.find_all("span")
	crit = critSearch[1].contents[0]
	print("Critical Stike:", crit)

	# Haste
	hasteSearch = soup.find("div", class_="color-stat-HASTE")
	hasteSearch = hasteSearch.find_all("span")
	haste = hasteSearch[1].contents[0]
	print("Haste:", haste)

	# Mastery
	masterySearch = soup.find("div", class_="color-stat-MASTERY")
	masterySearch = masterySearch.find_all("span")
	mastery = masterySearch[1].contents[0]
	print("Mastery:", mastery)

	# Versatility
	versatilitySearch = soup.find("div", class_="color-stat-VERSATILITY")
	versatilitySearch = versatilitySearch.find_all("span")
	versatility = versatilitySearch[1].contents[0]
	print("Versatility:", versatility)

	player = (name, server, iLVL, crit, haste, mastery, versatility)
	db.addPlayer(player)

def test(page):
	page = urlopen(page)
	soup = BeautifulSoup(page, 'html.parser')

# <div class="GameIcon GameIcon--EPIC GameIcon--azerite GameIcon--slot CharacterProfile-itemIcon CharacterProfile-itemSlot GameIcon--transmog GameIcon--large" media-wide="GameIcon--large" queryselectoralways="0" media-original="GameIcon GameIcon--EPIC GameIcon--azerite GameIcon--slot CharacterProfile-itemIcon CharacterProfile-itemSlot GameIcon--transmog"><div class="GameIcon-icon" style="background-image:url(&quot;https://render-eu.worldofwarcraft.com/icons/56/inv_helm_leather_zandalardungeon_c_01.jpg&quot;);"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>
	#azeriteTraitsSearch = soup.find_all("div", class_="CharacterProfile-itemSlot")
	azeriteTraitsSearch = soup.find_all(string="Font of Life")
	for t in azeriteTraitsSearch:
		print(t.prettify())
