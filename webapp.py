from flask import Flask, url_for, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)
@app.route('/')
def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template("index.html",options = get_state_options(counties))
def get_state_options(state):
    options = ""
    dictStates = {}  # empty dictionary
    for d in state:  # loops in empty dict adding states
        if d["State"] in dictStates:
            dictStates[d["State"]] += 1
        else:
            dictStates[d["State"]] = 1
    for c in dictStates:
        options += Markup("<option value=\"" + c + "\">" + c + "</option>")
    return options
@app.route('/response.html')
def render_response():
    stateName = request.args["State"]
    if stateName == counties["State"]:
        reply = stateName
    return render_template('response.html',stateNameVar = reply)
 
if __name__ == '__main__':
    main()
