import re
import json

def stringsearch(z,t):
  if t == "H":
    hazardphraseslist = re.findall(r"H[2-4]\d\d", z)
    results = []
    for i in hazardphraseslist:
      if i not in results:
        results.append(i)
    return
  elif t == "cid":
     match = re.search(r"(\"cid\"\:\s)([0-9]+)", z)
     return match.group(2)
  else:
    pass

def getnums(x):
  listresults = re.search(r"[0-9]+", x)
  return listresults[0]


# 0id, 1CAS, 2substance, 3tier1, 4tier2, 5tier3, 6type, 7class, 8tooltip
bigDatabase = [
[101, "", "Carcinogens", 0.05, 0.5, 2, "named", "", "Carcinogens at concentration above 5%: 4-Aminobiphenyl, Benzotrichloride, Benzidine, Chloromethyl ether, Chloromethyl methyl ether, 1,2-Dibromoethane, Diethyl sulphate, Dimethyl sulphate, Dimethylcarbamoyl Chloride, 1,2-Dibromo-3-chloropropane, 1,2-Dimethylhydrazine, Dimethylnitrosamine, Hexamethylphosphoric triamide, Hydrazine, 2-Naphthylamine, 2-Naphthylamine salts, 4-Nitrodiphenyl, 1,3-Propanesultone",""],
[6326, "74-86-2", "Acetylene", 0.5, 5, 50, "named", "", "", ["H220"]],
[222, "7664-41-7", "Ammonia anhydrous", 5, 50, 200, "named", "", "", ["H221", "H314", "H331", "H400"]],
[229851, "6484-52-2", "Ammonium nitrate (Composites)", 500, 5000, 10000, "named", "", "Ammonium Nitrate-based fertiliser composites with less than 25% Nitrogen content as a result of Ammonium Nitrate and with no more than 0.4% total combustible or organic materials (or which satisfy the detonation resistance test)."],
[229852, "6484-52-2", "Ammonium nitrate (Fertiliser grade)", 125, 1250, 5000, "named", "", "Ammonium Nitrate-based Fertiliser with more than 24,5% Nitrogen as a result of Ammonium Nitrate or Ammonium Sulphate composites with more than 16% Nitrogen as a result of Ammonium Nitrate."],
[229853, "6484-52-2", "Ammonium nitrate (Technical grade)", 35, 350, 2500, "named", "", "Ammonium Nitrate and preparations of ammonium nitrate in with more than 24,5% Nitrogen as a result of Ammonium Nitrate or aqueous ammonium nitrate solutions of which 80% or more is Ammonium Nitrate."],
[229854, "6484-52-2", "Ammonium nitrate (10/50 Off-Specs)", 1, 10, 50, "named", "", "Ammonium Nitrate \"off-specs\" material and fertilisers not satisfying the detonation resistance test or degraded and/or contaminated Ammonium Nitrate compounds."],
[234, "7778-39-4", "Arsenic (V) acid and/or salts", 0.1, 1, 2, "named", "", "", ["H301","H312","H314","H318","H331","H350","H361","H400","H410"]],
[14771, "1303-28-2", "Arsenic pentoxide", 0.1, 1, 2, "named", "", "",["H301","H331","H350","H400","H410"]],
[518605, "1327-53-3", "Arsenic trioxide", 0.01, 0.1, 0.1, "named", "", "Tetraarsenic oxide / ",["H300","H314","H350","H400", "H410"]],
[76591, "3141-12-6", "Arsenous (III) acid and/or salts", 0.01, 0.1, 0.1, "named", "", "Triethyl arsenite / Arsenous acid / triethyl ester",["H226","H301","H301","H331","H400","H410"]],
[24408, "7726-95-6", "Bromine", 2, 20, 100, "named", "", "",["H314","H330","H400"]],
[6371, "75-44-5", "Carbonyl dichloride", 0.03, 0.3, 0.75, "named", "", "Phosgene",["H314","H330"]],
[23969, "7784-42-1", "Arsenic trihydride", 0.02, 0.2, 1, "named", "", "Arsine / Hydrogen arsenide",["H220","H330","H373","H400","H410"]],
[24526, "7782-50-5", "Chlorine", 1, 10, 25, "named", "", "Chloride, Bertholite, ",["H270","H315","H319","H331","H335","H400"]],
[6354, "75-21-8", "Ethylene oxide", 0.5, 5, 50, "named", "", "",["H220","H315","H319","H331","H335","H340","H350"]],
[9033, "151-56-4", "Ethyleneimine", 1, 10, 20, "named", "", "Aziridine, Polyethyleneimine",["H225","H300","H310","H314","H330","H340","H350","H411"]],
[24524, "7782-41-4", "Fluorine", 1, 10, 20, "named", "", "",["H270","H314","H330"]],
[712, "50-00-0", "Formaldehyde", 0.5, 5, 50, "named", "", "Formalin",["H301","H311","H314","H317","H331","H341","H350"]],
[783, "1333-74-0", "Hydrogen", 0.5, 5, 50, "named", "", "",["H220"]],
[313, "7647-01-0", "Hydrogen chloride", 2.5, 25, 250, "named", "", "Hydrochloric Acid (liquefied gas)",["H314", "H331"]],
[14917, "7664-39-3", "Hydrogen fluoride", 0.5, 5, 20, "named", "", "",["H300","H310","H314","H330"]],
[21, "", "Lead alkyls", 0.5, 5, 50, "named", "", ""],
[22, "", "LPG", 5, 50, 200, "named", "", "Liquefied extremely flammable gases (including LPG) and natural gas (liquefied or otherwise)."],
[887, "67-56-1", "Methanol", 50, 500, 5000, "named", "", "Carbinol",["H225","H301","H311","H331","H370"]],
[12228, "624-83-9", "Methyl isocyanate", 0.015, 0.15, 0.15, "named", "", "Methyl carbonimide",["H225","H301","H311","H315","H317","H318","H330","H334","H335","H361"]],
[7543, '101-14-4', '4,4-Methylenebis', 0.001, 0.01, 0.01, 'named', '', '2-Chloraniline and/or salts (Powder form)',["H302","H350","H400","H410"]],
[25, "", "Nickel compounds", 0.1, 1, 1, "named", "", "Nickel compounds in inhalable powder form: Nickel monoxide, Nickel dioxide, Nickel sulphide, tri-Nickel disulphide, di-Nickel trioxide.",[]],
[977, "7782-44-7", "Oxygen", 20, 200, 2000, "named", "", "",["H270"]],
[27, "", "Petroleum products", 250, 2500, 25000, "named", "", "gasolines ; naphthas; kerosenes (including jet fuels); gas oils (including diesel fuels; home heating oils and gas oil blending streams)",[]],
[24404, "7803-51-2", "Phosphorus trihydride", 0.02, 0.2, 1, "named", "", "Phosphine",["H220","H314","H330","H400"]],
[29, "", "Polychlorodibenzofurans / polychlorodibenzodioxins (including TCDD)", 1, 0.001, 0.001, "named", "", "Please see Note 7 on the 'Help' page for more info.",[]],
[244341, "", "Potassium nitrate (granular)", 500, 5, 10, "named", "", "Potassium nitrate (5 000/10 000): composite potassium nitrate-based fertilisers composed of potassium nitrate in prilled/granular form.",[]],
[244342, "", "Potassium nitrate (crystalline)", 125, 1, 5, "named", "", "Potassium nitrate (1 250/5 000): composite potassium nitrate-based fertilisers composed of potassium nitrate in crystalline form.",[]],
[6378, "75-56-9", "Propylene oxide", 0.5, 5, 50, "named", "", "Methyloxirane",["H224","H302","H311","H319","H331","H335","H340","H350"]],
[25353, "10545-99-0", "Sulphur dichloride", 0.1, 1, 1, "named", "", "",["H314","H335","H400"]],
[1119, "7446-09-5", "Sulphur dioxide", 0.5, 5, 20, "named", "", "Sulfurous anhydride, Sulfurous oxide",["H314","H331"]],
[24682, "7446-11-9", "Sulphur trioxide", 1.5, 15, 75, "named", "", "12210-38-7",["H314","H318","H330","H335","H351","H411"]],
[21584847, "", "Toluene di-isocyanate", 1, 10, 100, "named", "", "",["H315","H317","H319","H330","H334","H351"]]
]

