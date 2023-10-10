#!/usr/bin/python3

from flask import Flask
from flask import render_template


@app.route("/configurator/")
def gatherparams():
    try:
        params={}
        params['hostname'] = request.args.get('hostname')


        return render_template("baseIOS.conf.j2", **params)
    except Exception as err:
        return f"Error at {err}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
