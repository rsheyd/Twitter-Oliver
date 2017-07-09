from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('login.html')
 
@app.route('/', methods=['POST'])
def do_admin_login():
	print(request.form['handle'])
	print(request.form['volume'])
	return home()
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)