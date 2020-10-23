from flask import Flask, jsonify, request, flash, redirect, render_template, url_for, send_from_directory, session, g, abort
import json
import hyginus
import requests

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
    for chem in inv:
      if newEntry["id"] == str(chem["id"]):
        if int(newEntry["qty"]) > 0:
          chem["qty"] = newEntry["qty"]
        elif int(newEntry["qty"]) == 0:
          inv.remove(chem)
        return "updated"
    #listed substance
    if newEntry["type"] == "named":
      for chem in hyginus.chemlist:
        if newEntry["id"] == str(chem["id"]):
          result = chem
          result["qty"] = newEntry["qty"]
          result["indexpos"] = len(inv)+1
    #listed substance
    else:
      result = newEntry
      result["indexpos"] = len(inv)+1

    print("result", result)
    inv.append(result)
    print("inv", inv)
    return render_template("list_item_template.html", item=result)
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

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/clearinv', methods=["Post"])
def clearinv():
  inv.clear()
  return "Cleared"

def updatehphrases(entry):
  try:
    if entry["CAS"] and len(entry["CAS"]) > 1:
      cas = entry["CAS"]
      query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/xref/rn/{cas}/json"
    else:
      substance = entry["name"]
      query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{substance}/json"
    print("Q: ", query)
    response = requests.get(query)
    print("response1: ", response)
    queryAnswer = json.loads(response.content)
    print("answer1: ", queryAnswer)
    cid = hyginus.stringsearch(json.dumps(queryAnswer), "cid")
    query2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON?heading=GHS classification"
    print("query2: ", query2)
    response2 = requests.get(query2)
    print("response2: ", response2)
    queryAnswer2 = json.loads(response2.content)
    print("response2content: ", queryAnswer2)
    hazardphrases = hyginus.stringsearch(json.dumps(queryAnswer2), "H")
    print("hazardphrases: ", hazardphrases)
    for item in inv:
      if entry["id"] == item["id"]:
        item["hphrases"] = hazardphrases
  except Exception as e:
    print(e)
    return f"An Error Occured: {e}"