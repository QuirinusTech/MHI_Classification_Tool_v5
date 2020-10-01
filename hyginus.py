

"""chemlist = ["Ammonia anhydrous","Ammonium nitrate-1","Ammonium nitrate-2","Ammonium nitrate-3","Ammonium nitrate-4","Potassium nitrate-1","Potassium nitrate-2","Arsenic pentoxide", "arsenic (V) acid and/or salts","Arsenic trioxide", "Arsenious (III) acid and/or salts", "Bromine", "Chlorine", "Nickel compounds", "Ethyleneimine", "Fluorine", "Formaldehyde", "Hydrogen", "Hydrogen chloride", "Hydrogen fluoride", "Lead alkyls", "LPG", "Acetylene", "Ethylene oxide", "Propylene oxide", "Methanol", "Methylenebis", "Methyl isocyanate", "Oxygen", "Toluene diisocyanate", "Carbonyl dichloride", "Arsenic trihydride", "Phosphorus trihydride", "Sulphur dichloride", "Sulphur dioxide", "Sulphur trioxide"]"""


# 0id, 1CAS, 2substance, 3tier1, 4tier2, 5tier3, 6type, 7class, 8tooltip
bigDatabase = [
[1, "", "Carcinogens", 0.05, 0.5, 2, "named", "", "Carcinogens at concentration above 5%; *-link to sheet 2;"],
[2, "74-86-2 ", "Acetylene", 0.5, 5, 50, "named", "", ""],
[3, "7664-41-7", "Ammonia anhydrous", 5, 50, 200, "named", "", ""],
[4, "", "Ammonium nitrate-1", 500, 5, 10, "named", "", "Ammonium nitrate fertilisers capable of self-sustaining decomposition."],
[5, "", "Ammonium nitrate-2", 125, 1, 5, "named", "", "Ammonium nitrate: fertiliser grade."],
[6, "", "Ammonium nitrate-3", 35, 350, 3, "named", "", "Ammonium nitrate: technical grade."],
[7, "", "Ammonium nitrate-4", 1, 10, 50, "named", "", "Ammonium nitrate (10/50): 'off-specs' material and fertilisers not satisfying the detonation resistance test."],
[8, "", "Arsenic (V) acid and/or salts", 0.1, 1, 2, "named", "", ""],
[9, "1303-28-2", "Arsenic pentoxide", 0.1, 1, 2, "named", "", ""],
[10, "1327-53-3", "Arsenic trioxide", 0.01, 0.1, 0.1, "named", "", ""],
[11, "7726-95-6", "Bromine", 2, 20, 100, "named", "", ""],
[12, "75-44-5", "Carbonyl dichloride", 0.03, 0.3, 0.75, "named", "", ""],
[13, "", "Chlorine", 1, 10, 25, "named", "", ""],
[14, "75-21-8 ", "Ethylene oxide", 0.5, 5, 50, "named", "", ""],
[15, "151-56-4 ", "Ethyleneimine", 1, 10, 20, "named", "", ""],
[16, "7782-41-4 ", "Fluorine", 1, 10, 20, "named", "", ""],
[17, "50-00-0 ", "Formaldehyde", 0.5, 5, 50, "named", "", ""],
[18, "1333-74-0 ", "Hydrogen", 0.5, 5, 50, "named", "", ""],
[19, "7647-01-0 ", "Hydrogen chloride", 2.5, 25, 250, "named", "", ""],
[20, "", "Hydrogen fluoride", 0.5, 5, 20, "named", "", ""],
[21, "", "Lead alkyls", 0.5, 5, 50, "named", "", ""],
[22, "", "LPG", 5, 50, 200, "named", "", ""],
[23, "67-56-1", "Methanol", 50, 500, 5, "named", "", ""],
[24, "624-83-9", "Methyl isocyanate", 15, 0.15, 0.15, "named", "", ""],
[25, "", "Nickel compounds", 0.1, 1, 1, "named", "", ""],
[26, "7782-44-7", "Oxygen", 20, 200, 2, "named", "", ""],
[27, "", "Petroleum products", 250, 2500, 25000, "named", "", "gasolines ; naphthas; kerosenes (including jet fuels); gas oils (including diesel fuels; home heating oils and gas oil blending streams)"],
[28, "7803-51-2 ", "Phosphorus trihydride", 0.02, 0.2, 1, "named", "", ""],
[29, "", "Polychlorodibenzofurans / polychlorodibenzodioxins (including TCDD)", 1, 0.001, 0.001, "named", "", "* - Link to Note 7 Table"],
[30, "", "Potassium nitrate-1", 500, 5, 10, "named", "", "Potassium nitrate (5 000/10 000): composite potassium nitrate-based fertilisers composed of potassium nitrate in prilled/granular form."],
[31, "", "Potassium nitrate-2", 125, 1, 5, "named", "", "Potassium nitrate (1 250/5 000): composite potassium nitrate-based fertilisers composed of potassium nitrate in crystalline form."],
[32, "75-56-9 ", "Propylene oxide", 0.5, 5, 50, "named", "", ""],
[33, "10545-99-0", "Sulphur dichloride", 0.1, 1, 1, "named", "", ""],
[34, "", "Sulphur dioxide", 0.5, 5, 20, "named", "", ""],
[35, "7446-11-9", "Sulphur trioxide", 1.5, 15, 75, "named", "", ""],
[201, "", "*", 0.5, 5, 20, "listed", "Very ", "very toxic"],
[202, "", "*", 5, 50, 200, "listed", "Toxic", "TOXIC (R23 as per Note 4)"],
[203, "", "*", 5, 50, 200, "listed", "Oxidising", "OXIDISING"],
[204, "", "*", 500, 5, 50, "listed", "Flammable", "flammable liquids - substances and preparations having a flash point equal to or greater than 23�C and less than or equal to 60�C (dange"],
[205, "", "*", 5, 50, 200, "listed", "Highly Flammable", "substances and preparations which may become hot and finally catch fire in contact with air at ambient temperature without any input of "],
[206, "", "*", 500, 5, 50, "listed", "Highly Flammable", "substances and preparations having a flash point lower than 23�C and which are not extremely flammable (danger group II; SANS 10228);"],
[207, "", "*", 1, 10, 50, "listed", "Extremely Flammable", "liquid substances and preparations which have a flash point lower than 0�C and the boiling point (or; in the case of a boiling range; th"],
[208, "", "*", 10, 100, 200, "listed", "Hazardous (Environment)", "HAZARDOUS FOR THE ENVIRONMENT risk phrases: (a) Very toxic to aquatic organisms"],
[209, "", "*", 20, 200, 500, "listed", "Hazardous (Environment)", "HAZARDOUS FOR THE ENVIRONMENT risk phrases: (b) Toxic to aquatic organisms: may cause long term adverse effects in the aquatic environme"],
[210, "", "*", 10, 100, 500, "listed", "Violent Reaction", "ANY CLASSIFICATION not covered by those given above in combination with risk phrases: (a) Reacts violently with water"],
[211, "", "*", 5, 50, 200, "listed", "Gas Release", "ANY CLASSIFICATION not covered by those given above in combination with risk phrases: (b) In contact with water; liberates toxic gas"]
]

