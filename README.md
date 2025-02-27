## DocInsight: Document Summarization and Interaction Tool

**DocInsight** is an NLP-driven web application designed to save user's time in analyzing and comprehending complex documents. It offers document summarization, interactive chatbot for queries, voice commands, and customizable options to make document analysis more efficient.

---

### Features

1. Document Summarization - Summarize documents using GeminiAPI

2. Interactive Chatbot - Ask queries about your documents

3. Voice Assistant - Listen to document summaries and navigate using voice commands

4. User Preferences - Adjust summary length, focusing on specific sections.

---

### Tech Stack

1. Frontend: Streamlit

2. Backend: FastAPI

3. Database: PostgreSQL

4. AI Models: GeminiAPI

5. OCR: OpenCV & Tesseract

---

### Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/docinsight.git
cd docinsight
```

2️⃣ Install Dependencies

Make sure you have Python 3.8+ installed. Then, run:

```bash
pip install -r requirements.txt
```

3️⃣ Run the Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

4️⃣ Run the Frontend (Streamlit)

```bash
streamlit run app.py
```

---

### Usage

1. Upload your document (PDF, DOCX, PPTX, XLSX).

2. Choose between summarization, chatbot interaction, or voice narration.

3. Customize your summary (short, medium, detailed).

4. Ask the AI chatbot about specific sections of your document.

5. Listen to audio summaries for hands-free interaction.

---

### PURPOSE

#### This project, DocInsight, is being developed as part of the curriculum for the MCA program at Christ University, Bangalore. It is designed to showcase practical applications of Natural Language Processing (NLP) and AI-driven document analysis. The project aims to enhance efficiency in document summarization, query-based interaction, and voice-based accessibility.
