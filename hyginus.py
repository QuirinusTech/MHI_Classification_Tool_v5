import re
from listedSubstancesModule import listedSubstances, RuleFinder, MasterCategoryController, RuleFinder, listedSubstances, CategoryFinder
from namedSubstancesModule import namedSubstances
import json
import requests
from mercury import ReportError
import traceback

def stringsearch(z,t):
  """
    Searches a given string (z) for one of the patterns patterns (t)
    
  """
  print("key to search by (t): ", t)

  print("stringsearch by t: ", t)
  if t == "H": #Hazard statements
    hazardphraseslist = re.findall(r"H[2-4]\d\d", z)
    results = []
    for i in hazardphraseslist:
      print(i)
      if i not in results:
        results.append(i)
    print("Response: ", results)
    return results
  elif t == "cid": #cid
    match = re.search(r"(\"cid\"\:\s*)([0-9]+)", z)
    if match is None:
       print("stringsearch", t, "No cid found")
       return "NotFound"
    else:
      print("Response: ", match.group(2))
      return match.group(2)
  elif t == "fault": #PUG errors
     match = re.search(r"(PUG[REST|VIEW].)([NotFound|Timeout])", z)
     print("Match value: ", match)
     if match is None:
       print("stringsearch", t, "No faults found")
       return "OK"
     else:
       print("fault found: ", match.group(2))
       return match.group(2)
  elif t == "RT": #Record Title
    match = re.search(r"(RecordTitle.\: [\'|\"])([A-Za-z\s*]+)([\'|\"])", z)
    if match is None:
      print("stringsearch", t, "Response: None")
      return None
    else:
      print("Response: ", match.group(2))
      return match.group(2)
  elif t == "UN":
    match = re.search(r"([\'|\"]UN[\s]?)(\d{4})([\'|\"],)", z)
    if match is None:
      print("stringsearch", t, "Response: None")
      return None
    else:
      print("UN Number: ", match.group(2))
      return match.group(2)
  elif t == "CAS":
    match = re.search(r"([0-9]{2,7}-[0-9]{2}-[0-9])", z)
    if match is None:
      print("stringsearch", t, "Response: None")
      return None
    else:
      print("CAS Number: ", match.group(1))
      return match.group(1)
  else:
    pass

def assessment(inv):
  """
    Full inventory (inv) assessment assessment.
    Determined individual tier
    if individual tier = 0, also determines aggregate tier

    returns an dict of results
  """
  #set up final variable
  results = {"indTier" : 0, "aggregateTier": 0, "finalTier": 0}
  individualFlags = []
  try:
    #individual tiers
    for item in inv:
      item["tier"] = deftier(item)
      if item["tier"] == None or item["tier"] == False:
        individualFlags.append(item['name'])
      else:
        if item["tier"] > results["indTier"]:
          results["indTier"] = item["tier"]
    if results["indTier"] > 0:
      results["finalTier"] = results["indTier"]

    #calculate the aggregate rules
    aggregateFindings = AggregateAssessment(inv)
    for aggKey in aggregateFindings.keys():
      results[aggKey] = aggregateFindings[aggKey]

    if results["aggregateTier"] > results["finalTier"]:
      results["finalTier"] = results["aggregateTier"]
    if len(individualFlags) > 0:
      results["flag"] = True
      for item in individualFlags:
        results["flaggedSubstances"].append(item)
    return results
  except Exception as e:
    errorstring = str(traceback.print_exc())
    errorstring = errorstring + str(e) + str(inv)
    ReportError(errorstring)


def AggregateAssessment(inv):
  usedListedSubstances = {"H": 0, "P": 0, "O": 0}
  aggregateTier = 3
  done = False
  flaggedSubstances = []
  flag = False

  while done == False:
    usedListedSubstances["H"] = 0
    usedListedSubstances["P"] = 0
    usedListedSubstances["O"] = 0
    for item in inv:
      if item['chemtype']=="named":
        for substance in namedSubstances:
          if int(item["chemid"]) == int(substance["chemid"]):
            currenttier = "tier" + str(aggregateTier)
            qx = float(item["qty"]) / float(substance[currenttier])
            rule = RuleFinder(item)
            if rule != 0:
              substance["rule"] = rule
              usedListedSubstances[rule] = float(usedListedSubstances[rule]) + qx
            else:
              flag = True
              flaggedSubstances.append(item["name"])
      elif item['chemtype']=="listed":
        for substance in listedSubstances:
          if int(item["chemid"]) == int(substance["chemid"]) or item['category'] == substance['desc']:
            currenttier = "tier" + str(aggregateTier)
            qx = float(item["qty"]) / float(substance[currenttier])
            rule = RuleFinder(item)
            if rule != 0:
              substance["rule"] = rule
              usedListedSubstances[rule] = float(usedListedSubstances[rule]) + qx
            else:
              flag = True
              flaggedSubstances.append(item["name"]) 
    for sub in usedListedSubstances.keys():
      if usedListedSubstances[sub] >= 1: 
        done = True
    if aggregateTier > 0 and done == False:
      aggregateTier = aggregateTier-1
    if aggregateTier == 0:
      done = True

  #update the overall/final tier based on the findings of the aggregate tier rule
  aggregateFindings = {"aggregateTier": aggregateTier, "usedListedSubstances": usedListedSubstances, "flag": flag, "flaggedSubstances": flaggedSubstances}
  return aggregateFindings