listedSubstances = [
  {'chemid': 201, 'tier1': 0.5, 'tier2': 5, 'tier3': 20, 'class': 'Very toxic ', 'tooltip': 'very toxic'},
  {'chemid': 202, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Toxic', 'tooltip': 'TOXIC (R23 as per Note 4)'},
  {'chemid': 203, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Oxidising', 'tooltip': 'OXIDISING'},
  {'chemid': 204, 'tier1': 500, 'tier2': 5000, 'tier3': 50000, 'class': 'Flammable', 'tooltip': 'flammable liquids - substances and preparations having a flash point equal to or greater than 23�C and less than or equal to 60�C (dange'},
  {'chemid': 205, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Highly Flammable', 'tooltip': 'substances and preparations which may become hot and finally catch fire in contact with air at ambient temperature without any input of '},
  {'chemid': 206, 'tier1': 500, 'tier2': 5000, 'tier3': 50000, 'class': 'Highly Flammable', 'tooltip': 'substances and preparations having a flash point lower than 23�C and which are not extremely flammable (danger group II; SANS 10228);'},
  {'chemid': 207, 'tier1': 1, 'tier2': 10, 'tier3': 50, 'class': 'Extremely Flammable', 'tooltip': 'liquid substances and preparations which have a flash point lower than 0�C and the boiling point (or; in the case of a boiling range; th'},
  {'chemid': 208, 'tier1': 10, 'tier2': 100, 'tier3': 200, 'class': 'Hazardous (Environment)', 'tooltip': 'HAZARDOUS FOR THE ENVIRONMENT risk phrases: (a) Very toxic to aquatic organisms'},
  {'chemid': 209, 'tier1': 20, 'tier2': 200, 'tier3': 500, 'class': 'Hazardous (Environment)', 'tooltip': 'HAZARDOUS FOR THE ENVIRONMENT risk phrases: (b) Toxic to aquatic organisms: may cause long term adverse effects in the aquatic environme'},
  {'chemid': 210, 'tier1': 10, 'tier2': 100, 'tier3': 200, 'class': 'Violent Reaction', 'tooltip': 'ANY CLASSIFICATION not covered by those given above in combination with risk phrases: (a) Reacts violently with water'},
  {'chemid': 211, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Gas Release', 'tooltip': 'ANY CLASSIFICATION not covered by those given above in combination with risk phrases: (b) In contact with water; liberates toxic gas'}
  ]

#pure list of chemicals
chemlist = [
    {'id': 1, 'CAS': '', 'name': 'Carcinogens', 'type': 'named', 'class': '', 'tooltip': 'Carcinogens at concentration above 5%; *-link to sheet 2;'},
    {'id': 2, 'CAS': '74-86-2 ', 'name': 'Acetylene',
        'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 3, 'CAS': '7664-41-7', 'name': 'Ammonia anhydrous',
        'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 4, 'CAS': '', 'name': 'Ammonium nitrate-1', 'type': 'named', 'class': '',
        'tooltip': 'Ammonium nitrate fertilisers capable of self-sustaining decomposition.'},
    {'id': 5, 'CAS': '', 'name': 'Ammonium nitrate-2', 'type': 'named',
        'class': '', 'tooltip': 'Ammonium nitrate: fertiliser grade.'},
    {'id': 6, 'CAS': '', 'name': 'Ammonium nitrate-3', 'type': 'named',
        'class': '', 'tooltip': 'Ammonium nitrate: technical grade.'},
    {'id': 7, 'CAS': '', 'name': 'Ammonium nitrate-4', 'type': 'named', 'class': '',
        'tooltip': "Ammonium nitrate (10/50): 'off-specs' material and fertilisers not satisfying the detonation resistance test."},
    {'id': 8, 'CAS': '',
        'name': 'Arsenic (V) acid and/or salts', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 9, 'CAS': '1303-28-2', 'name': 'Arsenic pentoxide',
        'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 10, 'CAS': '1327-53-3', 'name': 'Arsenic trioxide', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 11, 'CAS': '7726-95-6', 'name': 'Bromine', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 12, 'CAS': '75-44-5', 'name': 'Carbonyl dichloride', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 13, 'CAS': '', 'name': 'Chlorine', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 14, 'CAS': '75-21-8 ', 'name': 'Ethylene oxide', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 15, 'CAS': '151-56-4 ', 'name': 'Ethyleneimine', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 16, 'CAS': '7782-41-4 ', 'name': 'Fluorine', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 17, 'CAS': '50-00-0 ', 'name': 'Formaldehyde', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 18, 'CAS': '1333-74-0 ', 'name': 'Hydrogen', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 19, 'CAS': '7647-01-0 ', 'name': 'Hydrogen chloride', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 20, 'CAS': '', 'name': 'Hydrogen fluoride', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 21, 'CAS': '', 'name': 'Lead alkyls', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 22, 'CAS': '', 'name': 'LPG', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 23, 'CAS': '67-56-1', 'name': 'Methanol', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 24, 'CAS': '624-83-9', 'name': 'Methyl isocyanate', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 25, 'CAS': '', 'name': 'Nickel compounds', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 26, 'CAS': '7782-44-7', 'name': 'Oxygen', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 27, 'CAS': '', 'name': 'Petroleum products', 'type': 'named', 'class': '', 'tooltip': 'gasolines ; naphthas; kerosenes (including jet fuels); gas oils (including diesel fuels; home heating oils and gas oil blending streams)'},
    {'id': 28, 'CAS': '7803-51-2 ', 'name': 'Phosphorus trihydride', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 29, 'CAS': '', 'name': 'Polychlorodibenzofurans / polychlorodibenzodioxins (including TCDD)', 'type': 'named', 'class': '', 'tooltip': '* - Link to Note 7 Table'},
    {'id': 30, 'CAS': '', 'name': 'Potassium nitrate-1', 'type': 'named', 'class': '', 'tooltip': 'Potassium nitrate (5 000/10 000): composite potassium nitrate-based fertilisers composed of potassium nitrate in prilled/granular form.'},
    {'id': 31, 'CAS': '', 'name': 'Potassium nitrate-2', 'type': 'named', 'class': '', 'tooltip': 'Potassium nitrate (1 250/5 000): composite potassium nitrate-based fertilisers composed of potassium nitrate in crystalline form.'},
    {'id': 32, 'CAS': '75-56-9 ', 'name': 'Propylene oxide', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 33, 'CAS': '10545-99-0', 'name': 'Sulphur dichloride', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 34, 'CAS': '', 'name': 'Sulphur dioxide', 'type': 'named', 'class': '', 'tooltip': ''},
    {'id': 35, 'CAS': '7446-11-9', 'name': 'Sulphur trioxide', 'type': 'named', 'class': '', 'tooltip': ''}
]

"""for chem in bigDatabase:
  chemlist.append({"id": chem[0], "CAS": chem[1], "name": chem[2], "type": chem[6], "class": chem[7], "tooltip": chem[8]})
print(chemlist)"""

def findattribs(param1):
  print("findattribs", param1)
  for chem in chemlist:
    if param1 == chem["id"]:
      return chem

def assessment(inv):
  #cumulative

  indtier = 0
  for item in inv:
    item["tier"] = deftier(item)
    if item["tier"] > indtier:
      indtier = item["tier"]

  usedlistedsubs = []
  cumultier = 0
  for listedsub in listedSubstances:
    currentTier = 0
    for item in inv:
      if item["type"]=="listed" and listedsub["chemid"] == int(item["chemid"]):
        currentTier = currentTier + listedtier(item)
    if currentTier > 0:
      if currentTier > cumultier:
        cumultier = currentTier
      usedlistedsubs.append({"chemid": listedsub["chemid"], "class": listedsub["class"], "tier": currentTier})
  results = {
    "usedlistedsubs": usedlistedsubs,
    "cumultier": cumultier,
    "indtier": indtier,
    "finaltier": max(cumultier, indtier)
  }
  print(results)
  return results

def deftier(item):
  qty = int(item["qty"])
  if item['type']=="named":
    for chem in bigDatabase:
      if int(item["id"]) == chem[0]:
        if qty > chem[5]:
          return 3
        elif qty > chem[4]:
          return 2
        elif qty > chem[3]:
          return 1
        else:
          return 0
  elif item["type"]=="listed":
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
      return int(item["qty"]) / int(substance["tier1"])