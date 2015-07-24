from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
import json
import os
import psycopg2
import urlparse
import dj_database_url

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environo["DATABASE_URL"])
conn = psycopg2.connect(
	database=url.path[1:],
	user=url.username,
	password=url.password,
	host=url.hostname,
	port=url.port
	)
DATABASES['default'] = dj_database_url.config()

app = Flask(__name__)

app.secret_key = "ASECRET"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/get_rates', methods=['GET'])
def get_rates():
 	
 	rate_params = {}

	annualincome = request.form['annualincome']
	rate_params['annualincome'] = annualincome

	monthlypayment = request.form['monthlypayment']
	rate_params['monthlypayment'] = monthlypayment

	down = request.form['down']
	rate_params['down'] = down

	monthlydebts = request.form['monthlydebts']
	rate_params['monthlydebts'] = monthlydebts

	rate = request.form['rate']
	rate_params['rate'] = rate

	schedule = request.form['schedule']
	rate_params['schedule'] = schedule

	term = request.form['term']
	rate_params['term'] = term

	debttoincome = request.form['debttoincome']
	rate_params['debttoincome'] = debttoincome

	incometax = request.form['incometax']
	rate_params['incometax'] = incometax

	propertytax = request.form['propertytax']
	rate_params['propertytax'] = propertytax

	hazard = request.form['hazard']
	rate_params['hazard'] = hazard

	pmi = request.form['pmi']
	rate_params['pmi'] = pmi

 	hoa = request.form['hoa']
	rate_params['hoa'] = hoa

 	zipc = request.form['zipcode']
	rate_params['zipc'] = zipc

 	estimate = request.form['estimate']
	rate_params['estimate'] = estimate

 	zwsid = 'X1-ZWz1eunt26vguj_6msnx'
	rate_params['zwsid'] = zwsid

 	output = 'json'
	rate_params['output'] = output


	rate_api_resp = requests.get('http://www.zillow.com/webservice/mortgage/CalculateAffordability.htm?', params=rate_params)
	rate_info_api = rate_api_resp.json()
	# print rate_info.keys()
	# print rate_info.values()
	rate_info = rate_info_api['response']

	rate_info_lastWeek = rate_info_api['response']['lastWeek']
	rate_info_today = rate_info_api['response']['today']

	return render_template('rates.html', rate_info=rate_info)	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))

	app.debug = True

	DebugToolbarExtension(app)
	app.run(host='0.0.0.0', port=port)