from re import sub
import requests
import json


listedSubstances = [
    {
        "chemid": 101,
        "tier1": 5,
        "tier2": 5,
        "tier3": 20,
        "desc": "H1 Acute Toxic Category 1",
        "hazardPhrases": ["H300", "H310", "H330"],
        "hazardCategories": [
            ["Acute", "Toxic", 1]
        ],
        "hazardCategoriesKeyword": 1,
        "tooltip": "All exposure routes"
    },
    {
        "chemid": 102,
        "tier1": 15,
        "tier2": 50,
        "tier3": 200,
        "desc": "H2 Acute Toxic (Inhalation)",
        "hazardPhrases": ["H331", "H301"],
        "hazardCategories": [
            ["Acute","Toxic", 2],
            ["Acute","Toxic", "inhalation", 3]
        ],
        "hazardCategoriesKeyword": "or",
        "tooltip": "Category 2, all exposure routes. \n Category 3, inhalation exposure route."
    },
    {
        "chemid": 103,
        "tier1": 15,
        "tier2": 50,
        "tier3": 200,
        "desc": "H3 STOT Category 1, SE STOT",
        "hazardPhrases": ["H370"],
        "hazardCategories": [
            ["Specific Target Organ Toxicity", "single exposure", 1]
        ],
        "hazardCategoriesKeyword": 1,
        "tooltip": "Specific Target Organ Toxicity. Category 1, Single Exposure SE STOT"
    },
    {
        "chemid": 201,
        "tier1": 2.5,
        "tier2": 10,
        "tier3": 50,
        "desc": "P2 Flammable Gases",
        "hazardPhrases": ["H220", "H221"],
        "hazardCategories": [
            ["Flammable Gases", [1,2]],
        ],
        "hazardCategoriesKeyword": 1,
        "tooltip": "Flammable gases, Category 1 or 2"
    },
    {
        "chemid": 202,
        "tier1": 50,
        "tier2": 150,
        "tier3": 500,
        "desc": "P3a Flammable Aerosols",
        "hazardPhrases": ["H222", "H223"],
        "hazardCategories": [
            ["Flammable Aerosols", [1,2]],
            ["Flammable Gases", [1,2]],
            ["Flammable Liquids", 1]
        ],
        "hazardCategoriesKeyword": 2,
        "tooltip": "Flammable aerosols Category 1 or 2, containing flammable gases Category 1 or 2 or flammable liquids Category 1"
    },
    {
        "chemid": 203,
        "tier1": 1250,
        "tier2": 5000,
        "tier3": 50000,
        "desc": "P3b Flammable Aerosols",
        "hazardPhrases": [],
        "hazardCategories": [
            ["Flammable Aerosols", [1,2]],
            ["Flammable Gases", 0],
            ["Flammable Liquids", 0]
        ],
        "hazardCategoriesKeyword": "and",
        "tooltip": "Flammable’ aerosols Category 1 or 2, not containing flammable gases Category 1 or 2 nor flammable liquids category 1"
    },
    {
        "chemid": 204,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P4 Oxidising Gases",
        "hazardPhrases": ["H270"],
        "hazardCategories": [
            ["Oxidising Gases", 1]
        ],
        "hazardCategoriesKeyword": 1,
        "tooltip": "Oxidising gases, Category 1"
    },
    {
        "chemid": 205,
        "tier1": 5,
        "tier2": 10,
        "tier3": 50,
        "desc": "P5a Flammable Liquids",
        "hazardPhrases": ["H224"],
        "hazardCategories": [
            ['Flammable Liquids',[1,2,3]]
        ],

        "tooltip": ""
    },
    {
        "chemid": 206,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P5b Flammable Liquids",
        "hazardPhrases": [],
        "hazardCategories": [
            ['Flammable Liquids',[1,2,3]]
        ],

        "tooltip": ""
    },
    {
        "chemid": 216,
        "tier1": 1250,
        "tier2": 5000,
        "tier3": 50000,
        "desc": "P5c Flammable Liquids",
        "hazardPhrases": ["H225", "H226"],
        "hazardCategories": [
            ["Flammable Liquids", [2,3]]
        ],

        "tooltip": "Flammable Liquids, Categories 2 or 3 not covered by P5a and P5b"
    },
    {
        "chemid": 207,
        "tier1": 5,
        "tier2": 10,
        "tier3": 50,
        "desc": "P6a Self-Reactive Substances and Mixtures and Organic Peroxides",
        "hazardPhrases": ["H240", "H241"],
        "hazardCategories": [
            {"classification": "", "category": 1}
        ],

        "tooltip": "Self-reactive substances and mixtures, Type A or B or organic peroxides, Type A or B"
    },
    {
        "chemid": 208,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P6b Self -Reactive Substances and Mixtures and Organic Peroxides",
        "hazardPhrases": ["H242"],
        "hazardCategories": [
            {"classification": "", "category": 1}
        ],

        "tooltip": "Self-reactive substances and mixtures, Type C, D, E or F or organic peroxides, Type C, D, E, or F"
    },
    {
        "chemid": 209,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P7 Pyrophoric Liquids and Solids",
        "hazardPhrases": ["H250"],
        "hazardCategories": [
            ["Pyrophoric Liquids and Solids", 1]
        ],

        "tooltip": "Pyrophoric Liquids and Solids, Category 1"
    },
    {
        "chemid": 210,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P8 Oxidising Liquids and Solids",
        "hazardPhrases": ["H271", "H272", "H273"],
        "hazardCategories": [
            ["Oxidising Liquids", [1,2,3]],
            ["Oxidising Solids", [1,2,3]]
        ],

        "tooltip": "Oxidising Liquids, Category 1, 2 or 3, or Oxidising Solids, Category 1, 2 or 3"
    },
    {
        "chemid": 301,
        "tier1": 40,
        "tier2": 100,
        "tier3": 500,
        "desc": "O1 Violent aqueous reaction.",
        "hazardPhrases": [],
        "hazardCategories": [
            {"classification": "", "category": 1}
        ],

        "tooltip": "Substances or mixtures that reacts violently with water"
    },
    {
        "chemid": 302,
        "tier1": 40,
        "tier2": 100,
        "tier3": 500,
        "desc": "O2 flammable gas emission on aqueous contact",
        "hazardPhrases": ["H260"],
        "hazardCategories": [
            {"classification": "", "category": 1}
        ],

        "tooltip": "Substances and mixtures which in contact with water emit flammable gases"
    },
    {
        "chemid": 303,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "O3 Toxic gas emission on aqueous contact",
        "hazardPhrases": [],
        "hazardCategories": [
            {"classification": "", "category": 1}
        ],

        "tooltip": "Substances or mixtures that liberates toxic gas when in contact with water."
    }
]

