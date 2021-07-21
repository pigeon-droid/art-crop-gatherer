import json
import urllib.request
import os

# I'm using MTGjson catalog
identifiers = open('AllIdentifiers.json', encoding='UTF-8') 
identifiers = json.load(identifiers)

row_list = []

card_list = {}

wizard_list = []
warrior_list = []

for each in identifiers['data']:
    row = []
    row.append(identifiers['data'][each]['name'])
    row.append(identifiers['data'][each]['setCode'])
    row.append(identifiers['data'][each]['number'])
    row.append(identifiers['data'][each]['type'])
    row.append(identifiers['data'][each]['identifiers']['scryfallId'])
    card_list[tuple(row)] = each

for each in card_list:
    if "Wizard" in each[3] and each[0] not in wizard_list:
        url = 'https://c1.scryfall.com/file/scryfall-cards/art_crop/front/' + each[4][0] + "/" + each[4][1] + "/" + each[4] + ".jpg"
        urllib.request.urlretrieve(url, os.getcwd() + "\\Wizard\\" + each[4] + ".jpg")
        wizard_list.append(each[0])

    elif "Warrior" in each[3] and each[0] not in warrior_list:
        url = 'https://c1.scryfall.com/file/scryfall-cards/art_crop/front/' + each[4][0] + "/" + each[4][1] + "/" + each[4] + ".jpg"
        urllib.request.urlretrieve(url, os.getcwd() + "\\Warrior\\" + each[4] + ".jpg")
        warrior_list.append(each[0])
