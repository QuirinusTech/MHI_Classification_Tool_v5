from flask import Flask, jsonify, request, redirect, render_template, url_for, flash, session
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf import FlaskForm
import json
import hyginus
from namedSubstancesModule import namedSubstances
import requests
from listedSubstancesModule import MasterCategoryController, listedSubstances, flammableLiquidWarning
from random import randint
from users import dbUsers
from mercury import ReportError
from werkzeug.exceptions import HTTPException
import traceback

app = Flask(__name__)
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

app.secret_key = '6F74T2O4Z9YTCN1U5ASA78EO2ER56BE'

login = LoginManager(app)
login.login_view = 'login'

inventories = []

def GetInv():
  invexists = False
  for inventory in inventories:
    if inventory['invId'] == session['_id']:
      return inventory['inv']
  if invexists == False:
    inventories.append({'invId': session['_id'], "inv": []})
  for inventory in inventories:
    if inventory['invId'] == session['_id']:
      return inventory['inv']

class User(UserMixin):
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return self.uid

all_users = []
currentuserlistname = []

for x in dbUsers:
    user = User()
    user.email = x['email']
    user.set_password(x['password'])
    user.uid = x['id']
    user.name = x['name']
    user.uname = x['username']
    currentuserlistname.append(x['username'])
    all_users.append(user)

@login.user_loader
def load_user(arg1):
    for user in all_users:
        if user.uid == arg1:
            return user

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errorPage.html', e=e, errorType="general"), 404

@app.errorhandler(HTTPException)
def httpException(e):
  response = e.get_response()
  response = str(response) + str(traceback.print_exc())
  return render_template('errorPage.html', e=response, errorType="general"), 500

def errorPage(e,errorType="general"):
  ReportError(str(e))
  print("Error: " + str(e))
  return render_template('errorPage.html', e=e, errorType=errorType)

@app.route('/error')
def testerrorPage(e="Testing", errorType="assessfail"):
  print("Error: " + str(e))
  return render_template('errorPage.html', e=e, errorType=errorType)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('start'))
    user = ""
    form = LoginForm()
    if form.validate_on_submit():
        for x in all_users:
            if x.uname == form.username.data:
                user = x
        if user is None or not user or not user.check_password(form.password.data):
            errormessage = 'Invalid username or password'
            flash(errormessage)
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('welcome')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You've been successfully logged out.")
    return redirect(url_for('terminal'))

@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

@app.route('/')
def welcome():
  print(session)
  return render_template("welcome.html")

@app.route('/inventory')
@login_required
def inventory():
  print('before')
  print(inventories)
  inv = GetInv()
  print('after')
  print(inventories)
  return render_template("inventory.html", flammableLiquidWarning=flammableLiquidWarning, inventory=inv, chemlist=namedSubstances, listedSubstances=listedSubstances)

@app.route('/addtoinv', methods=["Post"])
def addtoinv():
  inv = GetInv()
  newEntry = json.loads(request.form['newEntry'])
  inv.append(hyginus.Process(newEntry))
  indexpos = len(inv) + 1
  print(inv)
  return render_template("list_item_template.html", indexpos=indexpos, item=newEntry)

@app.route("/update", methods=["POST"])
def update():
  inv = GetInv()
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
    errorstring = str(traceback.print_exc())
    errorstring = errorstring + str(e) + str(inv)
    ReportError(errorstring)
    return f"An Error Occured: {e}. Please try again. If the error persists: please contact us directly."

