---
title: English to Multi-Language Translator
emoji: 🌍
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# English to Multi-Language Translator

A free, production-ready translation API powered by Hugging Face Transformers (MarianMT models). Translate English text to 16+ languages with zero cost.

**Created by:** Mohit Peshwani | Certified Salesforce Developer | Python & Data Analytics Professional

## Quick Start

### Local Testing
```bash
# Install dependencies
pip install -r simple_requirements.txt

# Run the server
uvicorn simple_app:app --host 0.0.0.0 --port 7860

# In another terminal, test it
curl -X POST http://localhost:7860/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "lang": "es"}'
```

## API Endpoints

### 1. Health Check
```bash
GET /
```
Response: `{"status": "ok"}`

### 2. Get Supported Languages
```bash
GET /languages
```
Response:
```json
{
  "en->es": "Spanish",
  "en->fr": "French",
  "en->de": "German",
  "en->it": "Italian",
  "en->pt": "Portuguese",
  "en->ru": "Russian",
  "en->ja": "Japanese",
  "en->ko": "Korean",
  "en->zh": "Chinese",
  "en->ar": "Arabic",
  "en->hi": "Hindi",
  "en->nl": "Dutch",
  "en->pl": "Polish",
  "en->tr": "Turkish",
  "en->vi": "Vietnamese",
  "en->th": "Thai"
}
```

### 3. Translate Text
```bash
POST /translate
Content-Type: application/json

{
  "text": "Hello, how are you?",
  "lang": "es"
}
```

Response:
```json
{
  "text": "Hello, how are you?",
  "translated": "Hola, ¿cómo estás?",
  "lang": "es"
}
```

## Supported Languages
- **Spanish** (es)
- **French** (fr)
- **German** (de)
- **Italian** (it)
- **Portuguese** (pt)
- **Russian** (ru)
- **Japanese** (ja)
- **Korean** (ko)
- **Chinese** (zh)
- **Arabic** (ar)
- **Hindi** (hi)
- **Dutch** (nl)
- **Polish** (pl)
- **Turkish** (tr)
- **Vietnamese** (vi)
- **Thai** (th)

## Salesforce Integration Example

Use in Salesforce with this Apex code:

```apex
public class TranslationService {
    public static String translate(String text, String language) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('https://your-space-url/translate');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        
        String body = '{"text":"' + text + '","lang":"' + language + '"}';
        req.setBody(body);
        
        HttpResponse res = new Http().send(req);
        Map<String, Object> response = (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
        
        return (String) response.get('translated');
    }
}
```

## Cost Analysis
- **API Cost**: $0 (Free)
- **Hosting Cost**: $0 (Hugging Face Spaces free tier includes GPU)
- **Model Cost**: $0 (Open-source MarianMT models)
- **Data Cost**: $0 (No external API calls)

**Total Cost of Ownership: $0 / month**

## Deployment

This Space uses Docker and auto-deploys from the GitHub repository. Every push to main triggers automatic redeploy.

## Files
- `simple_app.py` - FastAPI application with translation logic
- `simple_requirements.txt` - Python dependencies (4 packages)
- `Dockerfile` - Container definition for Hugging Face Spaces
- `README.md` - This documentation

## Performance
- **Latency**: ~500ms per translation (first request loads model, subsequent requests <100ms due to caching)
- **Throughput**: Single instance handles ~10 concurrent requests
- **Memory**: ~2GB for all 16 language models cached
- **Model Size**: ~1.5GB total (all MarianMT models)

## Technology Stack
- **Framework**: FastAPI (modern async Python)
- **ML Library**: Hugging Face Transformers
- **Models**: Helsinki-NLP MarianMT neural translation
- **Inference**: PyTorch CPU
- **Server**: Uvicorn ASGI
- **Validation**: Pydantic type safety

## Error Handling
- Unsupported language → HTTP 400 with message
- Empty text → HTTP 400 with message
- Server error → HTTP 500 with details

## Support
For issues or questions, check the [GitHub repository](https://github.com/yourusername/PythonTranslation).

---

**Built with ❤️ using free, open-source technology**
