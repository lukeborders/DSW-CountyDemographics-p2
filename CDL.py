from Flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)
@app.route("/index.html")
def get_state_options(counties):
  for s in counties:
    if s["counties"] == stateVar += Markup("<option value=\"" + s + "\">" + s + "</option>"):
      return stateVar

if __name__ == '__main__':
  main()
