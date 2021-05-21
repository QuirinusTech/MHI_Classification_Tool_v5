hphrases = {
    "H200":	"Unstable explosive",
    "H201": "Explosive; mass explosion hazard",
    "H202": "Explosive; severe projection hazard",
    "H203": "Explosive; fire, blast or projection hazard",
    "H204": "Fire or projection hazard",
    "H205": "May mass explode in fire",
    "H206": "Fire, blast or projection hazard: increased risk of explosion if desensitizing agent is reduced",
    "H207": "Fire or projection hazard: increased risk of explosion if desensitizing agent is reduced",
    "H208": "Fire hazard: increased risk of explosion if desensitizing agent is reduced",
    "H220": "Extremely flammable gas",
    "H221": "Flammable gas",
    "H222": "Extremely flammable aerosol",
    "H223": "Flammable aerosol",
    "H224": "Extremely flammable liquid and vapour",
    "H225": "Highly flammable liquid and vapour",
    "H226": "Flammable liquid and vapour",
    "H227": "Combustible liquid",
    "H228": "Flammable solid",
    "H229": "Pressurized container: may burst if heated",
    "H230": "May react explosively even in the absence of air",
    "H231": "May react explosively even in the absence of air at elevated pressure and/or temperature",
    "H232": "May ignite spontaneously if exposed to air",
    "H240": "Heating may cause an explosion",
    "H241": "Heating may cause a fire or explosion",
    "H242": "Heating may cause a fire",
    "H250": "Catches fire spontaneously if exposed to air",
    "H251": "Self-heating; may catch fire",
    "H252": "Self-heating in large quantities; may catch fire",
    "H260": "In contact with water releases flammable gases which may ignite spontaneously",
    "H261": "In contact with water releases flammable gas",
    "H270": "May cause or intensify fire; oxidizer",
    "H271": "May cause fire or explosion; strong oxidizer",
    "H272": "May intensify fire; oxidizer",
    "H280": "Contains gas under pressure; may explode if heated",
    "H281": "Contains refrigerated gas; may cause cryogenic burns or injury",
    "H290": "May be corrosive to metals",
    "H300": "Fatal if swallowed.",
    "H301": "Toxic if swallowed",
    "H302": "Harmful if swallowed",
    "H303": "May be harmful if swallowed",
    "H304": "May be fatal if swallowed and enters airways",
    "H305": "May be harmful if swallowed and enters airways",
    "H310": "Fatal in contact with skin",
    "H311": "Toxic in contact with skin",
    "H312": "Harmful in contact with skin",
    "H313": "May be harmful in contact with skin",
    "H314": "Causes severe skin burns and eye damage",
    "H315": "Causes skin irritation",
    "H316": "Causes mild skin irritation",
    "H317": "May cause an allergic skin reaction",
    "H318": "Causes serious eye damage",
    "H319": "Causes serious eye irritation",
    "H320": "Causes eye irritation",
    "H330": "Fatal if inhaled",
    "H331": "Toxic if inhaled",
    "H332": "Harmful if inhaled",
    "H333": "May be harmful if inhaled",
    "H334": "May cause allergy or asthma symptoms or breathing difficulties if inhaled",
    "H335": "May cause respiratory irritation",
    "H336": "May cause drowsiness or dizziness",
    "H340": "May cause genetic defects",
    "H341": "Suspected of causing genetic defects",
    "H350": "May cause cancer",
    "H351": "Suspected of causing cancer",
    "H360": "May damage fertility or the unborn child",
    "H361": "Suspected of damaging fertility or the unborn child",
    "H361d": "Suspected of damaging the unborn child",
    "H360D": "May damage the unborn child",
    "H361f": "Suspected of damaging fertility",
    "H360F": "May damage fertility",
    "H362": "May cause harm to breast-fed children",
    "H370": "Causes damage to organs",
    "H371": "May cause damage to organs",
    "H372": "Causes damage to organs through prolonged or repeated exposure",
    "H373": "May cause damage to organs through prolonged or repeated exposure",
    "H300+H310": "Fatal if swallowed or in contact with skin",
    "H300+H330": "Fatal if swallowed or if inhaled",
    "H310+H330": "Fatal in contact with skin or if inhaled",
    "H300+H310+H330": "Fatal if swallowed, in contact with skin or if inhaled",
    "H301+H311": "Toxic if swallowed or in contact with skin",
    "H301+H331": "Toxic if swallowed or if inhaled",
    "H311+H331": "Toxic in contact with skin or if inhaled",
    "H301+H311+H331": "Toxic if swallowed, in contact with skin or if inhaled",
    "H302+H312": "Harmful if swallowed or in contact with skin",
    "H302+H332": "Harmful if swallowed or if inhaled",
    "H312+H332": "Harmful in contact with skin or if inhaled",
    "H302+H312+H332": "Harmful if swallowed, in contact with skin or if inhaled",
    "H303+H313": "May be harmful if swallowed or in contact with skin",
    "H303+H333": "May be harmful if swallowed or if inhaled",
    "H313+H333": "May be harmful in contact with skin or if inhaled",
    "H303+H313+H333": "May be harmful if swallowed, in contact with skin or if inhaled",
    "H315+H320": "Causes skin and eye irritation",
    "H400": "Very toxic to aquatic life",
    "H401": "Toxic to aquatic life",
    "H402": "Harmful to aquatic life",
    "H410": "Very toxic to aquatic life with long-lasting effects",
    "H411": "Toxic to aquatic life with long-lasting effects",
    "H412": "Harmful to aquatic life with long-lasting effects",
    "H413": "May cause long-lasting harmful effects to aquatic life",
    "H420": "Harms public health and the environment by destroying ozone in the upper atmosphere",
    "H433": "Harmful to terrestrial vertebrates"
}


