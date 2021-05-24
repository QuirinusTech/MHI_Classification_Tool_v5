def convertNumberToWord(arg):
  """
    Converts all tier numbers to words
    arg can be string, list, dict or list of dict
  """

  NumberToWord = {
    3: "High",
    2: "Medium",
    1: "Low",
    0: "None"
  }

  if type(arg) is dict:
    for keyname in arg.keys():
      if type(arg[keyname]) is int and arg[keyname] <= 3 and arg[keyname]>=0:
        arg[keyname] = NumberToWord[arg[keyname]]
  if type(arg) is list and type(arg[0]) is dict:
    for chem in arg:
      chem["tier"] = str(NumberToWord[int(chem["tier"])])
  if type(arg) is list and type(arg[0]) is not dict:
    for chem in arg:
      if type(chem) is not int:
        integer = int(chem)
      else:
        integer = chem
      string = NumberToWord[integer]
      chem = string
  elif type(arg) is str or type(arg) is int:
    arg = str(NumberToWord[int(arg)])

  return arg



var1= {
    'name': 'Potassium nitrate (as described in Note 8) ',
    'UN': '1488',
    'tier1': 1,
    'tier2': 2,
    'tier3': 3,
    'CAS': '7757-79-1',
    'chemid': 0,
    'hazardPhrases': ['H272', 'H315', 'H319', 'H335', 'H361', 'H370', 'H372', 'H303', 'H371', 'H373']
}
convertNumberToWord(var1)
print(convertNumberToWord(var1))

#output: {'name': 'Potassium nitrate (as described in Note 8) ', 'UN': '1488', 'tier1': 'Low', 'tier2': 'Medium', 'tier3': 'High', 'CAS': '7757-79-1', 'chemid': 'None', 'hazardPhrases': ['H272', 'H315', 'H319', 'H335', 'H361', 'H370', 'H372', 'H303', 'H371', 'H373']}