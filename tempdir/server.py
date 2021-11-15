from flask import Flask, redirect, url_for, render_template,request
import ipapi
app = Flask(__name__)

@app.route("/")
def home():
	return render_template ("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/content",methods = ['GET','POST'])
def content():
	search = request.form.get('search')
	data = ipapi.location(ip = search,output = 'json')

	return render_template("content.html",data = data)

if __name__ == "__main__":
	app.run(host = "0.0.0.0",port = 5050,debug=True)