import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Assets
lottie_coding = load_lottieurl("https://lottie.host/7064520d-a1f4-45ce-8c28-073dc3015814/9okX5gqzJO.json")
def evaluate_site_sustainability(topography, drainage, soil_type, environmental_considerations):
    sustainability_score = 0

    # Evaluate topography
    if topography == "Flat":
        sustainability_score += 25
    elif topography == "Mountainous":
        sustainability_score += 10
    elif topography == "Hilly":
        sustainability_score += 20
    elif topography == "Coastal":
        sustainability_score += 15
    elif topography == "Wetland":
        sustainability_score += 20
    elif topography == "Hilly":
        sustainability_score += 20
    

    # Evaluate drainage
    if drainage == "Good":
        sustainability_score += 25
    elif drainage == "Moderate":
        sustainability_score += 20
    elif drainage == "Poor":
        sustainability_score += 10

    # Evaluate soil type
    if soil_type == "Loam":
        sustainability_score += 25
    elif soil_type == "Sand":
        sustainability_score += 15
    elif soil_type in ["Silt", "Clay"]:
        sustainability_score += 10

    # Evaluate environmental considerations
    if "Flood Risk" in environmental_considerations:
        sustainability_score -= 10
    if "Erosion Risk" in environmental_considerations:
        sustainability_score -= 10
    if "Ecological Impact" in environmental_considerations:
        sustainability_score -= 10
    if "None" in environmental_considerations:
        sustainability_score += 25

    return sustainability_score

def perform_analysis(topography, drainage, soil_type, environmental_considerations):
    analysis_result = ""

    # Analyze topography
    if topography == "Flat":
        analysis_result += "The site has a flat topography, which facilitates construction and reduces excavation costs.\n"
    elif topography == "Mountainous":
        analysis_result += "The site has a towering peaks and rugged landscapes, presenting one of the most formidable challenges for property development. Constructing on mountainous terrain can be increadibly ardous and costly due to steep slopes.\n"
    elif topography == "Hilly":
        analysis_result += "The site has a hilly topography, which may pose challenges for construction and site development. Constructing on hilly land can be costly due to the need for extensive grading or earthmoving.\n"
    elif topography == "Coastal":
        analysis_result += "The site has both the combination of land and water including beaches, cliffs, and wetlands. This type of terrain both poses both challenges for property development for they are subject to environmental regulations and potential hazards such as erosion, storm surges, and rising levels. \n"
    elif topography == "Wetland":
        analysis_result += "The site is characterized by low-lying areas where water tables are high or standing water is present. This type of topography can present challenges for property evelopment due to the risk of flooding and the diffuculty of construction buildings on unstable soil. \n"
    elif topography == "Urban":
        analysis_result += "The site is defined by hunan-made structures, roads, and utilities that are constructed on natural landscapes. Property development in urban environments presents unique challenges and prospects, such as limited space and potential for redevelopment or revitalization projects. \n"
    # Analyze drainage
    if drainage == "Good":
        analysis_result += "The site has good drainage conditions, reducing the risk of water accumulation and flooding.\n"
    elif drainage == "Moderate":
        analysis_result += "The site has moderate drainage conditions, which may require some management measures to prevent water-related issues.\n"
    elif drainage == "Poor":
        analysis_result += "The site has poor drainage conditions, increasing the risk of water accumulation and flooding.\n"

    # Analyze soil type
    if soil_type == "Sand":
        analysis_result += "The site has sandy soil, which offers good drainage but may have lower stability for construction.\n"
    elif soil_type == "Loam":
        analysis_result += "The site has loamy soil, which provides good balance between drainage and stability for construction.\n"
    elif soil_type == "Silt":
        analysis_result += "The site has silty soil, which may have moderate drainage and stability characteristics.\n"
    elif soil_type == "Clay":
        analysis_result += "The site has clayey soil, which may have good stability but may be prone to poor drainage.\n"

    # Analyze environmental considerations
    if "Flood Risk" in environmental_considerations:
        analysis_result += "The site is located in an area with flood risk, requiring additional measures to mitigate flooding.\n"
    if "Erosion Risk" in environmental_considerations:
        analysis_result += "The site is located in an area with erosion risk, requiring erosion control measures to protect the site.\n"
    if "Ecological Impact" in environmental_considerations:
        analysis_result += "The site has ecological considerations that need to be addressed during construction to minimize impact on the environment.\n"
    if "None" in environmental_considerations:
        analysis_result += "The site is optimal for costrction since few to no risk is needed to be adressed during construction. \n"

    return analysis_result

def main():

    st.title("Site Sustainability Evaluation")
    st.sidebar.header("Input Parameters")
    topography = st.sidebar.selectbox("Topography", ("Flat", "Hilly", "Mountainous", "Coastal", "Wetland", "Urban"))
    drainage = st.sidebar.selectbox("Drainage", ("Good", "Moderate", "Poor"))
    soil_type = st.sidebar.selectbox("Soil Type", ("Sand", "Silt", "Clay", "Loam"))
    environmental_considerations = st.sidebar.multiselect("Environmental Considerations", ("Flood Risk", "Erosion Risk", "Ecological Impact", "None"))


    sustainability_score = evaluate_site_sustainability(topography, drainage, soil_type, environmental_considerations)
    analysis_result = perform_analysis(topography, drainage, soil_type, environmental_considerations)

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("## Results")
            st.write(f"Site sustainability score: {sustainability_score}")
        with right_column:
            st_lottie(lottie_coding, height=200, key="coding")
    
    with st.container():
        st.write("---")
        st.write("## Analysis")
        st.write(analysis_result)
    
if __name__ == "__main__":
    main()