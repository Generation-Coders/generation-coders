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

@app.route('/upcoming')
def upcoming():
	return render_template('upcoming.html')

# @app.route('/resources')
# def index():
# 	return render_template('resources.html')