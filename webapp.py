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
def get_fact(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    fact = 0
    numCount = 0
    for c in counties:
        if state == c["State"]:
            fact += c["Miscellaneous"]["Percent Female"]
            numCount += 1
    fact = round(fact/numCount,2)
    funfact = Markup("<p>" + "Percent Female in " + state + " is, " + str(fact) + " %" + "</p>")
    return funfact


@app.route('/memes')
def render_response():
    state = request.args['state']
    return render_template('index.html',fact = get_fact(state))

if __name__ == '__main__':
    main()