hgroups_old = [
    {
        "chemid": 201,
        "desc": "Very toxic",
        "hphrases": ["H310", "H311", "H312", "H313", "314"]
    },
    {
        "chemid": 202,
        "desc": "Toxic",
        "hphrases": ["H300", "H301", "H302", "H303", "H304", "H305", "H331"]
    },
    {
        "chemid": 203,
        "desc": "Oxidising",
        "hphrases": ["H270", "H271", "H272"]
    },
    {
        "chemid": 204,
        "desc": "Flammable",
        "hphrases": ["H221", "H222", "H223", "H224", "H225", "H226", "H227", "H228", "H242", "H281"]
    },
    {
        "chemid": 205,
        "desc": "Highly Flammable (a)",
        "hphrases": ["H204", "H206", "H229", "H240", "H241", "H251", "H252", "H261", "H280"]
    },
    {
        "chemid": 206,
        "desc": "Highly Flammable (b)",
        "hphrases": ["H205", "H207", "H208", "H220", "H230", "H231", "H250", "H260"]
    },
    {
        "chemid": 207,
        "desc": "Extremely Flammable",
        "hphrases": ["H200", "H201", "H202", "H203", "H232"]
    },
    {
        "chemid": 208,
        "desc": "Hazardous (Environment) (a)",
        "hphrases": ["H330", "H370"]
    },
    {
        "chemid": 209,
        "desc": "Hazardous (Environment) (b)",
        "hphrases": ["H340", "H350", "H400", "H401", "H402", "H420", "H433"]
    },
    {
        "chemid": 210,
        "desc": "Violent Reaction",
        "hphrases": ["H290", "H318", "H410", "H411", "H412", "H413"]
    },
    {
        "chemid": 211,
        "desc": "Gas Release",
        "hphrases": []
    },
]

