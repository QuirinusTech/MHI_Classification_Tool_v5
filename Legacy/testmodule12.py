from listedSubstancesModule import GetHazardCategories
from namedSubstancesModule import namedSubstances

sample = []

for sub in namedSubstances:
  if "chemid" in sub.keys() and sub["chemid"] < 100000:
    try:
      thisitem = {"name": sub["name"], "hcats": GetHazardCategories(sub["chemid"])}
      sample.append(thisitem)
    except:
      pass

f=open("testmodule12output.txt","w+")
for chem in sample:
  f.write(str(chem))
  f.write(",\n")
f.close()