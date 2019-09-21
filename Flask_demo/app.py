# -*- coding: utf-8 -*-

#from flask import Flask
#from flask import Flask, render_template
from flask import Flask , render_template, request, url_for
from validator import name_validator
app = Flask(__name__)

@app.route("/abc")
def main():
    return "Hello World! My name is XYZ and I am from Jaipur"

@app.route("/hello", methods = ["GET", "POST"])
def welcome():
    if request.method == "GET":
        return "Hello this is a Flask Web App trial."
    elif request.method == "POST":
        return "Welcome POST method"

@app.route("/welcome")
def welcome_2():
    details = ["XYZ", "19", "Male"]
    return render_template("demo.html", details = details)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/validation", methods=["POST"])
def form_data():
	data = request.form
	name = data["name"]
	response = name_validator(name)
	return render_template("response.html", response=response)
    
if __name__ == "__main__":
    app.run(debug=True)