# AgriML

## Overview
AgriML is an AI-driven precision farming project leveraging machine learning models focused on agricultural challenges. The project aims to assist farmers by analyzing soil, detecting pests, and identifying crop diseases to enhance crop management and increase yield through data-driven decisions.

## Models and Features
AgriML includes three core machine learning models:

1. **Soil Tilling Detection**  
   Determines if soil needs tilling by analyzing soil images.
2. **Pest Detection**  
   Detects pests in crops using image-based analysis.
3. **Crop Disease Detection**  
   Identifies diseases in crops from leaf images to help timely treatment.

All models achieve an accuracy of approximately **90%**, providing reliable predictions to support farming practices.

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Common Python ML libraries such as numpy, pandas, scikit-learn, TensorFlow or PyTorch (depending on model implementations)
- OpenCV for image processing (for pest and disease detection)
- Streamlit (for web app interface)

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/preyaah/agri-ml.git
   ```
2. Navigate to the project directory:
   ```
   cd agri-ml
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage
- Use the web app to upload soil images to determine tilling needs.
- Upload crop images for pest detection.
- Upload leaf images to identify crop diseases.
- The app shows interactive predictions with recommendations.

