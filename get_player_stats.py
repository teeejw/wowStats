from bs4 import BeautifulSoup
from urllib.request import urlopen

import db

# tmp_page = 'https://worldofwarcraft.com/en-us/character/us/tichondrius/Furplepence'

def addPlayerStats(page):
	page = urlopen(page)
	soup = BeautifulSoup(page, 'html.parser')

	# Name
	# <a class="Link CharacterHeader-name" href="/en-gb/character/eu/tarren-mill/pottermonk">Pottermonk</a>
	nameSearch = soup.find("a", class_="Link CharacterHeader-name")
	name = nameSearch.contents[0]
	print(name)

	# iLVL
	# <div class="Media-text">418 ilvl</div>
	iLVLSearch = soup.find_all("div", class_="Media-text")
	iLVL = iLVLSearch[1].contents[0]
	iLVL = iLVL.split()[0]
	print(iLVL)

	# Crit
	# <div class="Media Media--gutterLarge color-stat-CRITICALSTRIKE Media--large" media-medium="!Media--small Media--large" queryselectoralways="0" media-original="Media Media--small Media--gutterLarge color-stat-CRITICALSTRIKE"><div class="Media-image"><span class="Icon Icon--critical-strike Media-icon"><svg class="Icon-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 64 64" focusable="false"><use xlink:href="/static/components/Icon/Icon.svg#critical-strike"></use></svg></span></div><div class="Media-text"><span>26%</span><div class="font-semp-xSmall-white text-upper">Critical Strike</div></div></div>
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

	player = (name, iLVL, crit, haste, mastery, versatility)
	db.addPlayer(player)