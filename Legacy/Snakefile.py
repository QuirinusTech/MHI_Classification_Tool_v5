from listedSubstancesModule import listedSubstances

rules = {
  "A": "",
  "B": "",
  "C": ""
}

listA = []
listB = []
listC = []

for sub in listedSubstances:
  chemid = str(sub["chemid"])
  if chemid[0] == "1":
    listA.append(sub["chemid"])
  if chemid[0] == "2":
    listB.append(sub["chemid"])
  if chemid[0] == "3":
    listC.append(sub["chemid"])
rules["A"] = listA
rules["B"] = listB
rules["C"] = listC

print(rules)