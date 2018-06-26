#!flask/bin/python

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index2')
def index2():
	return render_template('index2.html')

@app.route('/index3')
def index3():
	return render_template('index3.html')

@app.route('/pages/widgets')
def widgets():
	return render_template('pages/widgets.html')

@app.route('/pages/calendar')
def calendar():
	return render_template('pages/calendar.html')

@app.route('/pages/charts1')
def chartsa():
	return render_template('pages/charts/chartjs.html')

@app.route('/pages/charts2')
def chartsb():
	return render_template('pages/charts/flot.html')

@app.route('/pages/charts3')
def chartsc():
	return render_template('pages/charts/inline.html')

@app.route('/pages/general')
def general():
	return render_template('pages/UI/general.html')

@app.route('/pages/buttons')
def buttons():
	return render_template('pages/UI/buttons.html')

@app.route('/pages/icons')
def icons():
	return render_template('pages/UI/icons.html')

@app.route('/pages/sliders')
def sliders():
	return render_template('pages/UI/sliders.html')

@app.route('/pages/generals')
def generals():
	return render_template('pages/forms/general.html')

@app.route('/pages/advanced')
def advanced():
	return render_template('pages/forms/advanced.html')

@app.route('/pages/editors')
def editors():
	return render_template('pages/forms/editors.html')

@app.route('/pages/simple')
def simple():
	return render_template('pages/tables/simple.html')

@app.route('/pages/data')
def data():
	return render_template('pages/tables/data.html')

@app.route('/pages/mailbox')
def mailbox():
	return render_template('pages/mailbox/mailbox.html')

@app.route('/pages/compose')
def compose():
	return render_template('pages/mailbox/compose.html')

@app.route('/pages/read-mail')
def readmail():
	return render_template('pages/mailbox/read-mail.html')

@app.route('/pages/invoice')
def invoice():
	return render_template('pages/examples/invoice.html')

@app.route('/pages/profile')
def profile():
	return render_template('pages/examples/profile.html')

@app.route('/pages/login')
def login():
	return render_template('pages/examples/login.html')

@app.route('/pages/register')
def register():
	return render_template('pages/examples/register.html')

@app.route('/pages/lockscreen')
def lockscreen():
	return render_template('pages/examples/lockscreen.html')

@app.route('/pages/exta1')
def exta1():
	return render_template('pages/examples/404.html')

@app.route('/pages/extra2')
def extra2():
	return render_template('pages/examples/500.html')

@app.route('/pages/extra3')
def extra3():
	return render_template('pages/examples/blank.html')

@app.route('/starter')
def starter():
	return render_template('starter.html')

if __name__ == '__main__':
   app.run(debug = True)


