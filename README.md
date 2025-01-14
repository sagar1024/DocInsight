# DocInsight: AI-Powered Document Summarization and Interaction Tool

**DocInsight** is an AI-driven web application designed to revolutionize how users analyze and comprehend complex documents. It offers features such as document summarization, interactive chatbot queries, voice-based interactions, and customization options to make document analysis more accessible and efficient.

---

## Features

1. **Document Summarization**  
   Summarize PDFs, Word documents, Excel files, and PowerPoint presentations with AI-driven accuracy.

2. **Interactive Chatbot**  
   Ask queries about your documents using a conversational chatbot powered by the Gemini API.

3. **Voice Assistant**  
   Listen to document summaries and navigate the application using voice commands.

4. **Customizations**  
   Tailor summaries by adjusting their length, focusing on specific sections, or generating content in different languages.

5. **User Management**  
   - Visitors: Use the application without storing preferences or history.  
   - Registered Users: Log in to save chat history and preferences for a personalized experience.

6. **Seamless Integration**  
   Upload files directly or connect with Google Drive, Dropbox, and OneDrive for easy document management.

---

## Tech Stack

### **Frontend**
- **Framework:** [Streamlit](https://streamlit.io/)  
- **Features:**  
  - Responsive design for seamless interaction.  
  - Integration with backend services for summarization, chatbot, and voice assistant functionalities.  

### **Backend**
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Features:**  
  - API for handling document processing and user authentication.  
  - Scalable architecture for integration with AI models.  

### **Database**
- PostgreSQL (for user management and history storage).

---

## Project Structure

```plaintext
docinsight/
│
├── backend/                  # Backend codebase
│   ├── main.py               # Entry point for FastAPI
│   ├── routers/              # API endpoints
│   ├── services/             # Core logic (summarization, chatbot, etc.)
│   ├── schemas/              # Pydantic models
│   ├── utils/                # Authentication and helper utilities
│   ├── database.py           # Database connection
│   └── models.py             # ORM models
│
├── frontend/                 # Frontend codebase
│   ├── app.py                # Streamlit entry point
│   ├── pages/                # Individual pages (e.g., home, summarization)
│   ├── components/           # Reusable UI components (e.g., navbar, forms)
│   ├── helpers/              # Helper functions
│   ├── api_client.py         # Communicates with backend APIs
│   ├── config.toml           # Configuration settings
│   └── requirements.txt      # Python dependencies
│
└── README.md                 # Project documentation
