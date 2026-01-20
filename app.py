import pickle
import streamlit as st
import numpy as np
import sklearn

model=pickle.load(open('model.pkl','rb'))

st.title("Placement Predictor")

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Placement Predictor")

cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.1)

iq = st.number_input("Enter IQ", min_value=50, max_value=200, step=1)


if st.button("Predict"):
    input_data =np.array([[cgpa, iq]])
    result =model.predict(input_data)
    if result[0] ==1:
        st.success("The person is likely to be placed")
    else:
        st.error("The person is not likely to be placed")

