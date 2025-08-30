import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.title("House Price Prediction App")

st.divider()

st.write("This app predicts the price of a house based on given features.")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=0)
living_area = st.number_input("Living Area (in sqft)", min_value=0, value=2000)
condition = st.number_input("Condition of the House", min_value=1, value=3)
no_schools = st.number_input("Number of Schools Nearby", min_value=0, value=0)

st.divider()

x =[[bedrooms,bathrooms,living_area,condition,no_schools]]

predictbutton = st.button('Predict')
if predictbutton:
    st.balloons()
    x_array = np.array(x)

    prediction = model.predict(x_array)[0]
    st.write(f"Predicted price is {prediction:,.2f}")


else:
    st.write("Please use predict button after entering value")



