def deftier(item):

  """
    takes a single substance (item) from the inventory and returns it's tier
    The function reads the item's chemid to find the thresholds in the database
    item must have the followings fields:
    qty, type, chemid 
  """

  try:
    qty = float(item["qty"])
    if item['chemtype']=="named":
      for substance in namedSubstances:
        if int(item["chemid"]) == int(substance["chemid"]):
          if qty > substance["tier3"]:
            return 3
          elif qty > substance["tier2"]:
            return 2
          elif qty > substance["tier1"]:
            return 1
          else:
            return 0
    elif item["chemtype"]=="listed":
      for substance in listedSubstances:
        if int(item["chemid"]) == int(substance["chemid"]) or substance['desc'] == item['category']:
          if qty > substance["tier3"]:
            return 3
          elif qty > substance["tier2"]:
            return 2
          elif qty > substance["tier1"]:
            return 1
          else:
            return 0
  except Exception as e:
    errorstring = str(traceback.print_exc())
    errorstring = errorstring + str(e) + str(item)
    ReportError(errorstring)
    return 0



def convertNumberToWord(arg):
  """
    Converts all tier numbers to words 0=none,1=low,2=medium,3=high.
    arg can be int, string, list, list of dict's or dict.
    int/string will return string.
    list will return list of strings.
    dicts will return dict with all values that are ints between 0 and 3 converted to words
  """

  #actual converter
  NumberToWord = {
    3: "High",
    2: "Medium",
    1: "Low",
    0: "None"
  }
  #number as integer
  try:
    if type(arg) is int and arg in NumberToWord.keys():
      return str(NumberToWord[arg])
    #number as string/float
    elif type(arg) is str or type(arg) is float and int(arg) in NumberToWord.keys():
      return str(NumberToWord[int(arg)])
    #object with tier values. Attempt to parse numbers 1-3 as strings to int
    elif type(arg) is dict:
      for keyname in arg.keys():
        if arg[keyname] in NumberToWord.keys():
          arg[keyname] = NumberToWord[arg[keyname]]
        elif int(arg[keyname]) in NumberToWord.keys():
          arg[keyname] = NumberToWord[int(arg[keyname])]
    #list of objects with tier values. attempt to parse numbers 1-3 as strings to int
    elif type(arg) is list and type(arg[0]) is dict:
      for chem in arg:
        for keyname in chem.keys():
          if chem[keyname] in NumberToWord.keys():
            chem[keyname] = NumberToWord[chem[keyname]]
          elif int(chem[keyname]) in NumberToWord.keys():
            chem[keyname] = NumberToWord[int(chem[keyname])]
    #list of numbers or list of numbers as strings/floats
    elif type(arg) is list and type(arg[0]) is not dict:
      for chem in arg:
        if type(chem) is not int:
          integer = int(chem)
          string = NumberToWord[integer]
          chem = string
        elif chem in NumberToWord.keys():
          chem = NumberToWord[chem]
    return arg
  except:
    return arg

def RemoveDuplicates(arr):
  newarr = []
  for item in arr:
    if item not in newarr:
      newarr.append(item)
  return newarr