flammableLiquidWarning = ['This program only deals with flammable liquids that are stored below their boiling point.','Processing conditions where temperatures and pressures of flammable liquids are elevated may result in a higher hazard category.', 'Kindly contact ISHECON for further information.']


rules = {
  'H': [101, 102, 103],
  'P': [201, 202, 203, 204, 205, 206, 216, 207, 208, 209, 210],
  'O': [301, 302, 303]
}

hGroupHPhrases = []
for substance in listedSubstances:
  if substance["desc"][0] == "H":
    for hphrase in substance["hazardPhrases"]:
      hGroupHPhrases.append(hphrase)

pGroupHPhrases = []
for substance in listedSubstances:
  if substance["desc"][0] == "P":
    for hphrase in substance["hazardPhrases"]:
      pGroupHPhrases.append(hphrase)

def CheckIfFlammable(hazardPhrases):
  for hphrase in hazardPhrases:
    if hphrase in pGroupHPhrases:
      return True
  else:
    return False

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

def GetHazardCategories(arg):
    """
        using the cid as arg, returns a list of hazard categories
    """

    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{arg}/JSON?heading=Hazard%20classes%20and%20categories"
    response = requests.get(query)
    queryAnswer = json.loads(response.content)
    indexvalue = BreakItDown(queryAnswer)
    infoarray = indexvalue["Information"]
    hcats = []
    for obj in infoarray:
      for string in obj["Value"]["StringWithMarkup"]:
        hcats.append(string["String"])
    return hcats

#aggregaterule = {}
#for group in hgroups:
#  aggregaterule[group['chemid']] = 0

def CategoryFinder(hphraselist, field):
  
  """
    using an array of hphrases, finds the first match from the array in the hphrases group where the hphrase is found.
    return value is determined by the field argument, which can be either 'desc' (description) or 'chemid' (an id used to find other info on this substance in the database)
  """
  possiblegroups = []
  for hphrase in hphraselist:
    for group in listedSubstances:
      if hphrase in group["hazardPhrases"]:
        possiblegroups.append(group["chemid"])

  #assuming that the lowest number is the most severe ///flag///
  if field == "chemid":
    #precedence rules
    return min(possiblegroups)

  elif field == "desc":
    for desc in listedSubstances:
      if min(possiblegroups) == desc["chemid"]:
        return desc["desc"]

