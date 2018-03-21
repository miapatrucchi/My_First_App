from flask import Flask, render_template, request

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

@app.route ("/<name>")
# the 'name' in brackets is a variable. THe {{}} in the html file are allowing us to make it variable in html
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	print form_data["email"]
	return "All OK"

app.run(debug=True)