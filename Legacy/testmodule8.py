from finallist import namedSubstancesModule
from finallist import newinfo

for originalsub in finallist:
  if "chemid" in originalsub.keys():
    for sub in newinfo:
      if sub["cid"] == originalsub["chemid"] and sub["name"] ==     originalsub["name"]:
        originalsub["CAS"] = sub["CAS"]

f=open("finallist3.txt","w+")
for final in finallist:
  f.write(str(final))
f.close()