arr1 = ["Acute", "Toxic", 3]

hcats = ['Carc. 1A', 'Acute Tox. 3 *', 'Acute Tox. 3 *', 'Aquatic Acute 1', 'Aquatic Chronic 1', 'Acute Tox. 2 (76%)', 'Acute Tox. 3 (24%)', 'Acute Tox. 3 (100%)', 'Carc. 1A (100%)', 'Aquatic Acute 1 (100%)', 'Aquatic Chronic 1 (100%)', 'Acute toxicity - inhalation category 3', 'Acute toxicity - category 4', 'Carcinogenicity - category 1A', 'Germ cell mutagenicity - category 2', 'Specific target organ toxicity (repeated exposure) - category 2', 'Hazardous to the aquatic environment (acute) - category 1', 'Hazardous to the aquatic environment (chronic) - category 1', 'Skin corrosion - category 1', 'Acute toxicity (Dermal) - Category 2', 'Respiratory sensitization - Category 2', 'Reproductive toxicity - Category 1A', 'Specific target organ toxicity - Single exposure - Category 2', 'Specific target organ toxicity - Repeated exposure - Category 1 (digestive system, circulatory system, nervous system, blood system, respiratory system, skin, kidney, liver)', 'Aspiration hazard - Category 1 (digestive system, circulatory system, nervous system, kidney, liver, blood system, respiratory system, skin)', 'Acute toxicity (Dermal) - Category 2', 'Reproductive toxicity - Category 1A', 'Specific target organ toxicity - Repeated exposure - Category 1 (gastrointestinal tract, circulatory system, nervous system, blood system, respiratory system, skin, kidney, bone marrow, liver)', 'Aspiration hazard - Category 1 (respiratory system, skin, liver, cardiovascular system)', 'Hazardous to the aquatic environment (Long-term) - Category 3', 'Hazardous to the ozone layer - Category 3']

for hcat in hcats:
  hcat = hcat.lower()
  required = 3
  found = 0
  for string in arr1:
    if type(string) is not str:
      string = str(string)
    string = string.lower()

    if string in hcat:
      #print(string + " found in " + hcat)
      found +=1
  #print("found " + str(found))
  #print("required " + str(required))
  #print("end of hcat " + hcat)
  if found == required:
    print("----------------FOUND! " + hcat)