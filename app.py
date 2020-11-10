from flask import Flask, flash, jsonify, request, flash, redirect, render_template, url_for, send_from_directory, session, g, abort
import json
import hyginus
import requests
from hphrases import ClassFinder

app = Flask(__name__)

inv = []

@app.route('/')
def welcome():
  return render_template("welcome.html")

@app.route('/inventory')
def inventory():
  return render_template("inventory.html", inventory=inv, chemlist=hyginus.chemlist, listedSubstances=hyginus.listedSubstances)

"""@app.route('/list')
def listey():
  return render_template("list.html", inventory=inv)"""

@app.route('/addtoinv', methods=["Post"])
def addtoinv():
  try:
    newEntry = json.loads(request.form['newEntry'])
    print("newEntry", newEntry)
    #named substance
    if newEntry["type"] == "named":
      for chem in hyginus.chemlist:
        if newEntry["chemid"] == str(chem["chemid"]):
          result = chem
          result["class"] = ClassFinder(chem["hphrases"], "desc")
          result["id"] = newEntry["id"]
          result["qty"] = newEntry["qty"]
          result["indexpos"] = len(inv)+1
          break
    #listed substance
    else:
      result = newEntry
      if len(result["hphrases"]) > 0:
        hphrasesarr = hyginus.stringsearch(newEntry["hphrases"],"H")
        result["class"] = ClassFinder(hphrasesarr,"desc")
        result["chemid"] = ClassFinder(hphrasesarr,"chemid")
        result["hphrases"] = hphrasesarr
      else:
        for listedsub in hyginus.listedSubstances:
          if result["chemid"] == listedsub["chemid"]:
            result["class"] = listedsub["class"]
      result["indexpos"] = len(inv)+1
    print("result", result)
    inv.append(result)
    print("inv", inv)
    return render_template("list_item_template.html", item=result)
  except Exception as e:
    print(e)
    return f"An Error Occured: {e}"

@app.route("/update", methods=["POST"])
def update():
  try:
    update = json.loads(request.form['update'])
    print("update", update)
    for chem in inv:
      if update["id"] == str(chem["id"]):
        if int(update["qty"]) > 0:
          chem["qty"] = update["qty"]
          return "updated"
        elif int(update["qty"]) == 0:
          inv.remove(chem)
          return "deleted"
  except Exception as e:
    print(e)
    return f"An Error Occured: {e}"

@app.route('/results')
def results():
  if len(inv) > 0:
    results = hyginus.assessment(inv)
    return render_template('results.html', results=results, inv=inv)
  else:
    return redirect(url_for("inventory"))

@app.route('/help')
def help():
  return render_template("help.html")

@app.route('/faq')
def faq():
  return render_template("faq.html")


@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/clearinv', methods=["Post"])
def clearinv():
  inv.clear()
  return "Cleared"

@app.route("/updatehphrases", methods=["Post"])
def updatehphrases():
  entry = json.loads(request.form['substance'])
  print(entry)
  # check if substance not named substances database
  for chem in hyginus.MainDB:
    if entry["CAS"] == chem["CAS"] or entry["name"] == chem["name"]:
      findings = {"found": True, "foundresult": "named", "retry": False, "recordTitle": chem["name"], "hazardPhrases": chem["hphrases"]}
      print('Substance found in database under "named substances": ', findings)
      return json.dumps(findings) 

  # no results from checking existing database
  print("Substance not in named substances database. Continue external calls.")

  # search by CAS
  if entry["searchtype"] == "CAS" and hyginus.checkCAS(entry["CAS"]) == True:
    print('searching by CAS')
    cas = entry["CAS"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/xref/rn/{cas}/json"
    retry = True
  # search by substance name
  else:
    print('searching by substance name')
    substance = entry["name"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"
    retry = False

  if entry["searchtype"] == "name" or entry["searchtype"] == "CAS":
    response = requests.get(query)
    queryAnswer = json.loads(response.content)
    print(queryAnswer)
    check1 = hyginus.stringsearch(json.dumps(queryAnswer),"fault")
    #parse the response
    if check1 == "NotFound":
      result = {"found": False, "retry": retry}
      return json.dumps(results)

    elif check1 == "OK":
      cid = hyginus.stringsearch(json.dumps(queryAnswer), "cid")
      result = {"found": True, "foundresult": "cid", "cid": cid, "retry": retry}
      return json.dumps(result)


  if entry["searchtype"] == "cid":
    cid = entry["cid"]
    query2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=GHS classification"
    print("query2: ", query2)
    response2 = requests.get(query2)
    print("response2: ", response2)
    queryAnswer2 = json.loads(response2.content)
    print("response2content: ", queryAnswer2)
    check2 = hyginus.stringsearch(json.dumps(queryAnswer2),"fault")
    if check2 == "NotFound":
      print("Check2 failed")
      result = {"found": False, "retry": False}
      return json.dumps(results)
    elif check2 == "OK":
      hazardPhrases = hyginus.stringsearch(json.dumps(queryAnswer2), "H")
      recordTitle = hyginus.stringsearch(json.dumps(queryAnswer2), "RT")
      findings = {"found": True, "foundresult": "final", "recordTitle": recordTitle, "hazardPhrases": hazardPhrases}
      print(findings)
      return json.dumps(findings)