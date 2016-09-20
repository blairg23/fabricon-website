from flask import render_template
from app import app

import json

@app.route('/products/curtains_screens_and_facades/screens/vertical_roller/cable')
def vertical_roller_cable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/screens/vertical_roller/cable']
	return render_template('vertical_roller_cable.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains')
def curtains_screens_and_facades_curtains():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains']
	return render_template('curtains_screens_and_facades_curtains.html', page=page)

@app.route('/products/fabric_structures/deployable')
def fabric_structures_deployable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/deployable']
	return render_template('fabric_structures_deployable.html', page=page)

@app.route('/products/awnings_and_canopies/industrial')
def awnings_and_canopies_industrial():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/industrial']
	return render_template('awnings_and_canopies_industrial.html', page=page)

@app.route('/products/curtains_screens_and_facades/screens/vertical_roller/sun_screen')
def vertical_roller_sun_screen():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/screens/vertical_roller/sun_screen']
	return render_template('vertical_roller_sun_screen.html', page=page)

@app.route('/products/curtains_screens_and_facades')
def products_curtains_screens_and_facades():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades']
	return render_template('products_curtains_screens_and_facades.html', page=page)

@app.route('/products/curtains_screens_and_facades/screens/vertical_roller/power')
def vertical_roller_power():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/screens/vertical_roller/power']
	return render_template('vertical_roller_power.html', page=page)

@app.route('/about')
def about():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/about']
	return render_template('about.html', page=page)

@app.route('/products/curtains_screens_and_facades/screens/vertical_roller')
def screens_vertical_roller():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/screens/vertical_roller']
	return render_template('screens_vertical_roller.html', page=page)

@app.route('/products/consulting/design')
def consulting_design():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/consulting/design']
	return render_template('consulting_design.html', page=page)

@app.route('/products/awnings_and_canopies/residential')
def awnings_and_canopies_residential():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/residential']
	return render_template('awnings_and_canopies_residential.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/carrier/industrial')
def carrier_industrial():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/carrier/industrial']
	return render_template('carrier_industrial.html', page=page)

@app.route('/products/services/installation')
def services_installation():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services/installation']
	return render_template('services_installation.html', page=page)

@app.route('/products/consulting/engineering')
def consulting_engineering():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/consulting/engineering']
	return render_template('consulting_engineering.html', page=page)

@app.route('/products/custom/patterning')
def custom_patterning():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom/patterning']
	return render_template('custom_patterning.html', page=page)

@app.route('/products/awnings_and_canopies/retractable/nuimage')
def retractable_nuimage():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/retractable/nuimage']
	return render_template('retractable_nuimage.html', page=page)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/home']
	return render_template('index.html', page=page)

@app.route('/products/curtains_screens_and_facades/screens')
def curtains_screens_and_facades_screens():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/screens']
	return render_template('curtains_screens_and_facades_screens.html', page=page)

@app.route('/products/custom/marine')
def custom_marine():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom/marine']
	return render_template('custom_marine.html', page=page)

@app.route('/products/awnings_and_canopies/commercial')
def awnings_and_canopies_commercial():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/commercial']
	return render_template('awnings_and_canopies_commercial.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/carrier/light')
def carrier_light():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/carrier/light']
	return render_template('carrier_light.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/carrier')
def curtains_carrier():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/carrier']
	return render_template('curtains_carrier.html', page=page)

@app.route('/products/awnings_and_canopies/retractable/retractable_awnings')
def retractable_retractable_awnings():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/retractable/retractable_awnings']
	return render_template('retractable_retractable_awnings.html', page=page)

@app.route('/products/awnings_and_canopies/commercial/awning_styles')
def commercial_awning_styles():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/commercial/awning_styles']
	return render_template('commercial_awning_styles.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/pipe')
def curtains_pipe():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/pipe']
	return render_template('curtains_pipe.html', page=page)

@app.route('/products/awnings_and_canopies/fixed')
def awnings_and_canopies_fixed():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/fixed']
	return render_template('awnings_and_canopies_fixed.html', page=page)

@app.route('/products/fabric_structures/frame_supported')
def fabric_structures_frame_supported():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/frame_supported']
	return render_template('fabric_structures_frame_supported.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/carrier/track')
def carrier_track():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/carrier/track']
	return render_template('carrier_track.html', page=page)

@app.route('/products/fabric_structures/tents')
def fabric_structures_tents():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/tents']
	return render_template('fabric_structures_tents.html', page=page)

@app.route('/products/services')
def products_services():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services']
	return render_template('products_services.html', page=page)

@app.route('/products/awnings_and_canopies')
def products_awnings_and_canopies():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies']
	return render_template('products_awnings_and_canopies.html', page=page)

@app.route('/products/retractabledeployable')
def products_retractabledeployable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/retractabledeployable']
	return render_template('products_retractabledeployable.html', page=page)

@app.route('/products/consulting')
def products_consulting():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/consulting']
	return render_template('products_consulting.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/carrier/cable')
def carrier_cable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/carrier/cable']
	return render_template('carrier_cable.html', page=page)

@app.route('/products/awnings_and_canopies/retractable')
def awnings_and_canopies_retractable():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/awnings_and_canopies/retractable']
	return render_template('awnings_and_canopies_retractable.html', page=page)

@app.route('/products/fabric_structures/tipis')
def fabric_structures_tipis():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/tipis']
	return render_template('fabric_structures_tipis.html', page=page)

@app.route('/products/fabric_structures/shade_sails')
def fabric_structures_shade_sails():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/shade_sails']
	return render_template('fabric_structures_shade_sails.html', page=page)

@app.route('/products/fabric_structures')
def products_fabric_structures():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures']
	return render_template('products_fabric_structures.html', page=page)

@app.route('/products/services/maintenance_and_repair')
def services_maintenance_and_repair():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services/maintenance_and_repair']
	return render_template('services_maintenance_and_repair.html', page=page)

@app.route('/products/consulting/codes')
def consulting_codes():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/consulting/codes']
	return render_template('consulting_codes.html', page=page)

@app.route('/contact')
def contact():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/contact']
	return render_template('contact.html', page=page)

@app.route('/products/custom')
def products_custom():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom']
	return render_template('products_custom.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/pipe/roll_up')
def pipe_roll_up():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/pipe/roll_up']
	return render_template('pipe_roll_up.html', page=page)

@app.route('/products/fabric_structures/tensile')
def fabric_structures_tensile():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/fabric_structures/tensile']
	return render_template('fabric_structures_tensile.html', page=page)

@app.route('/products/curtains_screens_and_facades/curtains/pipe/roman')
def pipe_roman():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/curtains_screens_and_facades/curtains/pipe/roman']
	return render_template('pipe_roman.html', page=page)

@app.route('/products/services/design_engineering_and_permitting')
def services_design_engineering_and_permitting():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/services/design_engineering_and_permitting']
	return render_template('services_design_engineering_and_permitting.html', page=page)

@app.route('/products')
def products():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products']
	return render_template('products.html', page=page)

@app.route('/products/custom/specialty_production_runs')
def custom_specialty_production_runs():
	with open('app/data/pages.json', 'r') as infile:
		data = json.load(infile)
	page = data['/products/custom/specialty_production_runs']
	return render_template('custom_specialty_production_runs.html', page=page)

