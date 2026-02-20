# Translation API - Simple Version

Fast, simple translation API using Hugging Face models.

## Setup

```bash
# Install
pip install -r simple_requirements.txt

# Run
python simple_app.py

# Or with uvicorn
uvicorn simple_app:app --reload
```

Visit: http://localhost:8000/docs

## APIs

### 1. Health Check
```
GET /
```
Response: `{"status": "ok"}`

### 2. Translate
```
POST /translate
```
Body:
```json
{
  "text": "Hello world",
  "lang": "es"
}
```
Response:
```json
{
  "text": "Hello world",
  "translated": "Hola mundo",
  "lang": "es"
}
```

### 3. Get Languages
```
GET /languages
```
Response:
```json
{
  "es": "Spanish",
  "fr": "French",
  ...
}
```

## Languages

- es (Spanish)
- fr (French)
- de (German)
- it (Italian)
- pt (Portuguese)
- ru (Russian)
- ja (Japanese)
- ko (Korean)
- zh (Chinese)
- ar (Arabic)
- hi (Hindi)
- nl (Dutch)
- pl (Polish)
- tr (Turkish)
- vi (Vietnamese)
- th (Thai)

## Testing

```bash
python simple_test.py
```

## Salesforce Integration

```apex
// Apex code
Http http = new Http();
HttpRequest req = new HttpRequest();
req.setEndpoint('https://your-api-url/translate');
req.setMethod('POST');
req.setHeader('Content-Type', 'application/json');
req.setBody(JSON.serialize(new Map<String, String>{
    'text' => 'Hello',
    'lang' => 'es'
}));
HttpResponse res = http.send(req);
String translated = (String)JSON.deserializeUntyped(res.getBody()).get('translated');
System.debug(translated); // Output: Hola
```

## Deploy

### Hugging Face Spaces (Fastest)
1. Create Space: https://huggingface.co/spaces
2. Use Dockerfile
3. Push code
4. Done! 🎉

### Railway
1. Create account: https://railway.app
2. Connect GitHub
3. Deploy
4. Get URL

### Google Cloud Run
```bash
gcloud run deploy translation-api \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Cost
- **Free tier:** Hugging Face Spaces (FREE GPU!)
- **Production:** $0-20/month (all platforms)
- **First request:** 30-60s (model download, then cached)
- **Subsequent:** <1 second

## That's it!
3 files: app, test, requirements
3 APIs: health, translate, languages

Simple. Fast. Free. 🚀
