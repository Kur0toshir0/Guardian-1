import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Guardian AnGEOl", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/a06c0846-9fcd-4f20-89e4-8a734fa9732f/wfAmGtE1uH.json")
# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Guardian AnGEOl")
        st.write("##")
    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")


st.write("Guardian AnGEOl is a website that assesses the strength and stability of soil or land for various construction and hazard assessment purposes. Whether you are planning a new construction project, assessing the risk of landslides, or determining the suitability of land for development.")

# ---- CAPABILITIES ----
with st.container():
    st.write("---")
    st.markdown("<h3 style='text-align: center;'>What to do?</h3>", unsafe_allow_html=True)
    

# Adding columns
col1, col2, col3, = st.columns(3)

with col1: 
    st.markdown("""
    <div style='border: 1px solid #e6e6e6; border-radius: 5px; padding: 20px; text-align: center;'>
    <p>Assess soil strength and potential hazard</p>
    <p>Provide users with tools to assess the strength and stability of soil or land. By analyzing key soil properties such as compaction, moisture content, bearing capacity, and shear strength, the app helps users understand soil strength and identify areas vulnerable to geological hazards such as landslides and subsidence.</p>
    <img src='https://scontent.xx.fbcdn.net/v/t1.15752-9/440543744_417477914571406_1770367509985217455_n.png?stp=dst-png_s403x403&_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=V5QadTrGAo0Q7kNvgE4bzKo&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_Q7cD1QG6VVrY9Rg9SdpHsJ4zJ5A5LJlOL_fRfG27ktEA4ag_5A&oe=66681419' width='150px'>
    </div>
    """, unsafe_allow_html=True)
        
with col2:
    st.markdown("""
    <div style='border: 1px solid #e6e6e6; border-radius: 5px; padding: 20px; text-align: center;'>
    <p>Support construction planning</p>
    <p>Support construction planning by providing users with a comprehensive toolkit for evaluating properties for construction readiness.</p>
    <img src='https://scontent.xx.fbcdn.net/v/t1.15752-9/440543744_417477914571406_1770367509985217455_n.png?stp=dst-png_s403x403&_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=V5QadTrGAo0Q7kNvgE4bzKo&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_Q7cD1QG6VVrY9Rg9SdpHsJ4zJ5A5LJlOL_fRfG27ktEA4ag_5A&oe=66681419' width='150px'>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div style='border: 1px solid #e6e6e6; border-radius: 5px; padding: 20px; text-align: center;'>
    <p>Facilitate data visualization and reporting</p>
    <p>Facilitate data visualization and reporting to help users effectively communicate results, recommendations, and risk assessments using soil strength data, hazard maps, and construction readiness assessments.</p>
    <img src='https://scontent.xx.fbcdn.net/v/t1.15752-9/440543744_417477914571406_1770367509985217455_n.png?stp=dst-png_s403x403&_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=V5QadTrGAo0Q7kNvgE4bzKo&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_Q7cD1QG6VVrY9Rg9SdpHsJ4zJ5A5LJlOL_fRfG27ktEA4ag_5A&oe=66681419' width='150px'>
    </div>
    """, unsafe_allow_html=True)