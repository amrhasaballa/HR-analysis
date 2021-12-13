from flask import Flask, render_template, Response,jsonify, make_response,request,redirect,url_for
import pandas as pd
import json
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import xml.etree.ElementTree as ET
import sklearn.metrics
from sklearn.metrics import confusion_matrix,classification_report,plot_confusion_matrix



loaded_model = pickle.load(open(r'F:\model_sav', 'rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('emp_hankasha.html')

@app.route('/login',methods = ['POST'])
def login():
    print(request.form)
    JobRole = request.form['JobRole']
    EducationField = request.form['EducationField']
    JobLevel = request.form['JobLevel']
    Age = request.form['Age']
    MonthlyIncome = request.form['MonthlyIncome']
    YearsInCurrentRole = request.form['YearsInCurrentRole']
    x=[int(JobRole),int(EducationField),int(JobLevel),int(Age),int(MonthlyIncome),int(YearsInCurrentRole)]
    x=pd.DataFrame(x)

    x=x.transpose()
   
    out=loaded_model.predict_proba(x)
    print(out)
    sal="{:.2%}".format(out[0][0])
    Res="{:.2%}".format(out[0][1])
    hum="{:.2%}".format(out[0][2])
    return json.dumps({ 'sal':sal,'rs':Res,'hr':hum});
   



if __name__ == "__main__":
    app.run(debug=True)