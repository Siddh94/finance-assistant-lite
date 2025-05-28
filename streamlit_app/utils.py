# streamlit_app/utils.py

import requests

def send_text_query(symbols, query):
    response = requests.post("http://localhost:8000/briefing/", json={
        "symbols": symbols,
        "query": query
    })
    return response.json()

def send_voice_query(audio_path):
    with open(audio_path, "rb") as f:
        files = {"file": f}
        response = requests.post("http://localhost:8000/voice/", files=files)
    return response.json()
