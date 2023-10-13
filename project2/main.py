#!/usr/bin/python3

from flask import Flask           #Importing modules needed for Flask Frontend
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import paramiko                   #Importing paramiko for SSH access to host
import os                         #OS module used for file system interactions

app = Flask(__name__)             #Default parameter setup
configparams = {}

@app.route("/success/<hn>?<ia>")  #Method to render form data in a temp config file, pushes
def success(hn, ia):              #said config file to host, and renders html for user
    print(configparams)
    with open("tempconfig","w") as configfile:
        print(render_template("iosconfig.conf.j2", **configparams), file=configfile)
    h = paramiko.Transport("10.10.2.3", 22)
    h.connect(username="bender", password="alta3")
    sftp = paramiko.SFTPClient.from_transport(h)
    sftp.put("tempconfig", "/home/bender/config")
    sftp.close()
    h.close()
    os.remove("tempconfig")       #Removes temporary config file for cleanup
    return render_template("iosconfig.html", **configparams)

@app.route("/")                   #Initial form page for data entry
def start():
    return render_template("homepage.html")

@app.route("/params", methods = ["POST"]) #Gathers data from form into dictionary
def params():
    if request.method == "POST":
        if request.form.get("host"):
            configparams['hostname'] = request.form.get("host")
            configparams['ip'] = request.form.get("ip")
            configparams['domain'] = request.form.get("domain")
            configparams['nameserver'] = request.form.get("nameserver")
            configparams['subnet'] = request.form.get("subnet")
            configparams['gateway'] = request.form.get("gateway")
    return redirect(url_for("success", hn = configparams['hostname'],ia = configparams['ip']))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
