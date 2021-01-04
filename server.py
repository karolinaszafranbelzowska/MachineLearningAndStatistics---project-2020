# Machine Learning and Statistics - project 2020
# Karolina Szafran-Belzowska G00376368


# Taken from - https://github.com/ianmcloughlin/random-app/blob/master/rando.py


import flask as fl
from flask import Flask
import tensorflow.keras as kr
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
import json #?


# tensorflow documentation on saving and loading a model - https://www.tensorflow.org/guide/keras/save_and_serialize
# from tensorflow import keras - not working ?
# model = load_model("model_w.h5")


# Create a new web app.
app = Flask(__name__)


# Add root route.
# This will serve out the index.html page at the root
@app.route("/")
def home():
  return app.send_static_file('index.html')






if __name__ == '__main__':
    app.run(debug= True)