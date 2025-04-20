## DocInsight: Document Summarization and Interaction Tool

**DocInsight** is an NLP-driven web application designed to save user's time in analyzing and comprehending complex documents. It offers document summarization, interactive chatbot for queries, voice commands, and customizable options to make document analysis more efficient.

---

### Features -

1. Document Summarization - Summarize documents using GeminiAPI

2. Interactive Chatbot - Ask queries about your documents

3. Voice Assistant - Listen to document summaries and navigate using voice commands

4. User Preferences - Adjust summary length, focusing on specific sections.

---

### Tech Stack -

1. Frontend: Streamlit for UI

2. Backend: FastAPI(microservice architecture)

3. Database: PostgreSQL

4. NLP & AI Models: NLTK, GeminiAPI

5. OCR: Tesseract OCR for Image text extraction

---

### Installation & Setup -

1. Clone the Repository
```bash
git clone https://github.com/yourusername/docinsight.git
cd docinsight
```

2. Install Dependencies

Make sure you have Python 3.8+ installed. Then, run:

```bash
pip install -r requirements.txt
```

3. Create GEMINI_API_KEY from google AI studio. Create a .env file in the backend, and paste your GEMINI_API_KEY in it.

4. Run the Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

5. Run the Frontend (Streamlit)

```bash
streamlit run app.py
```

---

### How to USE -

1. Upload your document (PDF, DOCX, PPTX, XLSX).

2. Choose between summarization, chatbot interaction, or voice narration.

3. Customize your summary (short, medium, detailed).

4. Ask the AI chatbot about specific sections of your document.

5. Listen to audio summaries for hands-free interaction.

---

## Authors & Contributors

Developed by: Sagar – Creator & Lead Developer

#### Contributors:
We welcome contributions! If you'd like to improve DocInsight, feel free to fork the repo and submit a pull request.
