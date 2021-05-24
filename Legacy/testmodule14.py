from listedSubstancesModule import listedSubstances

def CompareStrings(hcats):
  
  for listedSub in listedSubstances:
    correct = 0
    for dbhcat in listedSub["hazardCategories"]:
      if type(dbhcat) == list:
        i = 0
        j = 0
        dhbcatlength = len(dbhcat)
        for i in range(dhbcatlength):
          checkdigit = dbhcat[dhbcatlength-1]
          if type(checkdigit) is int and checkdigit > 0:
          #search for word like acute or toxic
            if type(dbhcat[i]) is str:
              if hcats[j].find(dbhcat[i]) == -1:
                j = j + 1
                i = 0
                correct = 0
              elif hcats[j].find(dbhcat[i]) > 0:
                i = i+1
            #search for category number
            elif type(dbhcat[i]) is int:
              if hcats[j].find(str(dbhcat[i])) == -1:
                j = j + 1
                i = 0
                correct = 0
              elif hcats[j].find(str(dbhcat[i])) > 0:
                i = i+1
          elif type(checkdigit) is list:
            if type(dbhcat[i]) is str:
              if hcats[j].find(dbhcat[i]) == -1:
                j = j + 1
                i = 0
                correct = 0
              elif hcats[j].find(dbhcat[i]) > 0:
                i = i+1
            #final index of hazardCategories is array of numbers
            elif i == checkdigit:
              checkDigitArrLength = len(checkdigit)
              for k in range(checkDigitArrLength):
                if hcats[j].find(str(dbhcat[i][k])) > 0:
                  i = i+1
              if i == checkdigit:
                j = j + 1
                i = 0
                correct = 0
          elif checkdigit == 0:
            if hcats[j].find(str(dbhcat[i])) == -1:
              i = i+1
            elif hcats[j].find(str(dbhcat[i])) > 0:
              j = j + 1
              i = 0
              correct = 0

        #we've arrived at the end of hazardcategories list
        if i == len(dbhcat):
          if "hazardCategoriesKeyword" in listedSub.keys():
            keyword = listedSub["hazardCategoriesKeyword"]
            #if the keyword specifies a number of match required
            if type(keyword) is int:
              correct = correct + 1
              if correct >= keyword:
                return listedSubstances["desc"]
            #the keyword requires ALL matches
            elif keyword == "and":
              correct = correct + 1            
            #the keyword requires any single category
            elif keyword == "or":
              return listedSubstances["desc"]
          else:
            correct = correct + 1

        #all matched found
        if correct >= len(listedSub["hazardCategories"]):
          return listedSubstances["desc"]
      else:
        print(listedSub["desc"] + " not checked.")
  #all substances and categories checked, but no viable matches found
  if i == len(dbhcat) and j == len(hcats) and correct < len(listedSub["hazardCategories"]):
    return None
    
hcats = ['Carc. 1A', 'Acute Tox. 3 *', 'Acute Tox. 3 *', 'Aquatic Acute 1', 'Aquatic Chronic 1', 'Acute Tox. 2 (76%)', 'Acute Tox. 3 (24%)', 'Acute Tox. 3 (100%)', 'Carc. 1A (100%)', 'Aquatic Acute 1 (100%)', 'Aquatic Chronic 1 (100%)', 'Acute toxicity - category 3', 'Acute toxicity - category 4', 'Carcinogenicity - category 1A', 'Germ cell mutagenicity - category 2', 'Specific target organ toxicity (repeated exposure) - category 2', 'Hazardous to the aquatic environment (acute) - category 1', 'Hazardous to the aquatic environment (chronic) - category 1', 'Skin corrosion - category 1', 'Acute toxicity (Dermal) - Category 2', 'Respiratory sensitization - Category 2', 'Reproductive toxicity - Category 1A', 'Specific target organ toxicity - Single exposure - Category 2', 'Specific target organ toxicity - Repeated exposure - Category 1 (digestive system, circulatory system, nervous system, blood system, respiratory system, skin, kidney, liver)', 'Aspiration hazard - Category 1 (digestive system, circulatory system, nervous system, kidney, liver, blood system, respiratory system, skin)', 'Acute toxicity (Dermal) - Category 2', 'Reproductive toxicity - Category 1A', 'Specific target organ toxicity - Repeated exposure - Category 1 (gastrointestinal tract, circulatory system, nervous system, blood system, respiratory system, skin, kidney, bone marrow, liver)', 'Aspiration hazard - Category 1 (respiratory system, skin, liver, cardiovascular system)', 'Hazardous to the aquatic environment (Long-term) - Category 3', 'Hazardous to the ozone layer - Category 3']


result = CompareStrings(hcats)
print(result)