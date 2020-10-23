from flask import Flask, jsonify, request, flash, redirect, render_template, url_for, send_from_directory, session, g, abort
import json
import hyginus

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
    print(newEntry)
    for chem in inv:
      if newEntry["id"] == str(chem["id"]):
        if int(newEntry["qty"]) > 0:
          chem["qty"] = newEntry["qty"]
        elif int(newEntry["qty"]) == 0:
          inv.remove(chem)
        return "updated"
    if newEntry["type"] == "named":
      for chem in hyginus.chemlist:
        if newEntry["id"] == str(chem["id"]):
          result = chem
          result["qty"] = newEntry["qty"]
          result["indexpos"] = len(inv)+1
          inv.append(result)
    else:
      newEntry["indexpos"] = len(inv)+1
      inv.append(newEntry)
    print(inv)
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