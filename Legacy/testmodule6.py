from newNamedSubs import newNamedSubs, newNamedSubsSupplementaryinfo

for listoneitem in newNamedSubs:
  for listtwwoitem in newNamedSubsSupplementaryinfo:
    if listoneitem["name"] == listtwwoitem["name"]:
      listoneitem["hazardPhrases"] = listtwwoitem["hazardPhrases"]
      listoneitem["chemid"] = listtwwoitem["chemid"]

f=open("finallist.txt","w+")
for sub in newNamedSubs:
  f.write(str(sub))
f.close()