import re
import json
import hphrases

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

def checkCAS(arg1):
  result = re.search(r"[\d]{1,5}-[\d]{1,5}-[\d]{1,5}", arg1)
  return result

def getnums(x):
  """
    Extracts numbers from a string (x)
  """
  listresults = re.search(r"[0-9]+", x)
  return listresults[0]


chemlist

def findattribs(param1):

  """
    Small function for finding attributes of a listed substance based on the chemid (param1)
  """

  print("findattribs", param1)
  for chem in chemlist:
    if param1 == chem["chemid"]:
      return chem

def assessment(inv):

  """
    Full inventory (inv) assessment assessment.
    Determined individual tier
    if individual tier = 0, also determines aggregate tier

    returns an dict of results
  """

#set up final variable
  results = {"indTier" : 0, "aggregateTier": 0, "finalTier": 0}
  
  #individual tiers
  for item in inv:
    item["tier"] = deftier(item)
    if item["tier"] > results["indTier"]:
      results["indTier"] = item["tier"]
  if results["indTier"] > 0:
    results["finalTier"] = results["indTier"]
  
  #calculate the aggregate rules
  aggregateFindings = AggregateAssessment(inv)
  results["aggregateTier"] = aggregateFindings[0]
  results["usedListedSubstances"] = aggregateFindings[1]
  
  if results["aggregateTier"] > results["finalTier"]:
    results["finalTier"] = results["aggregateTier"]

  print(results)
  return results

def AggregateAssessment(inv):
  usedListedSubstances = {"A": 0, "B": 0, "C": 0}
  aggregateTier = 3
  done = False

  while done == False:
    usedListedSubstances["A"] = 0
    usedListedSubstances["B"] = 0
    usedListedSubstances["C"] = 0
    for item in inv:
      if item['chemtype']=="named":
        for substance in MainDB:
          if int(item["chemid"]) == int(substance["chemid"]):
            currenttier = "tier" + aggregateTier
            qx = float(item["qty"]) / float(substance[currenttier])
            rule = hphrases.RuleFinder(item)
            if rule != 0:
              usedListedSubstances[rule] = float(usedListedSubstances[rule]) + qx
            else:
              item.flag = True            
      elif item['chemtype']=="listed":
        for substance in listedSubstances:
          if int(item["chemid"]) == int(substance["chemid"]):
            qx = float(item["qty"]) / float(substance[currenttier])
            rule = hphrases.RuleFinder(item)
            if rule != 0:
              usedListedSubstances[rule] = float(usedListedSubstances[rule]) + qx
            else:
              item.flag = True
    for sub in usedListedSubstances.keys():
      if usedListedSubstances[sub] >= 1: 
        done = True

    if aggregateTier > 0 and done == False:
      aggregateTier = aggregateTier-1
    if aggregateTier == 0:
      done = True

  #update the overall/final tier based on the findings of the aggregate tier rule
  for sub in usedListedSubstances.keys():
    usedListedSubstances[sub] = round(usedListedSubstances[sub], 2)

  aggregateFindings = [aggregateTier, usedListedSubstances]
  return aggregateFindings

def deftier(item):

  """
    takes a single substance (item) from the inventory and returns it's tier
    The function reads the item's chemid to find the thresholds in the database
    item must have the followings fields:
    qty, type, chemid 
  """

  qty = float(item["qty"])
  if item['chemtype']=="named":
    for substance in MainDB:
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
      if int(item["chemid"]) == int(substance["chemid"]):
        if qty > substance["tier3"]:
          return 3
        elif qty > substance["tier2"]:
          return 2
        elif qty > substance["tier1"]:
          return 1
        else:
          return 0

def listedtier(item):
  for substance in listedSubstances:
    if int(item["chemid"]) == substance["chemid"]:
      return float(item["qty"]) / int(substance["tier1"])

def convertNumberToWord(arg):
  """
    Converts all tier numbers to words
    arg can be string, list or dict
  """
  if type(arg) is list or type(arg) is dict:
    for chem in arg:
      if int(chem["tier"]) == 3:
        chem["tier"] == "High"
      elif int(chem["tier"]) == 2:
        chem["tier"] == "Medium"
      elif int(chem["tier"]) == 1:
        chem["tier"] == "Low"
      elif int(chem["tier"]) == 0:
        chem["tier"] == "None"
      else:
        pass
  elif type(arg) is str or type(arg) is int:
    if int(arg) == 3:
      arg == "High"
    elif int(arg) == 2:
      arg == "Medium"
    elif int(arg) == 1:
      arg == "Low"
    elif int(arg) == 0:
      arg == "None"
    else:
      pass
  
  return arg