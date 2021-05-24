from listedSubstancesModule import listedSubstances

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
      print("Not checking " + listedSub["desc"])