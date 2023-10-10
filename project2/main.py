#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
'''
@app.route("/configurator/")
def gatherparams():
    try:
        params={}
        params['hostname'] = request.args.get('hostname')


        return render_template("baseIOS.conf.j2", **params)
    except Exception as err:
        return f"Error at {err}"
'''
@app.route("/success/<hn>?<ia>")
def success(hn, ia):
    return f"Welcome {hn},\n {ia}"

@app.route("/")
def start():
    return render_template("homepage.html")

@app.route("/params", methods = ["POST"])
def params():
    if request.method == "POST":
        if request.form.get("host"):
            hostname = request.form.get("host")
    if request.method == "POST":
        if request.form.get("ip"):
            ipadd = request.form.get("ip")
    return redirect(url_for("success", hn = hostname, ia = ipadd))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