def Process(newEntry):
  """
    Function used for processing new additions to inventory
  """
  print("newEntry", newEntry)
  try:
    #named substance
    if newEntry["chemtype"] == "named":
      #based on the current active dropdown on the addnew page, search for this substance in the namedSubstances DB by that field
      if "field" in newEntry.keys():
        field = newEntry["field"]
      for chem in namedSubstances:
        if newEntry[field] == chem[field] or int(newEntry["chemid"]) == int(chem["chemid"]) or newEntry["name"] == chem["name"]:
          #assign all the values of the substance from the DB
          for chemkey in chem.keys():
            newEntry[chemkey] = chem[chemkey]
          #attempt to update the hphrases if there are none in the DB
          try:
            if newEntry["hazardPhrases"] == "" or len(newEntry["hazardPhrases"]) < 1:
              manualgetresults = manualget(chem)
              newEntry["category"] = MasterCategoryController(manualgetresults["hazardPhrases"], manualgetresults["chemid"])
            else:
              newEntry["category"] = MasterCategoryController(chem["hazardPhrases"], chem["chemid"])
            if newEntry["category"] == False:
              newEntry["flag"] = True
              newEntry["category"] = "Undetermined"
          except:
            newEntry["flag"] = True
            newEntry["category"] = "Undetermined"
          break
    
    #listed substance
    else:
      #substance was added by category, create a name
      if newEntry["name"] == newEntry["chemid"] or newEntry['field'] == "category":
        for listedSubstance in listedSubstances:
          if int(newEntry["chemid"]) == int(listedSubstance["chemid"]):
            newEntry["category"] = listedSubstance["desc"]
            newEntry["name"] = f"Group {listedSubstance['desc'][0]} substance"
      else:
        #parse the hphrases from a string to an array, in case they were pulled manually from external DB
        if len(newEntry["hazardPhrases"]) > 0 and newEntry["hazardPhrases"] != "" and newEntry["hazardPhrases"] != []:
          if type(newEntry["hazardPhrases"]) is not list:
            hphrasestr = json.dumps(newEntry["hazardPhrases"])
            hPhraseArray = stringsearch(hphrasestr,"H")
            newEntry["hazardPhrases"] = hPhraseArray
        
        #The class wasn't manually selected; update the category
        if int(newEntry["chemid"]) > 304:
          newEntry["category"] = MasterCategoryController(hPhraseArray, newEntry["chemid"])
        else:
          newEntry["category"] = CategoryFinder(hPhraseArray,"desc")
          newEntry["chemid"] = CategoryFinder(hPhraseArray,"chemid")
  except Exception as e:
    errorstring = str(traceback.print_exc())
    errorstring = errorstring + str(e) + str(newEntry)
    ReportError(errorstring)
  finally:
    return newEntry

def manualget(entry):
  entry["searchtype"] = "name"
  entrykeys = entry.keys()
  if "chemid" in entrykeys and entry['chemid'] < 1000000:
    entry["searchtype"] = "chemid"
    tryThisFirst = Call2(entry['chemid'])
    if tryThisFirst != False:
      return tryThisFirst
  elif "CAS" in entrykeys and entry["CAS"] != "":
    entry["searchtype"] = "CAS"
  elif "UN" in entrykeys and entry["UN"] != "":
    entry["searchtype"] = "UN"

  # check if substance not named substances database
  #CALL 1

  # search by CAS
  if entry["searchtype"] == "CAS":
    print('Searching by CAS')
    cas = entry["CAS"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/xref/rn/{cas}/json"

  #search by UN number
  elif entry["UN"] == "UN":
    print('Searching by UN Number')
    un = entry["field"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/UN%20{un}/json"

  # search by substance name
  else:
    print('Searching by substance name')
    substance = entry["field"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"

  response = requests.get(query)
  queryAnswer = json.loads(response.content)
  print("Response 1 received")
  print(queryAnswer)
  check1 = stringsearch(json.dumps(queryAnswer),"fault")
  #parse the response
  if check1 == "NotFound":
    #call 1b
    print('No results found with CAS. Searching by substance name')
    substance = entry["field"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"
    response = requests.get(query)
    queryAnswer = json.loads(response.content)
    print("Response 1b received")
    print(queryAnswer)
    check1b = stringsearch(json.dumps(queryAnswer),"fault")
    if check1b == "NotFound":
      return False
    elif check1b == "OK":
      cid = stringsearch(json.dumps(queryAnswer), "cid")
      print("CID found: ", cid)
  
  elif check1 == "OK":
    cid = stringsearch(json.dumps(queryAnswer), "cid")
    print("CID found: ", cid)

  tryThisNow = Call2(cid)
  return tryThisNow
  

def Call2(cid):
  #call 2
  query2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=GHS classification"
  print("query2: ", query2)
  response2 = requests.get(query2)
  queryAnswer2 = json.loads(response2.content)
  print("response2 received")
  check2 = stringsearch(json.dumps(queryAnswer2),"fault")
 
  if check2 == "OK":
    hazardPhrases = stringsearch(json.dumps(queryAnswer2), "H")
    recordTitle = stringsearch(json.dumps(queryAnswer2), "RT")
    if recordTitle != "None" and hazardPhrases != []:
      findings = {"hazardPhrases": hazardPhrases, "chemid": cid}
      print(findings)
      return findings
    else:
      return False
  elif check2 == "NotFound":
    return False