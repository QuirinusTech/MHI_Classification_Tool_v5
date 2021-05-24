from namedSubstancesModule import namedSubstances, succeeded
from listedSubstancesModule import NewHazardCategoryFinder

for sub in namedSubstances:
  sub["chemtype"] = "named"
  print("Trying " + sub["name"])
  if type(sub["chemid"]) is int and sub["chemid"] < 1000000:
    try:
      sub["category"] = NewHazardCategoryFinder(sub["chemid"])
      print("success")
    except Exception as e:
      print("failed: " + str(e))
      pass


keyslist = ["chemid", "CAS", "UN", "name", "hazardPhrases", "tier1", "tier2", "tier3", "chemtype", "category", "tooltip"]

f=open("testmodule17output2.txt","w+")
f.write("namedSubstances = [")
for sub in namedSubstances:
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