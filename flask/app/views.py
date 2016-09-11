from flask import render_template
from app import app

import json

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	page = {
			"title": "Home Page",
			"jumbotron": "Welcome to Fabricon!",
			"images": [
						"/static/img/1.jpg",
						"/static/img/2.jpg",
						"/static/img/3.jpg",
						"/static/img/4.jpg",
						"/static/img/5.jpg"
					]
	}
	return render_template(
							'index.html',
							page=page							
						)

@app.route('/about')
def about():
	page = {
			"title": "About Fabricon",
			"jumbotron": "About Fabricon."
	}
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