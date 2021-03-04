import numpy as np
import streamlit as st
import pandas as pd
import pickle
from pickle import load
from scipy.special import boxcox, inv_boxcox



# Layout
# st.beta_set_page_config(layout="wide") # NEW FEATURE !
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

# Title
st.title("House Rental Price Predictor in Madrid 🏡💲")

# Description
st.markdown("""

**Description**: Created an app using machine learning tools that estimates rental prices from Madrid houses which can aid flat owners as well as people looking for a house to get an idea of the Real State Market in Madrid. 

""")

# About
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python libraries used:** pandas, numpy, beautifulsoup, sklearn, scipy, matplotlib, seaborn, flask, json, pickle
* **Data scrapped from [www.pisos.com](https://www.pisos.com/ )**.
""")

col1.markdown("""
**Please, select your input parameters below:**
""")
# Area input
area = col1.number_input("Introduce the area of the house (Square meters):",0.0,5000.0, 100.0, format="%.1f")

# Number Rooms input
bedrooms = col1.select_slider("How many bedrooms in total?:", list(range(1,15)), 5)

# Number BathRooms input
bathrooms = col1.select_slider("How many bathrooms in total?:", list(range(1,8)), 2)

locat = ["arganzuela", "barajas", "carabanchel", "centro", "chamartin", "chamberi", "ciudad lineal", "fuencarral-el pardo", "hortaleza", "latina", "moncloa-aravaca", "moratalaz", "puente de vallecas", "retiro", "salamanca", "san blas", "tetuan", "usera", "vicalvaro", "villa de vallecas", "villaverde"]
locat = [i.capitalize() for i in locat]

# Location
location = col1.selectbox("Select the location of the house", locat)

# Model
with open("Madrid_rent_price.pickle", 'rb') as pickle_file:
    model = pickle.load(pickle_file)

# Load X file
X = pd.read_csv("X.csv")

def predict_price(location, area, bedrooms, bathrooms):
    loc_index = np.where(X.columns==location)[0][0] # X is an np array so we use where method to loc the index
    
    x= np.zeros(len(X.columns))
    x[0] = boxcox(area,0)
    x[1] = boxcox(bedrooms,0)
    x[2] = boxcox(bathrooms,0)
    if loc_index >= 0:
        x[loc_index] = 1
    
    return "The rental predicted price for this house is " + " ".join((str(round(inv_boxcox(model.predict([x])[0],0))), "euros per month."))


# Prediction
if st.button("Predict"):
    result = predict_price(location, area, bedrooms, bathrooms)
    st.success(result)
    # balloons
    st.balloons()