listedSubstances = [
  {'chemid': 201, 'tier1': 0.5, 'tier2': 5, 'tier3': 20, 'class': 'Very toxic ', 'tooltip': 'very toxic'},
  {'chemid': 202, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Toxic', 'tooltip': 'TOXIC (R23 as per Note 4)'},
  {'chemid': 203, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Oxidising', 'tooltip': 'OXIDISING'},
  {'chemid': 204, 'tier1': 500, 'tier2': 5000, 'tier3': 50000, 'class': 'Flammable', 'tooltip': 'flammable liquids - substances and preparations having a flash point of 23°C - 60°C (danger group III as per SANS 10228), supporing combustion'},
  {'chemid': 205, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Highly Flammable (a)', 'tooltip': 'substances and preparations which may become hot and finally catch fire in contact with air at ambient temperature without any input of energy. Substances and preparations which have a flashpoint lower than 60;&degC and which remain liquid under pressure, where particular processing conditions, such as high pressure or high temperature may cause major-incident hazards. Substances and preparations having a flash point lower than 23;&degC and which are not extremely flammable (danger group II SANS 10228)'},
  {'chemid': 206, 'tier1': 500, 'tier2': 5000, 'tier3': 50000, 'class': 'Highly Flammable (b)', 'tooltip': 'Flash point below 0;&degC. Boiling point at normal pressure  < 35;&degC. Flammable when in contact with air at ambient temp and pressure, which are in a gaseous or supercritical state and flammable or highly flammable substances which are maintained at a temperature above their boiling point.'},
  {'chemid': 207, 'tier1': 1, 'tier2': 10, 'tier3': 50, 'class': 'Extremely Flammable', 'tooltip': 'liquid substances and preparations which have a flash point lower than 0°C and the boiling point (or; in the case of a boiling range; th'},
  {'chemid': 208, 'tier1': 10, 'tier2': 100, 'tier3': 200, 'class': 'Hazardous (Environment) (a)', 'tooltip': 'HAZARDOUS FOR THE ENVIRONMENT risk phrases: (a) Very toxic to aquatic organisms'},
  {'chemid': 209, 'tier1': 20, 'tier2': 200, 'tier3': 500, 'class': 'Hazardous (Environment) (b)', 'tooltip': 'HAZARDOUS FOR THE ENVIRONMENT risk phrases: (b) Toxic to aquatic organisms: may cause long term adverse effects in the aquatic environme'},
  {'chemid': 210, 'tier1': 10, 'tier2': 100, 'tier3': 200, 'class': 'Violent Reaction', 'tooltip': 'ANY CLASSIFICATION not covered by those given above in combination with risk phrases: (a) Reacts violently with water'},
  {'chemid': 211, 'tier1': 5, 'tier2': 50, 'tier3': 200, 'class': 'Gas Release', 'tooltip': 'ANY CLASSIFICATION not covered by those given above in combination with risk phrases: (b) In contact with water; liberates toxic gas'}
  ]

#pure list of chemicals
chemlist = []
MainDB = []

for chem in bigDatabase:
  MainDB.append({"id": chem[0], "CAS": chem[1], "name": chem[2], "tier1": chem[3], "tier2": chem[4], "tier3": chem[5], "type": chem[6], "class": chem[7], "tooltip": chem[8], "hphrases": chem[9]})

for chem in MainDB:
  chemlist.append({"id": chem["id"], "CAS": chem["CAS"], "name": chem["name"], "type": chem["type"], "class": chem["class"], "tooltip": chem["tooltip"]})
print("chemlist loaded!")

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
  inv["indtier"] = indtier
  return inv

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