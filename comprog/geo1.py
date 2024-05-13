import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_coding = load_lottieurl("https://lottie.host/f09766aa-772d-4758-9c7d-dee3bd371bd6/OxsMj6Rro4.json")

def assess_soil_strength():
    st.title("Soil Strength and Stability Assessment")

    st.sidebar.header("Input Parameters")
    compaction = st.sidebar.slider("Compaction (%)", 0, 100, 50)
    moisture_content = st.sidebar.slider("Moisture Content (%)", 0, 100, 50)
    bearing_capacity = st.sidebar.slider("Bearing Capacity (kN/m^2)", 0, 100, 50)
    shear_strength = st.sidebar.slider("Shear Strength (kN/m^2)", 0, 100, 50)

    moisture_content_level = 0  # Initialize moisture_content_level

    if 10 <= moisture_content <= 18:
        moisture_content_level += 100
    elif 19 <= moisture_content <= 42:
        moisture_content_level += 75
    elif 43 <= moisture_content <= 75:
        moisture_content_level += 50
    elif 75 <= moisture_content <= 90:
        moisture_content_level += 25
    elif moisture_content <= 9 or moisture_content >= 91:
        moisture_content_level += 0

    # Perform analysis based on input parameters
    soil_stability = (compaction + moisture_content_level + bearing_capacity + shear_strength) / 4

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("## Results")
            st.write(f"Estimated Soil Stability: {soil_stability}/100")
 
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

def main():
    st.sidebar.title("Soil Strength and Stability Assessment")
    page = st.sidebar.radio("Select Tool", ("Assess Soil Strength",))

    if page == "Assess Soil Strength":
        assess_soil_strength()

if __name__ == "__main__":
    main()