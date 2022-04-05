#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Mutemwa Masheke
#-----------------------------------------------------------------------

from sys import stderr
from urllib import response
from flask import Flask, request, make_response
from flask import render_template
import json
from flask import jsonify

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

# route for landing page which lists enables profile search
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response

def argument(argtext):
    return "${" + str(argtext) + "}"

def isValidUser(database, key, location):
    return (database["key"] == argument(key) and database["location"] == argument(location))

# route for searchresults - helper to index
@app.route('/getprofile', methods=['GET'])
def searchresults():
    keys = ['key', 'location']
    details = dict.fromkeys(keys)

    details['key'] = request.args.get('key')
    details['location'] = request.args.get('location')

    if details['key'] is None:
        details['key'] = ''
    if details['location'] is None:
        details['location'] = ''

    response = {"location": details['location'], "key": details['key']}

    if isValidUser(details, "Mutemwa", "Lusaka"):
        response.update({"FullName": "Mutemwa Masheke"})
        response.update({"Age": 21})
        response.update({"email": "mmasheke@princeton.edu"})
        response.update({"UserExists": True})

    elif isValidUser(details, "Aneekah", "Montclair"):
        response.update({"FullName": "Aneekah Uddin"})
        response.update({"Age": 21})
        response.update({"email": "auddin@princeton.edu"})
        response.update({"UserExists": True})

    elif isValidUser(details, "Zaid", "Dhahran"):
        response.update({"FullName": "Zaid Albarghouty"})
        response.update({"Age": 20})
        response.update({"email": "zaidma@princeton.edu"})
        response.update({"UserExists": True})

    else:
        response.update({"UserExists": False})

    return jsonify(response)