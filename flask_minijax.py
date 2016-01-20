"""
Tiny demo of Ajax interaction
"""

import flask
from flask import request  # Data from a submitted form
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging
import argparse  # For the vocabulary list
import sys

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.COOKIE_KEY  # Should allow using session variables

#
# One shared 'Vocab' object, read-only after initialization,
# shared by all threads and instances.  Otherwise we would have to
# store it in the browser and transmit it on each request/response cycle, 
# or else read it from the file on each request/responce cycle,
# neither of which would be suitable for responding keystroke by keystroke.
#


###
# Pages
###

@app.route("/")
def index():
  return flask.render_template('minijax.html')

###############
# AJAX request handlers 
#   These return JSON, rather than rendering pages. 
###############

@app.route("/_countem")
def countem():
  text = request.args.get("text", type=str) #checking the whole word
  length = len(text)
  rslt = { "long_enough": length > 5 } #this is a dictionary cuz javascript object is a dict
  return jsonify(result=rslt) #jsonify makes the dictionary into a string and send the string version of the dict
                                #but when you get it back in the html page it's back to being a dict. json just
                                #makes it into a string for sending it 

#############

# Run locally
if __name__ == "__main__":
    # Standalone. 
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

