![](images/logo_GMIT.jpeg)

# Machine Learning and Statistics---project-2020

## Higher Diploma in Data Analytics, Lecturer: Ian McLoughlin: ian.mcloughlin@gmit.ie
### Karolina Szafran-Belzowska, G00376368

This repository has been carried out as Assignment of the Machine Learning and Statistics Module of the Higher Diploma In Data Analytics at GMIT.


## Content of The Github Repository

- images (folder)
- static (folder)
- ReadMe.md
- LICENSE
- requirements.txt
- .gitignore
- powerproduction.csv
- MLS-project instructions 2020.pdf
- ML_and_S_project.2020.ipynb
- sever.py
- model.h5
- model.json
- Dockerfile
- .dockerignore

## Overwiev

This project creates a web service that uses machine learning to make predictions based on the dataset powerproduction. The goal is to produce a model that accurately predicts wind speed values. The web service will respond with predicted power values based on speed values sent as HTTP requests. 
The assignment was implemented in Python Language. Here are all details: [here](https://github.com/karolinaszafranbelzowska/MachineLearningAndStatistics---project-2020/blob/main/MLS%20-%20project%20instructions%202020.pdf)

## Packages used in this project

- Python 3 https://docs.python.org/3/
- Numpy http://www.numpy.org/ 
- Jupyter Notebook https://jupyter.org/ 
- Pandas https://pandas.pydata.org/
- Scipy.stats https://docs.scipy.org/doc/scipy/reference/stats.html
- Matplotlib.pylab https://matplotlib.org/
- Flask https://flask.palletsprojects.com/en/1.1.x/
- Seaborn https://seaborn.pydata.org/
- Tensorflow.keras https://www.tensorflow.org/, https://keras.io/
- Scikit-learn https://scikit-learn.org/stable/

## How to run web app

### Flask
LINUX
> export FLASK_APP=server.py

> python3 -m flask run

WINDOWS
> set FLASK_APP=server.py

> python -m flask run

Python is running in the background. It runs Flask Web Application.
Copy a special IP address (http://127.0.0.1:5000/), go to the Browser and paste this address into the URL.
My Web Application is running the function.
Use CTRL + C to kill the application.

### Docker
> docker build -t server-app

It goes and build an image from my repository

> docker run server-app

> docker run -d -p 5000:5000 server-app

> docker container ls
 (check if my container is running) 
 
> docker kill (container ID)

To delete use:
> docker rm (container ID) 

To see images use:
> docker image ls

To stop server running use: ctrl + c


## How to run Jupyter Notebook
In the Comannd Prompt type the path to the folder where the project is located:
> cd desktop

> cd MachineLearningAndStatistics---project-2020

> jupyter notebook


## References:

- https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/keras-neurons.ipynb, 02/01/2021
- https://keras.io/, 02/01/2021
- https://en.wikipedia.org/wiki/Wind_turbine, 03/01/2021
- https://www3.ntu.edu.sg/home/, 03/01/2021
- https://machinelearningmastery.com/, 03/01/221
- https://www.w3schools.com/python/
- https://en.wikipedia.org/wiki/Wind_turbine
- https://en.wikipedia.org/wiki/Wind_power
- https://ksopyla.com/machine-learning/modele-regresji-liniowej-z-scikit-learn/
- https://ichi.pro/pl/algorytm-regresji-liniowej-od-podstaw-w-pythonie-253366674175694

GitHub repositories:

- https://github.com/Freeha-S?tab=repositories
- https://github.com/doriszd?tab=repositories
- https://github.com/johndunne2019?tab=repositories
- https://github.com/andkoc001?tab=repositories
- https://github.com/IanWafer?tab=repositories


