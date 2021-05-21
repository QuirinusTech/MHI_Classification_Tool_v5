from hyginus import stringsearch
import time
import json
import requests
from newNamedSubs import newNamedSubs

newarray = []
failures = []
for entry in newNamedSubs:
  try:
    substance = entry["name"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"

    if entry["UN"] != "" and entry["UN"] != "-":
      if type(entry["UN"]) == list:
        un = entry["UN"][0]
        if len(un) > 4:
          un = un[0:4]
        query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/UN%20{un}/json"
        print("Searching for UN: \"" + un + "\"")
      elif type(entry["UN"]) == str:
        un = entry["UN"]
        if len(un) > 4:
          un = un[0:4]
        query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/UN%20{un}/json"
        print("Searching for UN: \"" + un + "\"")
    if len(un) != 4:
      substance = entry["name"]
      query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"

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
          hazardPhrases = stringsearch(json.dumps(queryAnswer2), "H")
          entry["chemid"] = cid
          entry["hazardPhrases"] = hazardPhrases
          newarray.append(entry)
          if entry["chemid"] != None: 
            filename = entry["chemid"] + "success.txt"
            f=open(filename,"w+")
            f.write(str(entry))
            f.close()
          else:
            failures.append({"1": queryAnswer, "2": queryAnswer2})

        print("Sleeping")
        time.sleep(10)
        print("Done sleeping")
  except:
    pass

f=open("NewUnNumbers","w+")
f.write(str(newarray))
f.close()
print(newarray)

f=open("Failures","w+")
f.write(str(failures))
f.close()
print(failures)