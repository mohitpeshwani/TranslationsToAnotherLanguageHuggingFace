"""
FastAPI + Hugging Face Transformers
English → 18+ Languages (Target for Arabic but covered others as well)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer
import os

app = FastAPI(title="Translation API", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models cache
MODELS = {}

# Language models
LANGUAGES = {
    "es": "Helsinki-NLP/Opus-MT-en-es",
    "fr": "Helsinki-NLP/Opus-MT-en-fr",
    "de": "Helsinki-NLP/Opus-MT-en-de",
    "it": "Helsinki-NLP/Opus-MT-en-it",
    "pt": "Helsinki-NLP/Opus-MT-en-pt",
    "ru": "Helsinki-NLP/Opus-MT-en-ru",
    "ja": "Helsinki-NLP/Opus-MT-en-ja",
    "ko": "Helsinki-NLP/Opus-MT-en-ko",
    "zh": "Helsinki-NLP/Opus-MT-en-zh",
    "ar": "Helsinki-NLP/Opus-MT-en-ar",
    "hi": "Helsinki-NLP/Opus-MT-en-hi",
    "nl": "Helsinki-NLP/Opus-MT-en-nl",
    "pl": "Helsinki-NLP/Opus-MT-en-pl",
    "tr": "Helsinki-NLP/Opus-MT-en-tr",
    "vi": "Helsinki-NLP/Opus-MT-en-vi",
    "th": "Helsinki-NLP/Opus-MT-en-th",
}

def get_model(lang: str):
    """Load model once and cache it"""
    if lang not in MODELS:
        model_name = LANGUAGES[lang]
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        MODELS[lang] = (model, tokenizer)
    return MODELS[lang]

# Request/Response
class TranslateRequest(BaseModel):
    text: str
    lang: str = "es"

class TranslateResponse(BaseModel):
    text: str
    translated: str
    lang: str

# API Endpoints
@app.get("/")
def health():
    """Health check"""
    return {"status": "ok"}

@app.post("/translate", response_model=TranslateResponse)
def translate(req: TranslateRequest):
    """Translate text to language"""
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text is required")
    
    if req.lang not in LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Language not supported: {req.lang}")
    
    try:
        model, tokenizer = get_model(req.lang)
        inputs = tokenizer(req.text, return_tensors="pt")
        outputs = model.generate(**inputs)
        translated = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return {
            "text": req.text,
            "translated": translated,
            "lang": req.lang
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/languages")
def get_languages():
    """Get supported languages"""
    return {
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "ja": "Japanese",
        "ko": "Korean",
        "zh": "Chinese",
        "ar": "Arabic",
        "hi": "Hindi",
        "nl": "Dutch",
        "pl": "Polish",
        "tr": "Turkish",
        "vi": "Vietnamese",
        "th": "Thai",
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
