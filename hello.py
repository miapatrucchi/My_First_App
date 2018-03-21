from flask import Flask, render_template

# here we are defining our app 
app = Flask ("MyApp")

# @app.route is a decorator, every time you write @app.route you are writing a new URL route 
@app.route("/")
def hello ():
	return "Goodbye World!"


@app.route("/idontexist")
def idontexist ():
	return "I do exist now"

@app.route ("/MiaPatrucchi")
def MiaPatrucchi ():
	return "That's my name"

app.run(debug=True)