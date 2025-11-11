import requests
from django.conf import settings

OLLAMA_API_URL = getattr(settings, "OLLAMA_API_URL", "http://localhost:11434")

def ask_ollama(prompt: str, model: str = "llama3", temperature: float = 0.7):
    payload = {
        "model": model,
        "prompt": prompt,
        "options": {
            "temperature": temperature
        },
        "stream": False
    }
    resp = requests.post(
        f"{OLLAMA_API_URL}/api/generate",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("response", "")
