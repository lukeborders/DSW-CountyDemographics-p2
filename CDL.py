from Flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)
@app.route("/index.html")
def get_state_options(counties):
    for c in counties:
        if c["counties"] == options += Markup("<option value=\"" + countyVar + "\">" + countyVar + "</option>"):
            return countyVar
def state_fact(state):
    for s in counties:
        if s["county"]["state"] == options += Markup("<option value=\"" + stateVar + "\">" + stateVar + "</option>"):
            
if __name__ == '__main__':
    main()
