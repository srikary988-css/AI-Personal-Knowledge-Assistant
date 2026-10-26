# 🧠 AI Personal Knowledge & Decision Assistant

An AI-powered knowledge workspace that helps users turn scattered documents and web resources into clear answers, evidence-based insights, and practical decision briefs.

## 🚀 Problem Statement

People collect notes, documents, links, and project materials across different places. Finding useful information and turning it into a clear decision can be time-consuming.

This project provides a single AI workspace where users can:

- 📄 Upload personal or project documents
- 🌐 Add website sources
- 🔎 Search across collected knowledge
- 🤖 Ask questions using AI
- 📚 View supporting evidence
- 🎯 Generate practical decision briefs

## 💡 Solution

The system combines document processing, retrieval-based search, and Gemini AI to create an evidence-based knowledge assistant.

The workflow is:

```text
User
  ↓
Streamlit Interface
  ↓
Document / Website Processing
  ↓
Knowledge Base
  ↓
TF-IDF Retrieval (RAG)
  ↓
Relevant Evidence
  ↓
Gemini AI
  ↓
Answer / Decision Brief
```

## ✨ Key Features

### 📚 Multi-Source Knowledge

Supports:

- PDF
- DOCX
- TXT
- Websites / URLs

### 🔎 Knowledge Retrieval

The system divides information into smaller chunks and uses TF-IDF similarity to retrieve the most relevant information for a user's question.

### 🤖 AI Question Answering

Users can ask questions about their collected knowledge and receive answers generated using the retrieved evidence.

### 🎯 Decision Assistant

Users can enter a decision they need to make and generate a structured decision brief containing:

- Decision
- Key Findings
- Options
- Comparison
- Advantages & Disadvantages
- Evidence
- Recommendation
- Risks & Considerations

### 📚 Evidence-Based Responses

The application displays the sources used to generate answers and decision briefs.

For PDF documents, relevant page numbers can also be displayed.

### 🧹 Session Control

Users can clear the current knowledge base and start a fresh session using the **Clear Knowledge** button.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Streamlit | Web application interface |
| Gemini AI | Natural language generation |
| Scikit-learn | TF-IDF retrieval and similarity |
| PyPDF | PDF processing |
| python-docx | DOCX processing |
| BeautifulSoup | Website text extraction |
| Requests | Web requests |

## 📂 Project Structure

```text
AI-Personal-Knowledge-Assistant/
│
├── app.py
├── backend.py
├── document_processor.py
├── rag.py
├── test_gemini.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

### File Description

**app.py**  
Main Streamlit application and user interface.

**backend.py**  
Handles Gemini AI requests, question answering, and decision brief generation.

**document_processor.py**  
Extracts text from PDF, DOCX, TXT files, and websites.

**rag.py**  
Handles document chunking, TF-IDF vectorization, similarity search, and evidence retrieval.

**test_gemini.py**  
Tests the Gemini API connection.

**requirements.txt**  
Contains the Python dependencies required by the project.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Personal-Knowledge-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

⚠️ Never upload your `.env` file or expose your API key publicly.

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🧪 Example Workflow

1. Upload one or more documents.
2. Add a relevant website if required.
3. Review the Knowledge Sources.
4. Open **Ask Your Knowledge**.
5. Ask a question.
6. Review the AI-generated answer and evidence.
7. Open **Decision Assistant**.
8. Enter a decision.
9. Generate the Decision Brief.
10. Review the recommendation and supporting evidence.

## 🔐 Security

The Gemini API key is stored in an environment variable and excluded from Git using `.gitignore`.

The `.env` file should never be committed to the repository.

## 🔮 Future Improvements

- Semantic embeddings for improved retrieval
- Persistent vector database
- Conversation history
- More advanced source citations
- Support for additional file formats
- Improved website extraction
- User authentication
- Export decision briefs as PDF
- Cloud deployment
- Personalized knowledge spaces

## 🎯 Hackathon Goal

The project demonstrates how AI can transform scattered information into:

**Knowledge → Evidence → Insight → Decision**

## 👩‍💻 Project

Built as an AI-powered personal knowledge and decision-support workspace for hackathon development.