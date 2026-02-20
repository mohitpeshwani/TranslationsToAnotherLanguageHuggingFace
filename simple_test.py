import requests

BASE = "http://localhost:8000"

# Health check
print("Health:", requests.get(f"{BASE}/").json())

# Get languages
print("Languages:", requests.get(f"{BASE}/languages").json())

# Translate
result = requests.post(f"{BASE}/translate", json={
    "text": "Hello world",
    "lang": "es"
})
print("Translation:", result.json())

# Batch translate
for lang in ["es", "fr", "de"]:
    result = requests.post(f"{BASE}/translate", json={
        "text": "Good morning",
        "lang": lang
    })
    print(f"{lang}: {result.json()['translated']}")
