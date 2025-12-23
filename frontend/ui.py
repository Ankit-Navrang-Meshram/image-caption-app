import streamlit as st
import requests
from PIL import Image

# The URL where FastAPI is running (inside Docker, we use the service name)
# If running locally without Docker, use "http://127.0.0.1:8000/predict"
API_URL = "http://backend:8000/predict"

st.title("🖼️ AI Image Captioning Tool")
st.write("Upload an image and the AI will describe it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Analyzing image..."):
            try:
                # Send the file to the FastAPI backend
                files = {"file": uploaded_file.getvalue()}
                response = requests.post(API_URL, files=files)
                
                # Parse the response
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"**Caption:** {data['caption']}")
                else:
                    st.error("Error connecting to the backend.")
            except Exception as e:
                st.error(f"Connection failed. Is the backend running? {e}")