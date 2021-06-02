from listedSubstancesModule import MasterCategoryController
from hyginus import manualget, GetCAS
from UNNumbers import unNumbersListOld
from namedSubstancesModule import namedSubstances
from listedSubstancesModule import listedSubstances

unNumbers = []
finallist = []
failedlist = []

keyslist = ["chemid", "CAS", "UN", "name", "hazardPhrases", "tier1", "tier2", "tier3", "chemtype", "category", "tooltip"]

def GetTiers(item):
  try:
    if item['chemtype'] == "named":
      for namedSubstance in namedSubstances:
        for key in keyslist:
          if key in namedSubstance.keys() and key in item.keys() and item[key] == namedSubstance[key]:
            result = {}
            result['tier1'] = namedSubstance['tier1']
            result['tier2'] = namedSubstance['tier2']
            result['tier3'] = namedSubstance['tier3']
            print(item['name'], str(result))
            return result
    elif item['chemtype'] == "listed":
      for listedSubstance in listedSubstances:
        if item['category'] == listedSubstance['desc']:
          result = {}
          result['tier1'] = listedSubstance['tier1']
          result['tier2'] = listedSubstance['tier2']
          result['tier3'] = listedSubstance['tier3']
          print(item['name'], str(result))
          return result
  except:
    result = {}
    result['tier1'] = 0
    result['tier2'] = 0
    result['tier3'] = 0
    print(item['name'], "FAILED TO SET TIERS")
    return result

for item in unNumbersListOld:
  replacement = {"UN": str(item[1]), "name": item[0]}
  unNumbers.append(replacement)

for item in unNumbers:
  item['chemtype'] = "listed"
  for namedSubstance in namedSubstances:
    if item["name"] == namedSubstance['name'] or str(item["UN"]) == str(namedSubstance['UN']):
      item['chemtype'] = "named"
    
for item in unNumbers:
  try:
    print(item)
    getchemresults = manualget(item)
    print(getchemresults)
    if getchemresults != False:
      for key in getchemresults.keys():
        item[key] = getchemresults[key]
        item['chemtype'] = "listed"
      item['CAS'] = GetCAS(item['chemid'])
      item['category'] = MasterCategoryController(item['hazardPhrases'], item['chemid'])
      try:
        tierInfo = GetTiers(item)
        for key in tierInfo.keys():
          item[key] = tierInfo[key]
        finallist.append(item)
      except:
        print("Failed: ", str(item))
  except Exception as e:
    failedlist.append(item)
    print("Error: ", item['name'], e)

f=open("testmodule18output.txt","w+")
f.write("unNumbers = [")
for sub in finallist:
  try:
    f.write("{\n")
    for key in keyslist:
      if key in sub.keys():
        if type(sub[key]) is int:
          f.write(f"\'{key}\': \'{str(sub[key])}\',\n")
        elif type(sub[key]) is list:
          f.write(f"\'{key}\': {str(sub[key])},\n")
        else:
          f.write(f"\'{key}\': \'{sub[key]}\',\n")
      else:
        f.write(f"\'{key}\': \'\',\n")
    f.write("},\n")
  except:
    print("failed " + sub["name"])
    pass
f.close()

print("failedlist: ")
for item in failedlist:
  print(item)