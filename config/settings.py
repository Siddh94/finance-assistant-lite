# config/settings.py
import os
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ALPHA_VANTAGE_API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY", "")
    PINECONE_API_KEY: Optional[str] = os.getenv("PINECONE_API_KEY")
    
    # Model Configurations
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL: str = "gpt-3.5-turbo"
    WHISPER_MODEL: str = "whisper-1"
    TTS_MODEL: str = "tts-1"
    
    # Vector Store Settings
    VECTOR_DIMENSION: int = 384
    TOP_K_RETRIEVAL: int = 5
    SIMILARITY_THRESHOLD: float = 0.7
    
    # Agent Service Ports
    API_AGENT_PORT: int = 8001
    SCRAPING_AGENT_PORT: int = 8002
    RETRIEVER_AGENT_PORT: int = 8003
    ANALYSIS_AGENT_PORT: int = 8004
    LANGUAGE_AGENT_PORT: int = 8005
    VOICE_AGENT_PORT: int = 8006
    ORCHESTRATOR_PORT: int = 8000
    
    # Data Sources
    MARKET_DATA_REFRESH_INTERVAL: int = 300  # 5 minutes
    MAX_SCRAPING_PAGES: int = 50
    
    # Voice Settings
    AUDIO_SAMPLE_RATE: int = 16000
    AUDIO_CHUNK_SIZE: int = 1024
    
    class Config:
        env_file = ".env"

settings = Settings()

# config/prompts.py
SYSTEM_PROMPTS = {
    "market_analyst": """
You are a senior financial analyst specializing in Asian technology stocks. 
Analyze market data, earnings reports, and news to provide concise, actionable insights.
Focus on risk exposure, earnings surprises, and market sentiment.
Always include specific percentages and quantitative metrics.
""",
    
    "portfolio_manager": """
You are speaking to a portfolio manager who needs quick, precise market updates.
Structure your response as: Current allocation → Key changes → Market drivers → Recommendations.
Keep responses under 60 seconds when spoken aloud.
""",
    
    "data_synthesizer": """
Combine information from multiple sources (market data, news, filings) into a coherent narrative.
Prioritize: 1) Portfolio impact, 2) Risk factors, 3) Opportunities, 4) Timeline considerations.
""",
    
    "voice_assistant": """
You are a professional financial voice assistant. Speak clearly and confidently.
Use natural speech patterns with appropriate pauses. Avoid jargon unless essential.
Structure: Greeting → Key insight → Supporting details → Action items.
"""
}

ANALYSIS_TEMPLATES = {
    "morning_brief": """
Based on the following data, provide a morning market brief for Asia tech stocks:

Portfolio Data: {portfolio_data}
Market Data: {market_data}
News/Earnings: {news_data}
Filings: {filings_data}

Focus on:
1. Current risk exposure percentage
2. Significant earnings surprises (>3% vs estimates)
3. Market sentiment and key drivers
4. Actionable recommendations

Response format: Professional, quantitative, under 45 seconds spoken.
""",
    
    "risk_assessment": """
Analyze risk exposure for the following portfolio allocation:

Current Holdings: {holdings}
Market Conditions: {market_conditions}
Recent Changes: {recent_changes}

Provide:
- Risk concentration analysis
- Volatility assessment
- Correlation risks
- Hedging recommendations
"""
}

print("Configuration and prompt templates created!")
print("API keys and model settings configured")
print("System prompts optimized for financial analysis")