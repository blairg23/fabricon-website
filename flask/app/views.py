from flask import render_template
from app import app

import json

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/index']
	return render_template(
							'index.html',
							page=page
						)

@app.route('/about')
def about():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/about']
	return render_template(
							'about.html',							
							page=page
						)

@app.route('/contact')
def contact():
	page = {
			"title": "Contact Us",
			"jumbotron": "Contact Us."
	}
	return render_template(
							'contact.html',
							page=page
						)

@app.route('/products')
def products():
	page = {
			"title": "Products",
			"jumbotron": "Products."
	}
	return render_template(
							'products.html',
							page=page							
						)

@app.route('/user')
@app.route('/user/<string:username>')
def user(username='Mr. McDefault'):
	username = username
	user = {'nickname': username}  # fake user
	with open('app/posts.json', 'r') as infile:
		data = json.load(infile)
	posts = data['posts']
	print posts
	return render_template(
							'users.html',
							title='Home',
							user=user,
							posts=posts
						)