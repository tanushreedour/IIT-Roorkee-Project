# 🎓 PARIMAL - OCR and Entity Search Application

### An advanced application that extracts text from images using OCR and allows entity search within the extracted text. The application is built with Azure AI Vision services and Google Gemini API for AI-powered entity search.

---

## ✨ Live URL of Project: 

You can check out the project at this link : **https://bilingual-extractor-ocr.streamlit.app/**

![image](https://github.com/user-attachments/assets/290fdf70-1d2d-4541-a634-379caaf7da39)

## ***Text Extraction:***

![image](https://github.com/user-attachments/assets/b4a244be-4a06-4e41-a250-7804c4fffe43)

## ***Entity Recognition:***

![image](https://github.com/user-attachments/assets/03ff31d2-821b-4c3d-a0a0-d985cdd734dc)


## 🚀 Features

- **Text Extraction**: Upload images in JPG, JPEG, or PNG formats and extract text from them using **Azure's OCR** capabilities.
- **Entity Search**: Once the text is extracted, search for any specific keyword or entity within the extracted text.
- **Intuitive UI**: The application features a modern, sleek design with easy navigation between text extraction and entity search functionalities.
- **AI-Powered Entity Search**: Leverages **Google Gemini API** to generate relevant content based on the entity search query.
- **Two-page Application**: Separate pages for Text Extraction and Entity Search for a smooth user experience.

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit for building a fast and interactive UI.
- **OCR Service**: Azure AI Vision's OCR API for accurate text extraction from images.
- **AI Search**: Google Gemini API for entity search within the extracted text.
- **Cloud Services**: Azure for image analysis.

---

## 📋 Prerequisites

Before running the application, ensure you have the following:

1. **Python 3.8+** installed.
2. Azure Account and API Key for Azure AI Vision services.
3. Google Cloud API Key for Google Gemini API.
4. Streamlit installed (`pip install streamlit`).

---

## 🔧 Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/IIT-Roorkee-Project.git
   ```
   
2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a .env file in the root directory and add the following environment variables:**

   ```bash
   AI_SERVICE_ENDPOINT=your_azure_vision_endpoint
   AI_SERVICE_KEY=your_azure_vision_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the application:**

   ```bash
   streamlit run main.py
   ```

## 🧑‍💻 Usage Guide

### 1. Text Extraction

- Navigate to the **Text Extraction** page via the sidebar.
- Upload an image (supported formats: `.jpg`, `.jpeg`, `.png`).
- The app automatically extracts and displays the text from the uploaded image.
- The extracted text is saved for use in the **Entity Search** page.

### 2. Entity Search

- Navigate to the Entity Search page via the sidebar.
- Enter a keyword to search within the extracted text.
- The app performs an AI-powered search using Google Gemini API to provide relevant information based on the keyword and extracted text.

---

## 📚 Project Structure

```bash
IIT-Roorkee-Project/
│
├── .env                      # Environment variables for API keys
├── main.py                    # Main application file
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── ...                        # Other project-related files
```

---

## ⚙️ Environment Variables

Add the following variables to the .env file for the API services:

```bash
AI_SERVICE_ENDPOINT=your_azure_vision_endpoint
AI_SERVICE_KEY=your_azure_vision_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## 📦 Dependencies

Key dependencies include:

- **Streamlit**: For the web interface.
- **Pillow**: For image processing.
- **Azure AI Vision**: For OCR services.
- **Google Generative AI:** For entity search functionality.

---

## 🤝 Contributing

- Fork the repository.
- Create a new branch for your feature (git checkout -b feature/feature-name).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/feature-name).
- Create a pull request.
