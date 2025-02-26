import streamlit as st
import pickle
import numpy as np
import pandas as pd
from babel.numbers import format_decimal

# Load the trained model
with open("pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Real Estate")
st.title("🏡 Delhi House Price Prediction")

# User input fields
area = st.number_input("Area(sq ft)", min_value=100, value=1000)
latitude = st.number_input("Latitude", value=12.9)
longitude = st.number_input("Longitude", value=77.5)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=1)
neworold = st.selectbox("New or Old", ["New Property", "Resale"])
type_of_building = st.selectbox("Type of Building", ["Individual House", "Flat"])

# Furnishing status logic
if "furnished_semi" not in st.session_state:
    st.session_state["furnished_semi"] = False
if "furnished_un" not in st.session_state:
    st.session_state["furnished_un"] = False

def update_semi():
    """If 'Semi-Furnished' is checked, set 'Unfurnished' to False."""
    if st.session_state["furnished_semi"]:
        st.session_state["furnished_un"] = False

def update_unfurnished():
    """If 'Unfurnished' is checked, set 'Semi-Furnished' to False."""
    if st.session_state["furnished_un"]:
        st.session_state["furnished_semi"] = False

# Checkboxes with callback functions
furnished_semi = st.checkbox("Semi-Furnished", key="furnished_semi", on_change=update_semi)
furnished_un = st.checkbox("Unfurnished", key="furnished_un", on_change=update_unfurnished)


# Prediction Button
if st.button("Predict Price"):

    # Prepare request data
    data = {
        "area": float(area),
        "latitude": float(latitude),
        "longitude": float(longitude),
        "Bedrooms": float(bedrooms),
        "Bathrooms": float(bathrooms),
        "neworold": neworold,
        "type_of_building": type_of_building,
        "Furnished_status_Semi-Furnished": furnished_semi,
        "Furnished_status_Unfurnished": furnished_un
    }

    df = pd.DataFrame(data, index=[0])
    prediction = np.expm1(model.predict(df))
    # st.success(f"🏠 Estimated House Price: ₹{int(prediction[0]):,}")

    formatted_price = format_decimal(prediction[0], locale='en_IN')
    st.success(f"🏠 Estimated House Price: ₹{formatted_price}")