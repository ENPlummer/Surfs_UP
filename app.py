from flask import Flask, render_template, redirect, jsonify


#dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurements = Base.classes.measurements
Stations = Base.classes.stations

session = Session(engine)

@app.route("/")
def Home():
	return (f"Welcome to the Surfs Up Weather API!<br>"
		    f"Available Routes:<br>"
		    f"/api/v1.0/Precipitation"
		    f"/api/v1.0/Stations"
		    f"/api/v1.0/tobs"
		    f"/api/v1.0/<start>"
		    f"/api/v1.0/<start>/<end>"
		)
@app.route("/welcome")
def Welcome():
	print("Server received request for the 'Welcome Page'")
	return "Welcome to the Surfs up Weather API!"


@app.route("/api/v1.0/Precipitation")
def Precipitation():
	results = session.query(Measurements.date).filter(Measurements.date >= "2016-08-23").all()
	past_year_prcp = []
	for measurment in results:
		measurements_dict = {}
		measurements_dict["date"] = measurements.date
		measurements_dict["prcp"] = measurements.prcp
		past_year_prcp.append(measurements_dict)

	return jsonify(past_year_measurements)

@app.route("/api/v1.0/Stations")
def Stations():
	results = session.query(Stations.stations).all()
	all_stations = list(np.raval(results))
	return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def Temperature():
	results = session.query(Measurements.date,Measurements.tobs)filter(Measurements.date >= "2016-08-23").all()
	past_year_tobs = list(np.raval(results))

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")




if __name__ == '__main__':
    app.run(debug=True)