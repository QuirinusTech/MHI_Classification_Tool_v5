from hyginus import stringsearch
import time
import json
import requests
from finallist import namedSubstances



newarray = []
failures = []
errors = []

def GetCAS(cid):
  query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=synonyms"
  print("query: ", query)
  response = requests.get(query)
  queryAnswer = json.loads(response.content)
  print("response received. Searching for CAS")
  cas = stringsearch(json.dumps(queryAnswer),"CAS")
  return cas

for entry in nocas:
  try:
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{entry}/json"

    response = requests.get(query)
    queryAnswer = json.loads(response.content)

    check1 = stringsearch(json.dumps(queryAnswer),"fault")
    #parse the response
    if check1 == "OK":
      cid = stringsearch(json.dumps(queryAnswer), "cid")
      print("CID found: ", cid)
      if cid != "NotFound":
        #call 2
        query2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=GHS classification"
        print("query2: ", query2)
        response2 = requests.get(query2)
        queryAnswer2 = json.loads(response2.content)
        print("response2 received")
        check2 = stringsearch(json.dumps(queryAnswer2),"fault")
      
        if check2 == "OK":
          newChem = {"CAS": "", "name": "", "chemid": "", "hazardPhrases": ""}
          hazardPhrases = stringsearch(json.dumps(queryAnswer2), "H")
          try:
            maybeCAS = GetCAS(cid)
            newChem["CAS"] = maybeCAS
          except:
            pass
          newChem["chemid"] = cid
          newChem["hazardPhrases"] = hazardPhrases
          newChem["name"] = entry
          newarray.append(newChem)
        else:
          failures.append({"1": queryAnswer, "2": queryAnswer2, "name": entry})

        print("Cycle paused for five seconds.")
        time.sleep(5)
        print("Done sleeping")
  except Exception as e:
    errors.append([entry, e])
    pass

f=open("FoundNewCAS.txt","w+")
for line in newarray:
  f.write(str(line))
f.close()
print(newarray)

f=open("NotFoundNewCAS.txt","w+")
for linee in failures:
  f.write(str(linee))
f.close()
print(failures)

f=open("TestModule9errors.txt")
for error in errors:
  f.write(str(error))
f.close()
print(errors)