@app.route('/results')
@login_required
def results():
  inv = GetInv()
  if len(inv) > 0:
    try:
      results = hyginus.assessment(inv)
      for listedSubKey in results['usedListedSubstances'].keys():
        if type(results['usedListedSubstances'][listedSubKey]) is float:
          results['usedListedSubstances'][listedSubKey] = round(results['usedListedSubstances'][listedSubKey], 2)
      for item in inv:
        if type(item['qty']) is float:
          item['qty'] = round(item['qty'], 2)
        if "flag" in item.keys() and item["flag"] == True:
          results['flag'] = True
      recommendation = results["finalTier"]
      results["indTier"] = hyginus.convertNumberToWord(results["indTier"])
      results["finalTier"] = hyginus.convertNumberToWord(results["finalTier"])
      results["aggregateTier"] = hyginus.convertNumberToWord(results["aggregateTier"])
      print("Inventory: ")
      for item in inv:
        if type(item["tier"]) == int:
          item["tier"] = hyginus.convertNumberToWord(item["tier"])
        print(item)
      print("Generating Results Page - SUCCESS!")
      print("Results: " + str(results))
      print("Recommendation: " + str(recommendation))
      if "flaggedSubstances" in results.keys():
        results["flaggedSubstances"] = hyginus.RemoveDuplicates(results["flaggedSubstances"])
      return render_template('results.html', results = results, inv = inv, recommendation=recommendation)
    except Exception as e:
      errorstring = str(traceback.print_exc())
      errorstring = errorstring + str(e) + str(inv)
      ReportError(errorstring)
      errorPage(e, errorType="assessfail")
      return render_template('errorPage.html', e=e, errorType="assessfail")
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
  try:
    for inventory in inventories:
      if inventory['invId'] == session['_id']:
        inventory['inv'].clear()
        return "Cleared"
    inventories.append({'invId': session['_id'], "inv": []})
    return "Cleared"
  except Exception as e:
    inv = GetInv()
    errorstring = str(traceback.print_exc())
    errorstring = errorstring + str(e) + str(inv)
    ReportError(errorstring)
    return "FAIL"


@app.route("/updatehphrases", methods=["Post"])
def updatehphrases():
  entry = json.loads(request.form['substance'])
  print(entry)
  # check if substance not named substances database
  searchtype = entry["searchtype"]
  for chem in namedSubstances:
    if entry["field"] == chem[searchtype]:
      category = MasterCategoryController(chem["hazardPhrases"],chem["chemid"])
      findings = {"found": True, "foundresult": "named", "category": category, "retry": False, "recordTitle": chem["name"], "CAS": chem["CAS"], "hazardPhrases": chem["hazardPhrases"], "UN": chem["UN"], "chemtype": "named"}
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
    query = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/UN%20{un}/json"

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
      category = MasterCategoryController(hazardPhrases, cid)
      findings = {"found": True, "foundresult": "final", "recordTitle": recordTitle, "hazardPhrases": hazardPhrases, "chemid": cid, "category": category, "chemtype": "listed"}
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
@login_required
def testinventory():
  inv = GetInv()
  while len(inv) < 5:
    usedchemids = []
    namedSubstancesLength = len(namedSubstances)
    randomnumber = randint(0,namedSubstancesLength)
    newrandomchemid = namedSubstances[randomnumber]["chemid"]
    for chem in namedSubstances:
      if len(inv) < 5 and newrandomchemid not in usedchemids and chem["chemid"] == newrandomchemid:      
        usedchemids.append(chem["chemid"])
        result = chem
        print(result)
        try:
          result["category"] = MasterCategoryController(chem["hazardPhrases"], chem["chemid"])
        except:
          try:
            manualResults = hyginus.manualget(chem)
            result["hazardPhrases"] = manualResults["hazardPhrases"]
            result["chemid"] = manualResults["chemid"]
            result["category"] = MasterCategoryController(result["hazardPhrases"], result["chemid"])
          except:
            result["category"] == "FAIL"
        if result['category'] != "FAIL":
          result["id"] = "test_id_" + str(randint(0,10000))
          maxqty = int(chem["tier3"] * 1.5)
          result["qty"] = randint(0,maxqty)
          newFloat = randint(0,10) / randint(1,10)
          result["qty"] = result["qty"] + newFloat
          inv.append(result)        
  return render_template("inventory.html", inventory=inv, chemlist=namedSubstances, listedSubstances=listedSubstances, flammableLiquidWarning=flammableLiquidWarning)


@app.route('/errorReport', methods=["Post"])
def errorReportAPI():
  errorReportVar = json.loads(request.form['errorreport'])
  print("Error Report: ", str(errorReportVar))
  inv = GetInv()
  ReportError(str(errorReportVar) + str(inv))