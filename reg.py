#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Author: Mutemwa Masheke
#-----------------------------------------------------------------------

from profiles_create import create_profile
from profiles_get import get_profiles
from profiles_edit import edit_profile
import requests
import socket
from flask import Flask, request, jsonify

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

# route for landing page which lists enables profile search
@app.route('/', methods=['GET', 'POST'])
@app.route('/updatelocation', methods=['GET', 'POST'])
def updatelocation():
    user_key = request.args.get('key')
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_addr = socket.gethostbyname(hostname)
    response = requests.get(f"http://ip-api.com/json/{ip_addr}?fields=city")
    location = response.json()
    # edit_profile(user_key=user_key, args={"location": location})
    return jsonify(ip_addr)

# route for searchresults - helper to index
@app.route('/getprofile', methods=['GET'])
def getprofile():
    keys = ["name", "email", "federate", "location", "key", "age", "role"]
    details = {}
    for k in keys:
        if request.args.get(k):
            arg = request.args.get(k) if request.args.get(k) else ""
            details[k] = arg
    response = get_profiles(details)
    return jsonify(response)

@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    if not request.args.get("key"):
        raise Exception("No key provided")

    keys = ["name", "email", "federate", "location", "key", "age", "role"]
    details = {}
    for k in keys:
        if request.args.get(k):
            arg = request.args.get(k) if request.args.get(k) else ""
            details[k] = arg
    response = edit_profile(details["key"], details)
    return jsonify(response)

@app.route('/createprofile', methods=['GET', 'POST'])
def createprofile():
    if not request.args.get("key"):
        raise Exception("No key provided")
        
    keys = ["name", "email", "federate", "location", "key", "age", "role"]
    details = {}
    for k in keys:
        if request.args.get(k):
            arg = request.args.get(k) if request.args.get(k) else ""
            details[k] = arg

    print(details)
    response = create_profile(details)
    return jsonify(response)

@app.route('/createdatabase', methods=['GET', 'POST'])
def createprofile():
    if not request.args.get("key"):
        raise Exception("No key provided")
        
    keys = ["name", "email", "federate", "location", "key", "age", "role"]
    details = {}
    for k in keys:
        if request.args.get(k):
            arg = request.args.get(k) if request.args.get(k) else ""
            details[k] = arg

    print(details)
    response = create_profile(details)
    return jsonify(response)