def NewHazardCategoryFinder(cid):
    """
        takes cid as arg
        returns category
    """
    hcats = GetHazardCategories(cid)
    result = ExtractHazardCategory(hcats)
    return result

def RuleFinder(item):
  """
    takes an item as an argument and returns the rule group in which a substance falls (a / b / c).
    item must have the following fields: type, chemid, hphrases
  """

  if item['chemtype'] == "named":
    for hphrase in item["hazardPhrases"]:
      if hphrase in hGroupHPhrases:
        return 'H'
    for hphrase in item["hazardPhrases"]:
      if hphrase in pGroupHPhrases:
        return 'P'
    for hphrase in item["hazardPhrases"]:  
      for listedSub in listedSubstances:
        if hphrase in listedSub["hazardPhrases"]:
          for rule in rules.keys():
            if listedSub["chemid"] in rules[rule]:
              return rule
  elif item['chemtype'] == "listed":
    for rule in rules.keys():
      if int(item["chemid"]) in rules[rule]:
        return rule
  else:
    return 0

def GetCorrectTarget(keyword, dbHcats):
  
  if type(keyword) is int:
    return keyword
  elif keyword == "or":
    return 1
  elif keyword == "and":
    return dbHcats

def ExtractHazardCategory(hcats):
  """
    hcats = list of hazard categories
    returns listedSubstance description
  """
  for listedSub in listedSubstances:
    if type(listedSub["hazardCategories"][0]) is not dict:
      #targets for match on substances category
      categoryMatches = 0
      if "hazardCategoriesKeyword" in listedSub.keys():
        categoryMatchesTarget = GetCorrectTarget(listedSub["hazardCategoriesKeyword"], len(listedSub["hazardCategories"]))
      else:
        categoryMatchesTarget = len(listedSub["hazardCategories"])
      fail = False

      for dbHcatString in listedSub["hazardCategories"]:
        for hcat in hcats:
          segmentMatches = 0
          hcat = hcat.lower()
          
          CheckDigitIndex = len(dbHcatString) - 1

          #check each individual section of the string
          for dbHcatStringSegment in dbHcatString:
            segmentMatchTarget = len(dbHcatString)
            #for strings
            if type(dbHcatStringSegment) is str:
              dbHcatStringSegment = dbHcatStringSegment.lower()
              if dbHcatStringSegment in hcat:
                segmentMatches = segmentMatches + 1
            #for arrays: any one of them will count
            elif type(dbHcatStringSegment) is list:
              for integer in dbHcatStringSegment:
                if str(integer) in hcat:
                  segmentMatches = segmentMatches + 1
            elif type(dbHcatStringSegment) is int and dbHcatStringSegment > 0:
              if str(dbHcatStringSegment) in hcat:
                segmentMatches = segmentMatches + 1

          #see if enough segments match to count as a full string match 
          #if the last item in the array is an int
          if type(dbHcatString[CheckDigitIndex]) is int:
            #the int is greater than zero
            if segmentMatches >= segmentMatchTarget and dbHcatString[CheckDigitIndex] != 0:
              categoryMatches = categoryMatches + 1
            #requirement is no matches
            elif segmentMatches >= CheckDigitIndex and dbHcatString[CheckDigitIndex] == 0:
              fail = True
          #default case, last item in array is an array of ints
          elif type(dbHcatString[CheckDigitIndex]) is list:
            if segmentMatches >= segmentMatchTarget:
              categoryMatches = categoryMatches + 1
      if categoryMatches >= categoryMatchesTarget and fail == False:
        return listedSub["desc"]
    else:
      pass
      #print\("Not checking " + listedSub["desc"])

def MasterCategoryController(hazardphrases, cid):
  """
    Primary Controller for determining category.
    chem.keys() must contain "hazardPhrases" and cid
  """
  if hazardphrases == None or hazardphrases == []:
    return NewHazardCategoryFinder(cid)
  else:
    category = CategoryFinder(hazardphrases, "desc")
    for hphrase in hazardphrases:
      if hphrase in hGroupHPhrases:
        return NewHazardCategoryFinder(cid)
    else:
      return category