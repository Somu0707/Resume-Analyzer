# AWS Resume Analyzer 📄☁️

## Project Description

AWS Resume Analyzer is a full-stack web application designed to simplify the process of extracting and organizing information from resume documents. The application allows users to upload resumes in PDF format and automatically extracts important details such as candidate information, technical skills, education, work experience, and project details.

The system uses **pdfplumber**, a Python-based PDF processing library, to extract text from resume documents efficiently. The extracted content is processed and displayed in a structured and user-friendly format, reducing the manual effort required to review resumes.

The project utilizes **AWS cloud services** to provide reliable and scalable cloud infrastructure for storing and managing resume-related data. By combining cloud computing with PDF processing techniques, the application provides an efficient solution for resume document analysis and management.

The application follows a full-stack architecture with a **React.js frontend** for creating an interactive user interface and a **Python backend** for handling PDF processing and API operations.

---

# ✨ Features

- 📄 Upload resumes in PDF format
- 🔍 Extract text from PDF files using pdfplumber
- 📝 Process and organize resume information
- 👤 Extract candidate details
- 💻 Identify technical skills
- 🎓 Extract education details
- 💼 Extract work experience information
- 🚀 Extract project details
- ☁️ AWS cloud integration
- 📊 Display extracted resume data in a structured format
- ⚡ Fast and efficient document processing

---

# 🛠️ Technologies Used

## Frontend
- React.js
- Vite
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask / FastAPI

## PDF Processing
- pdfplumber

## Cloud Services
- Amazon Web Services (AWS)

## Development Tools
- Git & GitHub
- VS Code
- Postman

---

# 🏗️ System Architecture

```
User
 |
 | Upload Resume PDF
 |
React.js Frontend
 |
Python Backend API
 |
pdfplumber PDF Processing
 |
AWS Cloud Services
 |
Extracted Resume Information
 |
Display Results
```

---

# 📂 Project Structure

```
AWS-Resume-Analyzer
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── backend
│   ├── app.py
│   ├── pdf_processor.py
│   ├── requirements.txt
│   └── routes
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation and Setup

## Clone the Repository

```bash
git clone https://github.com/your-username/AWS-Resume-Analyzer.git
```

Navigate to the project directory:

```bash
cd AWS-Resume-Analyzer
```

---

# Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the frontend application:

```bash
npm run dev
```

---

# Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run the backend server:

```bash
python app.py
```

---

# 📦 Dependencies

Main Python libraries used:

```
pdfplumber
flask
flask-cors
boto3
```

---

# ☁️ AWS Integration

AWS services are used to provide cloud-based support for the application.

AWS implementation includes:

- Secure storage and management of resume documents
- Cloud-based application support
- Scalable infrastructure for handling resume processing
- Reliable access to application resources

---
# 🔮 Future Enhancements

- Resume comparison with job descriptions
- Resume scoring system
- User authentication
- Database integration for storing resumes
- Improved resume information extraction
- Resume report generation
- Enhanced cloud deployment

---

# 👩‍💻 Author

**P. Sravya**

Computer Science Engineering Student

---

# 📜 License

This project is developed for educational and learning purposes.
