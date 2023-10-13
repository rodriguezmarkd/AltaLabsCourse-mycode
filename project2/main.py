#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import paramiko
import os

app = Flask(__name__)
configparams = {}

@app.route("/success/<hn>?<ia>")
def success(hn, ia):
    print(configparams)
    with open("tempconfig","w") as configfile:
        print(render_template("iosconfig.conf.j2", **configparams), file=configfile)
    h = paramiko.Transport("10.10.2.3", 22)
    h.connect(username="bender", password="alta3")
    sftp = paramiko.SFTPClient.from_transport(h)
    sftp.put("tempconfig", "/home/bender/config")
    sftp.close()
    h.close()
    return render_template("iosconfig.html", **configparams)

@app.route("/")
def start():
    return render_template("homepage.html")

@app.route("/params", methods = ["POST"])
def params():
    if request.method == "POST":
        if request.form.get("host"):
            hostname = request.form.get("host")
            configparams['hostname'] = request.form.get("host")
            ipadd = request.form.get("ip")
            configparams['ip'] = request.form.get("ip")
            configparams['domain'] = request.form.get("domain")
            configparams['nameserver'] = request.form.get("nameserver")
            configparams['subnet'] = request.form.get("subnet")
            configparams['gateway'] = request.form.get("gateway")
    return redirect(url_for("success", hn = hostname, ia = ipadd))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
