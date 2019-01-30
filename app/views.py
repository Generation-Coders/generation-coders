from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/showcase')
def showcase():
	return render_template('showcase.html')

@app.route('/showcase/<place>')
def reflections(place):
	return render_template('reflections/{0}.html'.format(place))

@app.route('/upcoming')
def upcoming():
	return render_template('upcoming.html')

@app.route('/resources')
def resources():
	return render_template('resources.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')
