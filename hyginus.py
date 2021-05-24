import re
import json

from werkzeug.exceptions import ServiceUnavailable
from listedSubstancesModule import listedSubstances, RuleFinder
from namedSubstancesModule import namedSubstances

def stringsearch(z,t):
  """
    Searches a given string (z) for one of the patterns patterns (t)
    
  """
  #print\("key to search by (t): ", t)

  #print\("stringsearch by t: ", t)
  if t == "H": #Hazard statements
    hazardphraseslist = re.findall(r"H[2-4]\d\d", z)
    results = []
    for i in hazardphraseslist:
      #print\(i)
      if i not in results:
        results.append(i)
    #print\("Response: ", results)
    return results
  elif t == "cid": #cid
    match = re.search(r"(\"cid\"\:\s*)([0-9]+)", z)
    if match is None:
       #print\("stringsearch", t, "No cid found")
       return "NotFound"
    else:
      #print\("Response: ", match.group(2))
      return match.group(2)
  elif t == "fault": #PUG errors
     match = re.search(r"(PUG[REST|VIEW].)([NotFound|Timeout])", z)
     #print\("Match value: ", match)
     if match is None:
       #print\("stringsearch", t, "No faults found")
       return "OK"
     else:
       #print\("fault found: ", match.group(2))
       return match.group(2)
  elif t == "RT": #Record Title
    match = re.search(r"(RecordTitle.\: [\'|\"])([A-Za-z\s*]+)([\'|\"])", z)
    if match is None:
      #print\("stringsearch", t, "Response: None")
      return None
    else:
      #print\("Response: ", match.group(2))
      return match.group(2)
  elif t == "UN":
    match = re.search(r"([\'|\"]UN[\s]?)(\d{4})([\'|\"],)", z)
    if match is None:
      #print\("stringsearch", t, "Response: None")
      return None
    else:
      #print\("UN Number: ", match.group(2))
      return match.group(2)
  elif t == "CAS":
    match = re.search(r"([0-9]{2,7}-[0-9]{2}-[0-9])", z)
    if match is None:
      #print\("stringsearch", t, "Response: None")
      return None
    else:
      #print\("CAS Number: ", match.group(1))
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
  results["flag"] = aggregateFindings[2]["flag"]
  results["flaggedSubstances"] = aggregateFindings[2]["flaggedSubstances"]
  #print\(results)
  return results

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

  aggregateFindings = [aggregateTier, usedListedSubstances, {"flag": flag, "flaggedSubstances": flaggedSubstances}]
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