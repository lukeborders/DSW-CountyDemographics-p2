from flask import Flask, url_for, request, Markup, render_template, flash, Markup
import os
import json
with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
app = Flask(__name__)
@app.route('/')
def main():
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
if __name__ == '__main__':
    main()
