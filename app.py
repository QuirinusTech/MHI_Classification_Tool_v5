from flask import Flask, flash, jsonify, request, flash, redirect, render_template, url_for, send_from_directory, session, g, abort
import json
import hyginus
from finallist import namedSubstances
import requests
from hphrases import ClassFinder
from random import randint

app = Flask(__name__)

inv = []

@app.route('/')
def welcome():
  return render_template("welcome.html")

@app.route('/inventory')
def inventory():
  return render_template("inventory.html", inventory=inv, chemlist=finallist.namedSubstances, listedSubstances=hphrases.listedsubstances)

"""@app.route('/list')
def listey():
  return render_template("list.html", inventory=inv)"""

@app.route('/addtoinv', methods=["Post"])
def addtoinv():
  try:
    newEntry = json.loads(request.form['newEntry'])
    print("newEntry", newEntry)
    
    #named substance
    if newEntry["chemtype"] == "named":
      for chem in finallist.namedSubstances:
        if int(newEntry["chemid"]) == int(chem["chemid"]):
          result = chem
          print("found named substance in database: ")
          print(chem)

          result["class"] = ClassFinder(chem["hazardPhrases"], "desc")
          result["id"] = newEntry["id"]
          result["qty"] = newEntry["qty"]
          result["indexpos"] = len(inv)+1
          break
    #listed substance
    else:
      result = newEntry
      if newEntry["name"] == newEntry["chemid"]:
        for listedSubstance in hphrases.listedsubstances:
          if int(result["chemid"]) == int(listedSubstance["chemid"]):
            result["class"] = listedSubstance["class"]
            result["name"] = listedSubstance["class"] + " substance"
      else:
        if len(result["hazardPhrases"]) > 0 and result["hazardPhrases"] != "" and result["hazardPhrases"] != []:
          if isinstance(result["hazardPhrases"],list):
            hPhraseArray = newEntry["hazardPhrases"]
          else:
            hphrasestr = json.dumps(newEntry["hazardPhrases"])
            hPhraseArray = hyginus.stringsearch(hphrasestr,"H")
            result["hazardPhrases"] = hPhraseArray
          result["class"] = ClassFinder(hPhraseArray,"desc")
          result["chemid"] = ClassFinder(hPhraseArray,"chemid")
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
        if float(update["qty"]) > 0:
          chem["qty"] = update["qty"]
          return "updated"
        elif float(update["qty"]) == 0:
          inv.remove(chem)
          return "deleted"
  except Exception as e:
    print(e)
    return f"An Error Occured: {e}"

@app.route('/results')
def results():
  if len(inv) > 0:
    results = hyginus.assessment(inv)
    recommendation = results.finalTier
    results.indTier = convertNumberToWord(results.indTier)
    results.finalTier = convertNumberToWord(results.finalTier)
    results.aggregateTier = convertNumberToWord(results.aggregateTier)
    return render_template('results.html', results = results, inv = hyginus.convertNumberToWord(inv), recommendation=recommendation)
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
  searchtype = entry["searchtype"]
  for chem in finallist.namedSubstances:
    if entry["field"] == chem[searchtype]:
      classvar = ClassFinder([chem["hazardPhrases"]],"chemid")
      findings = {"found": True, "foundresult": "named", "chemclass": classvar, "retry": False, "recordTitle": chem["name"], "CAS": chem["CAS"], "hphrases": chem["hazardPhrases"], "UN": chem["UN"], "chemtype": "named"}
      print('Substance found in database under "named substances": ', findings)
      return json.dumps(findings)

  # no results from checking existing database
  print("Substance not in named substances database. Continue external calls.")

  #CALL 1

  # search by CAS
  if entry["searchtype"] == "CAS":
    print('Searching by CAS')
    cas = entry["field"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/xref/rn/{cas}/json"

  #search by UN number
  elif entry["searchtype"] == "UN":
    print('Searching by UN Number')
    un = entry["field"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/UN%20{substance}/json"

  # search by substance name
  else:
    print('Invalid CAS. Searching by substance name')
    substance = entry["field"]
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"


  response = requests.get(query)
  queryAnswer = json.loads(response.content)
  print("Response 1 received")
  print(queryAnswer)
  check1 = hyginus.stringsearch(json.dumps(queryAnswer),"fault")
  #parse the response
  if check1 == "NotFound":
    if entry["field"] is None or entry["field"] == "":
      result = {"found" : False}
      return json.dumps(result)
    else:
      #call 1b
      print('No results found with CAS. Searching by substance name')
      substance = entry["field"]
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
 
  if check2 == "OK":
    hazardPhrases = hyginus.stringsearch(json.dumps(queryAnswer2), "H")
    recordTitle = hyginus.stringsearch(json.dumps(queryAnswer2), "RT")
    if recordTitle != "None" and hazardPhrases != [] and cid != 'NotFound':
      findings = {"found": True, "foundresult": "final", "recordTitle": recordTitle, "hphrases": hazardPhrases, "chemid": cid, "chemtype": "listed"}
      print(findings)
      return jsonify(findings)
    else:
      print("data corruption or bad search")
      results = {"found" : False, "foundresult": "final", "retry": False}
      return jsonify(results)
  elif check2 == "NotFound":
    print("Check2 failed")
    results = {"found" : False, "foundresult": "final", "retry": False}
    return jsonify(results)

@app.route("/testinventory")
def testinventory():
  while len(inv) < 5:
    namedSubstancesLength = len(finallist.namedSubstances) - 1
    randomnumber = randint(0,namedSubstancesLength)
    newrandomchemid = finallist.namedSubstances[randomnumber]["chemid"]
    for chem in finallist.namedSubstances:
      if newrandomchemid == chem["chemid"] and chem["hazardPhrases"] != []:
        result = chem
        print(result)
        result["class"] = ClassFinder(chem["hazardPhrases"], "desc")
        result["id"] = "test_id_" + str(randint(0,10000))
        maxqty = chem["tier3"] * 1.5
        result["qty"] = randint(0,maxqty)
        result["indexpos"] = len(inv)+1
        inv.append(result)
  return render_template("inventory.html", inventory=inv, chemlist=finallist.namedSubstances, listedSubstances=hphrases.listedsubstances)