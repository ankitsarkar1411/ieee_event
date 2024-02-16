from flask import Flask,render_template,request,redirect
app=Flask(__name__)
@app.route("/")
def homepage():
    return "Hey ALL!!"
if __name__=="__main__":
    app.run(debug=True)
@app.route("/")
def login():
    return "This is login page"
@app.route("/")
def about():
    return "This is about page"
@app.route("/")
def logout():
    return "This is logout page"

