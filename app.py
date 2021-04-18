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
      if len(result["hphrases"]) > 0 and result["hphrases"] != "" and result["hphrases"] != []:
        if isinstance(result["hphrases"],list):
          hphrasesarr = newEntry["hphrases"]
        else:
          hphrasestr = json.dumps(newEntry["hphrases"])
          hphrasesarr = hyginus.stringsearch(hphrasestr,"H")
          result["hphrases"] = hphrasesarr
        result["class"] = ClassFinder(hphrasesarr,"desc")
        result["chemid"] = ClassFinder(hphrasesarr,"chemid")
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
    if entry["CAS"] != "" and entry["CAS"] == chem["CAS"]:
        findings = {"found": True, "foundresult": "named", "retry": False, "recordTitle": chem["name"], "hphrases": chem["hphrases"]}
        print('Substance found in database under "named substances": ', findings)
        return json.dumps(findings) 
    elif entry["name"] == chem["name"] and entry["name"] != "":
        findings = {"found": True, "foundresult": "named", "retry": False, "recordTitle": chem["name"], "hphrases": chem["hphrases"]}
        print('Substance found in database under "named substances": ', findings)
        return json.dumps(findings)

  # no results from checking existing database
  print("Substance not in named substances database. Continue external calls.")

  #CALL 1

  # search by CAS
  if entry["searchtype"] == "CAS":
    print('Searching by CAS')
    cas = entry["CAS"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/xref/rn/{cas}/json"

  # search by substance name
  else:
    print('Invalid CAS. Searching by substance name')
    substance = entry["name"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"

  response = requests.get(query)
  queryAnswer = json.loads(response.content)
  print("Response 1 received")
  print(queryAnswer)
  check1 = hyginus.stringsearch(json.dumps(queryAnswer),"fault")
  #parse the response
  if check1 == "NotFound":
    if entry["name"] is None or entry["name"] == "":
      result = {"found" : False}
      return json.dumps(result)
    else:
      #call 1b
      print('No results found with CAS. Searching by substance name')
      substance = entry["name"]
      query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"
      response = requests.get(query)
      queryAnswer = json.loads(response.content)
      print("Response 1b received")
      print(queryAnswer)
      check1b = hyginus.stringsearch(json.dumps(queryAnswer),"fault")
      if check1b == "NotFound":
        result = {"found" : False}
        return json.dumps(result)
      elif check1b == "OK":
        cid = hyginus.stringsearch(json.dumps(queryAnswer), "cid")
        print("CID found: ", cid)
  
  elif check1 == "OK":
    cid = hyginus.stringsearch(json.dumps(queryAnswer), "cid")
    print("CID found: ", cid)

  #call 2
  query2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=GHS classification"
  print("query2: ", query2)
  response2 = requests.get(query2)
  queryAnswer2 = json.loads(response2.content)
  print("response2 received")
  check2 = hyginus.stringsearch(json.dumps(queryAnswer2),"fault")
  if check2 == "NotFound":
    print("Check2 failed")
    result = {"found" : False, "foundresult": "final", "retry": False}
    return json.dumps(results)
  elif check2 == "OK":
    hazardPhrases = hyginus.stringsearch(json.dumps(queryAnswer2), "H")
    recordTitle = hyginus.stringsearch(json.dumps(queryAnswer2), "RT")
    findings = {"found": True, "foundresult": "final", "recordTitle": recordTitle, "hphrases": hazardPhrases}
    print(findings)
    return json.dumps(findings)