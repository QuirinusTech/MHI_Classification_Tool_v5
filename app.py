from flask import Flask, jsonify, request, flash, redirect, render_template, url_for, send_from_directory, session, g, abort

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template("welcome.html")

inv = [{'CAS': "1234", 'name': "banana", "type": "type2", "class": "class4", "id": "42", "qty": '300'}, {'CAS': "122234", 'name': "ban23ana", "type": "t23ype2", "class": "clas23s4", "id": "4232", "qty": '32300'}, {'CAS': "6969", 'name': "name6969", "type": "type6969", "class": "6969class", "id": "69id", "qty": '6900'}]

@app.route('/inventory')
def inventory():
  return render_template("list.html", inventory=inv, chemlist=chemlist)

chemlist = ["Ammonia anhydrous","Ammonium nitrate-1","Ammonium nitrate-2","Ammonium nitrate-3","Ammonium nitrate-4","Potassium nitrate-1","Potassium nitrate-2","Arsenic pentoxide", "arsenic (V) acid and/or salts","Arsenic trioxide", "Arsenious (III) acid and/or salts", "Bromine", "Chlorine", "Nickel compounds", "Ethyleneimine", "Fluorine", "Formaldehyde", "Hydrogen", "Hydrogen chloride", "Hydrogen fluoride", "Lead alkyls", "LPG", "Acetylene", "Ethylene oxide", "Propylene oxide", "Methanol", "Methylenebis", "Methyl isocyanate", "Oxygen", "Toluene diisocyanate", "Carbonyl dichloride", "Arsenic trihydride", "Phosphorus trihydride", "Sulphur dichloride", "Sulphur dioxide", "Sulphur trioxide"]