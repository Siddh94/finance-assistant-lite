from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from orchestrator.routing import run_pipeline
from agents.voice_agent import transcribe_audio, synthesize_audio
import shutil

app = FastAPI()

# Request model for POST /briefing
class BriefingRequest(BaseModel):
    symbols: list[str]
    query: str

@app.post("/briefing/")
async def market_brief(payload: BriefingRequest):
    try:
        result = run_pipeline(payload.symbols, payload.query)
        return {"summary": result}
    except Exception as e:
        return {"error": str(e)}

@app.post("/voice/")
async def voice_brief(file: UploadFile = File(...)):
    try:
        with open("input.wav", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        query = transcribe_audio("input.wav")
        result = run_pipeline(["TSM", "005930.KQ"], query)
        synthesize_audio(result, "output.wav")

        return {
            "query": query,
            "summary": result,
            "audio_file": "output.wav"
        }
    except Exception as e:
        return {"error": str(e)}
