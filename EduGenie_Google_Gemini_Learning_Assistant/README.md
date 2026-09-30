# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a FastAPI-based learning assistant for explanations, study notes, quizzes, and step-by-step learning.

## Features
- Topic-based learning
- Beginner, Intermediate, and Advanced levels
- Explanation, Study Notes, Quiz, and Step-by-Step modes
- FastAPI backend and Jinja2 frontend
- Responsive CSS
- Health-check endpoint
- Runs locally without an API key

## Run
```bash
python -m venv venv
```
Windows:
```powershell
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

## Gemini Integration
The project is runnable without an API key. The learning service is isolated in `app/gemini_service.py`, where a real Gemini API integration can be added later. Never commit a real API key to GitHub.

## Educational Note
Verify important information with textbooks, course materials, teachers, or other trusted academic sources.
