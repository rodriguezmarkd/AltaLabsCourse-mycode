#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
configparams = {}
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
    print(configparams)
    return render_template("iosconfig.txt", **configparams)
#    return f"Welcome {hn},\n {ia}"

@app.route("/")
def start():
    return render_template("homepage.html")

@app.route("/params", methods = ["POST"])
def params():
    if request.method == "POST":
        if request.form.get("host"):
            hostname = request.form.get("host")
            configparams['hostname'] = request.form.get("host")
    if request.method == "POST":
        if request.form.get("ip"):
            ipadd = request.form.get("ip")
            configparams['ip'] = request.form.get("ip")
            configparams['domain'] = "domain"
            configparams['nameserver'] = "nameserver"
            configparams['subnet'] = "subnet"
            configparams['gateway'] = "gateway"
    return redirect(url_for("success", hn = hostname, ia = ipadd))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
