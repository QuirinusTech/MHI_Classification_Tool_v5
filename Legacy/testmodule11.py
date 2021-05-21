from finallist import namedSubstances
import requests
import json

f = open('14771.json',)
var14771 = json.load(f)
f.close()

def BreakItDown(arg):

  if TOCHeadingFound(arg["Record"]) == True:
    return arg["Record"]
  else:
    if TOCHeadingFound(arg["Record"]["Section"][0]) == True:
      return arg["Record"]["Section"][0]
    else:
      if TOCHeadingFound(arg["Record"]["Section"][0]["Section"][0]) == True:
        return arg["Record"]["Section"][0]["Section"][0]
      else:
        if TOCHeadingFound(arg["Record"]["Section"][0]["Section"][0]["Section"][0]) == True:
          return arg["Record"]["Section"][0]["Section"][0]["Section"][0]
        else:
          if TOCHeadingFound(arg["Record"]["Section"][0]["Section"][0]["Section"][0]["Section"][0]) == True:
            return arg["Record"]["Section"][0]["Section"][0]["Section"][0]["Section"][0]
          else:
            return False

def TOCHeadingFound(arg):
  if "TOCHeading" not in arg.keys():
    return False
  elif arg["TOCHeading"] == "Hazard Classes and Categories":
    return True
  else:
    return False

biglist = []

for chem in namedSubstances:
  if "hazardPhrases" in chem.keys() and "H300" in chem["hazardPhrases"]:
    print(chem["name"])
    cid = chem["chemid"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=Hazard%20classes%20and%20categories"
    response = requests.get(query)
    queryAnswer = json.loads(response.content)
    indexvalue = BreakItDown(queryAnswer)
    infoarray = indexvalue["Information"]
    hcats = []
    for obj in infoarray:
      for string in obj["Value"]["StringWithMarkup"]:
        if len(hcats) < 10: 
          hcats.append(string["String"])
    print(hcats)
    chem["hazardCategories"] = hcats
    biglist.append({"substance": chem["name"], "hazardCategories": hcats})

print(biglist)

f=open("h300chems.txt","w+")
for chem in namedSubstances:
  if "hazardCategories" in chem.keys():
    f.write(str(chem))
f.close()


