import requests
from hyginus import stringsearch
from finallist import namedSubstancesModule
import time
import json


def GetCAS(cid):
  query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=synonyms"
  print("query: ", query)
  response = requests.get(query)
  queryAnswer = json.loads(response.content)
  print("response received. Searching for CAS")
  cas = stringsearch(json.dumps(queryAnswer),"CAS")
  return cas

emptyarr = []

for sub in finallist:  
  if "chemid" in sub.keys() and sub["chemid"] is not None:
    print("Substance: " + sub["name"])
    cas = GetCAS(sub["chemid"])
    newinfo = {"name": sub["name"], "cid": sub["chemid"], "CAS": cas}
    emptyarr.append(newinfo)
    print("Found: " + str(newinfo))
    print("Sleeping. Restarting cycle in 5 seconds")
    time.sleep(5)
    print("Resume")


f=open("finallist2.txt","w+")
for sub in emptyarr:
  f.write(str(sub))
f.close()