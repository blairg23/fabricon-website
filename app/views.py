from flask import render_template
from app import app

import json

@app.route('/products/awnings_and_canopies/commercial_and_residential_awnings/awning_styles')
def commercial_and_residential_awnings_awning_styles():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/commercial_and_residential_awnings/awning_styles']
	return render_template('commercial_and_residential_awnings_awning_styles.html', page=page)

@app.route('/products/services')
def products_services():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services']
	return render_template('products_services.html', page=page)

@app.route('/products/fabric_structures/frame_supported')
def fabric_structures_frame_supported():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/frame_supported']
	return render_template('fabric_structures_frame_supported.html', page=page)

@app.route('/products/services/installation')
def services_installation():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services/installation']
	return render_template('services_installation.html', page=page)

@app.route('/products/custom/specialty_production_runs')
def custom_specialty_production_runs():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom/specialty_production_runs']
	return render_template('custom_specialty_production_runs.html', page=page)

@app.route('/products/curtains_screens_and_facades/screens')
def curtains_screens_and_facades_screens():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/screens']
	return render_template('curtains_screens_and_facades_screens.html', page=page)

@app.route('/products/curtains_screens_and_facades/facades')
def curtains_screens_and_facades_facades():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/facades']
	return render_template('curtains_screens_and_facades_facades.html', page=page)

@app.route('/products/fabric_structures/tents')
def fabric_structures_tents():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/tents']
	return render_template('fabric_structures_tents.html', page=page)

@app.route('/products/fabric_structures/deployable')
def fabric_structures_deployable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/deployable']
	return render_template('fabric_structures_deployable.html', page=page)

@app.route('/products/curtains_screens_and_facades')
def products_curtains_screens_and_facades():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades']
	return render_template('products_curtains_screens_and_facades.html', page=page)

@app.route('/products/awnings_and_canopies/canopies')
def awnings_and_canopies_canopies():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/canopies']
	return render_template('awnings_and_canopies_canopies.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains')
def curtains_screens_and_facades_curtains():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains']
	return render_template('curtains_screens_and_facades_curtains.html', page=page)

@app.route('/products/custom/marine')
def custom_marine():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom/marine']
	return render_template('custom_marine.html', page=page)

@app.route('/products/fabric_structures/shade_sails')
def fabric_structures_shade_sails():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/shade_sails']
	return render_template('fabric_structures_shade_sails.html', page=page)

@app.route('/products/custom')
def products_custom():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom']
	return render_template('products_custom.html', page=page)

@app.route('/products/fabric_structures/tipis')
def fabric_structures_tipis():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/tipis']
	return render_template('fabric_structures_tipis.html', page=page)

@app.route('/products')
def products():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products']
	return render_template('products.html', page=page)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/home']
	return render_template('index.html', page=page)

@app.route('/products/services/maintenance_and_repair')
def services_maintenance_and_repair():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services/maintenance_and_repair']
	return render_template('services_maintenance_and_repair.html', page=page)

@app.route('/products/awnings_and_canopies/commercial_and_residential_awnings')
def awnings_and_canopies_commercial_and_residential_awnings():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/commercial_and_residential_awnings']
	return render_template('awnings_and_canopies_commercial_and_residential_awnings.html', page=page)

@app.route('/products/awnings_and_canopies/retractable')
def awnings_and_canopies_retractable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/retractable']
	return render_template('awnings_and_canopies_retractable.html', page=page)

@app.route('/products/fabric_structures')
def products_fabric_structures():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures']
	return render_template('products_fabric_structures.html', page=page)

@app.route('/contact')
def contact():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/contact']
	return render_template('contact.html', page=page)

@app.route('/products/fabric_structures/tensile')
def fabric_structures_tensile():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/tensile']
	return render_template('fabric_structures_tensile.html', page=page)

@app.route('/products/awnings_and_canopies')
def products_awnings_and_canopies():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies']
	return render_template('products_awnings_and_canopies.html', page=page)

@app.route('/about')
def about():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/about']
	return render_template('about.html', page=page)

