from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .gemini_service import create_learning_response

app = FastAPI(title="EduGenie: Google Gemini Powered Learning Assistant")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.post("/learn", response_class=HTMLResponse)
def learn(request: Request, topic: str = Form(...), level: str = Form(...),
          mode: str = Form(...), question: str = Form(...)):
    response = create_learning_response(topic, level, mode, question)
    return templates.TemplateResponse(
        request=request, name="result.html",
        context={"topic": topic, "level": level, "mode": mode,
                 "question": question, "response": response}
    )

@app.get("/health")
def health():
    return {"status": "ok", "project": "EduGenie Google Gemini Powered Learning Assistant"}
