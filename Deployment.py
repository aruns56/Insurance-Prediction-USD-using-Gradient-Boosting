# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:50:11 2021

@author: arun
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import os
os.chdir("C://users//arun//Downloads")

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("gb.pkl","rb")
gb=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_charges(age,sex,bmi,children,smoker,region):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
      - name: sex
        in: query
        type: number
        required: true
      - name: bmi
        in: query
        type: number
        required: true
      - name: children
        in: query
        type: number
        required: true
      - name: smoker
        in: query
        type: number
        required: true
      - name: region
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=gb.predict([[age,sex,bmi,children,smoker,region]])
    print(prediction)
    return prediction



def main():
    st.title("Insurance Charges")
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Insurance Charges Predictor App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age","Eg. 18,25,30")
    sex = st.text_input("Sex","Male-1,Female-0")
    bmi = st.text_input("BMI","Eg. 20,17,30,28")
    children = st.text_input("Children","no. of children-0,1,2,3,4,5..")
    smoker = st.text_input("Smoker","yes-1,no-0")
    region = st.text_input("Region","NW-1,NE-4,SW-3,SE-2")
    result=""
    if st.button("Predict"):
        result=predict_charges(age,sex,bmi,children,smoker,region)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()