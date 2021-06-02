from UNNumbers import unNumbers
from namedSubstancesModule import namedSubstances

for namedSubstance in namedSubstances:
  for item in unNumbers:
    if type(namedSubstance['UN']) is list:
      for unnumber in namedSubstance['UN']:
        if unnumber == item['UN']:
          print(item['name'], namedSubstance['name'])
          print(item['UN'], namedSubstance['UN'])
          print(item['chemid'], namedSubstance['chemid'])
    else:
      if item["name"] == namedSubstance['name'] or str(item["UN"]) == str(namedSubstance['UN']):
        item['chemtype'] = "named"
        print(item['name'], namedSubstance['name'])
        print(item['UN'], namedSubstance['UN'])
        print(item['chemid'], namedSubstance['chemid'])