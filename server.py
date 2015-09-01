from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
import json
import os 
from wtforms import Form, BooleanField, StringField, validators

app = Flask(__name__)


app.config['SECRET_KEY'] = "ASECRET"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/get_rates', methods=['GET'])
def get_rates():
 	
 	rate_params = {}

 	print rate_params

	annualincome = request.args.get('annualincome', '')
	print annualincome

	rate_params['annualincome'] = int(annualincome)
	print rate_params

	monthlypayment = request.args.get('monthlypayment', '')
	rate_params['monthlypayment'] = int(monthlypayment)

	down = request.args.get('down', '')
	rate_params['down'] = int(down)

	monthlydebts = request.args.get('monthlydebts', '')
	rate_params['monthlydebts'] = int(monthlydebts)

	rate = request.args.get('rate', '')
	rate_params['rate'] = int(rate)

	schedule = request.args.get('schedule', '')
	rate_params['schedule'] = str(schedule)

	term = request.args.get('term', '')
	rate_params['term'] = int(term)

	debttoincome = request.args.get('debttoincome', '')
	rate_params['debttoincome'] = int(debttoincome)

	incometax = request.args.get('incometax', '')
	rate_params['incometax'] = int(incometax)

	propertytax = request.args.get('propertytax', '')
	rate_params['propertytax'] = int(propertytax)

	hazardinsurance = request.args.get('hazardinsurance', '')
	rate_params['hazard'] = int(hazardinsurance)

	pmi = request.args.get('pmi', '')
	rate_params['pmi'] = int(pmi)

 	zipc = request.args.get('zipc', '')
	rate_params['zipc'] = int(zipc)

 	true = request.args.get('True', '')
 	false = request.args.get('False', '')
	# if true === 'True':
		# rate_params['estimate'] = True
	# if false === 'False':
		# rate_params['estimate'] = False

 	zwsid = 'X1-ZWz1eunt26vguj_6msnx'
	rate_params['zws-id'] = str(zwsid)

 	output = 'json'
	rate_params['output'] = output
	print output
	print rate_params

	rate_api_resp = requests.get('http://www.zillow.com/webservice/mortgage/CalculateAffordability.htm?', params=rate_params)
	rate_info_api = rate_api_resp.json()
	print rate_info_api
	print rate_info.keys()
	print rate_info.values()
	rate_info = rate_info_api['response']

	rate_info_lastWeek = rate_info_api['response']['lastWeek']
	rate_info_today = rate_info_api['response']['today']

	return render_template('rates.html', rate_info=rate_info)	
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))

	app.debug = True

	DebugToolbarExtension(app)
	app.run(host='0.0.0.0', port=port)