import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize Azure and Gemini API details
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Authenticate Azure AI Vision client
cv_client = ImageAnalysisClient(
    endpoint=ai_endpoint,
    credential=AzureKeyCredential(ai_key)
)

# Configure Generative AI API
genai.configure(api_key=gemini_api_key)

# Function to extract text using Azure's OCR service
def GetTextRead(image_data):
    st.info("Extracting text...")

    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ]
    )

    extracted_text_list = []
    for block in result.read.blocks:
        for line in block.lines:
            st.markdown(f"**{line.text}**")
            extracted_text_list.append(line.text)

    return " ".join(extracted_text_list)

# ---- Page 1: Text Extraction ----
def text_extraction_page():
    st.title("Text Extraction")

    st.markdown("#### Upload an Image:")
    image = st.file_uploader("Upload image file (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if image is not None:
        img = Image.open(image)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Automatically trigger text extraction after image upload
        if image is not None:
            st.subheader("Extracted Text:")
            image_bytes = image.getvalue()
            extracted_text = GetTextRead(image_bytes)

            # Save extracted text to session state for use in the entity search page
            st.session_state['extracted_text'] = extracted_text
            st.success("Text extracted and saved successfully!")

# ---- Page 2: Entity Search ----
def entity_search_page():
    st.title("Entity Search")

    # Check if text has been extracted
    if 'extracted_text' in st.session_state:
        extracted_text = st.session_state['extracted_text']

        # Display the extracted text
        st.subheader("😶‍🌫️ Extracted Text:")
        st.write(extracted_text)

        # Entity search input
        st.write("")
        st.write("--------------------------------------------------------------------------------------")
        keyword = st.text_input("Enter keyword to search in the extracted text:")
        if st.button("Search Entity"):
            if keyword:
                st.markdown(f"Searching for **'{keyword}'** in the extracted text...")
                summary_template = f"""Given the entity "{keyword}", search for that entity in "{extracted_text}" and return the value of that entity with its unit."""
                
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(summary_template)

                st.subheader("Generated Response:")
                st.write(response.text)
            else:
                st.error("Please provide a keyword to search for.")
    else:
        st.warning("Please extract text from an image first on the 'Text Extraction' page.")

# ---- Main Navigation ----
def main():
    st.set_page_config(page_title="PARIMAL", layout="wide", page_icon="🎓")
    # Create a sidebar with a service selector
    st.sidebar.title("🌟 Service Options")
    st.sidebar.markdown("Select a service to begin:")

    # Main header and instructions
    st.title("🎓 PARIMAL - IIT Roorkee Project")
    st.markdown("#### A powerful OCR tool for **bilingual text extraction** and **entity search**")

    # User prompt with an instruction
    st.markdown("---")
    st.markdown("##### **How to Use:**\n1. Select the service you want from the sidebar.\n2. Upload your image and run the OCR or entity search.")
    st.markdown("---")

    # Navigation between pages
    pages = ["🔍 Text Extraction", "🔍 Entity Search"]
    selected_page = st.sidebar.selectbox("Choose a page:", pages)
    
    if selected_page == "🔍 Text Extraction":
        text_extraction_page()
    elif selected_page == "🔍 Entity Search":
        entity_search_page()

# Run the app
if __name__ == "__main__":
    main()