listedsubstances = [
    {
        "chemid": 101,
        "tier1": 5,
        "tier2": 5,
        "tier3": 20,
        "desc": "H1 Acute Toxic Category 1",
        "hphrases": ["H300", "H310", "H330"],
        "tooltip": "All exposure routes"
    },
    {
        "chemid": 102,
        "tier1": 15,
        "tier2": 50,
        "tier3": 200,
        "desc": "H2 Acute Toxic (Inhalation)",
        "hphrases": ["H331", "H301"],
        "tooltip": "Category 2, all exposure routes. \n Category 3, inhalation exposure route."
    },
    {
        "chemid": 103,
        "tier1": 15,
        "tier2": 50,
        "tier3": 200,
        "desc": "H3 STOT",
        "hphrases": ["H370"],
        "tooltip": "Specific Target Organ Toxicity. Category 1, Single Exposure SE STOT"
    },
    {
        "chemid": 201,
        "tier1": 2.5,
        "tier2": 10,
        "tier3": 50,
        "desc": "P2 Flammable Gases",
        "hphrases": ["H220", "H221"],
        "tooltip": "Flammable gases, Category 1 or 2"
    },
    {
        "chemid": 202,
        "tier1": 50,
        "tier2": 150,
        "tier3": 500,
        "desc": "P3a Flammable Aerosols",
        "hphrases": ["H222", "H223"],
        "tooltip": "Flammable aerosols Category 1 or 2, containing flammable gases Category 1 or 2 or flammable liquids Category 1"
    },
    {
        "chemid": 203,
        "tier1": 1250,
        "tier2": 5000,
        "tier3": 50000,
        "desc": "P3b Flammable Aerosols",
        "hphrases": [],
        "tooltip": "Flammable’ aerosols Category 1 or 2, not containing flammable gases Category 1 or 2 nor flammable liquids category 1"
    },
    {
        "chemid": 204,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P4 Oxidising Gases",
        "hphrases": ["H270"],
        "tooltip": "Oxidising gases, Category 1"
    },
    {
        "chemid": 205,
        "tier1": 5,
        "tier2": 10,
        "tier3": 50,
        "desc": "P5a Flammable Liquids",
        "hphrases": ["H224"],
        "tooltip": ""
    },
    {
        "chemid": 206,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P5b Flammable Liquids",
        "hphrases": [],
        "tooltip": ""
    },
    {
        "chemid": 216,
        "tier1": 1250,
        "tier2": 5000,
        "tier3": 50000,
        "desc": "P5c Flammable Liquids",
        "hphrases": ["H225", "H226"],
        "tooltip": "Flammable Liquids, Categories 2 or 3 not covered by P5a and P5b"
    },
    {
        "chemid": 207,
        "tier1": 5,
        "tier2": 10,
        "tier3": 50,
        "desc": "P6a Self-Reactive Substances and Mixtures and Organic Peroxides",
        "hphrases": ["H240", "H241"],
        "tooltip": "Self-reactive substances and mixtures, Type A or B or organic peroxides, Type A or B"
    },
    {
        "chemid": 208,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P6b Self -Reactive Substances and Mixtures and Organic Peroxides",
        "hphrases": ["H242"],
        "tooltip": "Self-reactive substances and mixtures, Type C, D, E or F or organic peroxides, Type C, D, E, or F"
    },
    {
        "chemid": 209,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P7 Pyrophoric Liquids and Solids",
        "hphrases": ["H250"],
        "tooltip": "Pyrophoric Liquids and Solids, Category 1"
    },
    {
        "chemid": 210,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "P8 Oxidising Liquids and Solids",
        "hphrases": ["H271", "H272", "H273"],
        "tooltip": "Oxidising Liquids, Category 1, 2 or 3, or Oxidising Solids, Category 1, 2 or 3"
    },
    {
        "chemid": 301,
        "tier1": 40,
        "tier2": 100,
        "tier3": 500,
        "desc": "O1 Violent aqueous reaction.",
        "hphrases": [],
        "tooltip": "Substances or mixtures that reacts violently with water"
    },
    {
        "chemid": 302,
        "tier1": 40,
        "tier2": 100,
        "tier3": 500,
        "desc": "O2 flammable gas emission on aqueous contact",
        "hphrases": ["H260"],
        "tooltip": "Substances and mixtures which in contact with water emit flammable gases"
    },
    {
        "chemid": 303,
        "tier1": 20,
        "tier2": 50,
        "tier3": 200,
        "desc": "O3 Toxic gas emission on aqueous contact",
        "hphrases": [],
        "tooltip": "Substances or mixtures that liberates toxic gas when in contact with water."
    }
]



rules = {
  "A": [201, 202],
  "B": [203, 204, 205, 206, 207],
  "C": [208, 209]
}

aggregaterule = {}
for group in hgroups:
  aggregaterule[group['chemid']] = 0

def ClassFinder(hphraselist, field):
  
  """
    using an array of hphrases, finds the first match from the array in the hphrases group where the hphrase is found.
    return value is determined by the field argument, which can be either 'desc' (description) or 'chemid' (an id used to find other info on this substance in the database)
  """
  possiblegroups = []
  for hphrase in hphraselist:
    for group in hgroups:
      if hphrase in group["hazardPhrases"]:
        possiblegroups.append(group[field])

  if field == "chemid":
    #precedence rules
    if 201 in possiblegroups:
      return 201
    elif 202 in possiblegroups:
      return 202
    elif 207 in possiblegroups:
      return 207
    elif 206 in possiblegroups:
      return 206
    elif 205 in possiblegroups:
      return 205
    elif 204 in possiblegroups:
      return 204
    else:
      return possiblegroups[0]

  elif field == "desc":
    #precedence rules
    if "Very toxic" in possiblegroups:
      return "Very toxic"
    elif "Toxic" in possiblegroups:
      return "Toxic"
    elif "Extremely Flammable" in possiblegroups:
      return "Extremely Flammable"
    elif "Highly Flammable (b)" in possiblegroups:
      return "Highly Flammable (b)"
    elif "Highly Flammable (a)" in possiblegroups:
      return "Highly Flammable (a)"
    elif "Flammable" in possiblegroups:
      return "Flammable"
    else:
      return possiblegroups[0]

def RuleFinder(item):
  """
    takes an item as an argument and returns the rule group in which a substance falls (a / b / c).
    item must have the following fields: type, chemid, hphrases
  """

  if item['chemtype'] == "named":
    for hphrase in item["hazardPhrases"]:
      for group in hgroups:
        if hphrase in group["hazardPhrases"]:
          for rule in rules.keys():
            if group["chemid"] in rules[rule]:
              return rule
  elif item['chemtype'] == "listed":
    for rule in rules.keys():
      if int(item["chemid"]) in rules[rule]:
        return rule
  else:
    return 0
