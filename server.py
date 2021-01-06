# Machine Learning and Statistics - project 2020
# Karolina Szafran-Belzowska G00376368


# Taken from - https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# libraries
import flask as fl
import numpy as np 
from tensorflow.keras.models import model_from_json
from flask import Flask, url_for, request, redirect, abort, jsonify

# Create a new web app.
app = fl.Flask(__name__) # the main script in the program. 

# Add root route.
@app.route("/")
def home():
  return app.send_static_file("index.html")
# Prediction routine to run here

def model_predict(wind):
    wind = float(wind)
    # load json and create model # not working
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    power = loaded_model.predict([wind])
    power = round(float(power), 2)
    return power

@app.route("/api/power/<wind>")
def power_predict(wind):
    return {"power" : model_predict(wind)}
    
if __name__ == "__main__":
    app.run(debug= True) 