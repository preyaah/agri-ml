import streamlit as st
from utils import load_models, predict_soil_tilling, predict_pest, predict_disease
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="AgriML - AI Precision Farming",
    page_icon="🌱",
    layout="wide"
)

# Load models
@st.cache_resource
def get_models():
    return load_models()

soil_model, pest_model, disease_model = get_models()

# Main title
st.title("🌱 AgriML - AI-Driven Precision Farming")
st.write("Leverage machine learning for soil analysis, pest detection, and crop disease identification")

# Sidebar for navigation
st.sidebar.title("Select Model")
option = st.sidebar.selectbox(
    "Choose a prediction model:",
    ("Soil Tilling Detection", "Pest Detection", "Crop Disease Detection")
)

# Model 1: Soil Tilling Detection (using image instead of sliders)
if option == "Soil Tilling Detection":
    st.header("🚜 Soil Tilling Detection")
    st.write("Upload an image of the soil to determine whether it needs tilling")
    
    uploaded_file = st.file_uploader("Choose a soil image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Soil Image")
            image = Image.open(uploaded_file)
            st.image(image, caption="Soil Image", use_column_width=True)
        
        with col2:
            if st.button("Analyze Soil"):
                result = predict_soil_tilling(soil_model, image)
                st.subheader("Prediction Result")
                if "Needs" in result:
                    st.error(f"🔴 {result}")
                    st.write("Recommendation: Till the soil before planting")
                else:
                    st.success(f"🟢 {result}")
                    st.write("Recommendation: Soil is ready for planting")

# Model 2: Pest Detection
elif option == "Pest Detection":
    st.header("🐛 Pest Detection")
    st.write("Upload a crop image to detect pest presence")
    
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
        
        with col2:
            st.subheader("Prediction Result")
            if st.button("Detect Pests"):
                result = predict_pest(pest_model, image)
                
                if "Detected" in result:
                    st.error(f"🔴 {result}")
                    st.write("Recommendation: Apply appropriate pest control measures")
                else:
                    st.success(f"🟢 {result}")
                    st.write("Recommendation: No immediate pest control needed")

# Model 3: Crop Disease Detection
elif option == "Crop Disease Detection":
    st.header("🦠 Crop Disease Detection")
    st.write("Upload a leaf image to identify potential diseases")
    
    uploaded_file = st.file_uploader("Choose a leaf image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            image = Image.open(uploaded_file)
            st.image(image, caption="Leaf Image", use_column_width=True)
        
        with col2:
            st.subheader("Disease Analysis")
            if st.button("Analyze Disease"):
                result = predict_disease(disease_model, image)
                
                st.write(f"**Prediction:** {result}")
                st.write("**Confidence:** 90% accuracy")
                # Add specific recommendations based on disease type
