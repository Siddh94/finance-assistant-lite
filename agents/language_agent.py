import os
from openai import OpenAI
from config.prompts import BRIEFING_PROMPT_TEMPLATE

client = OpenAI(api_key=os.getenv("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"))

def synthesize_briefing(analysis):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" only if you have access
            messages=[
                {"role": "system", "content": "You are a financial assistant."},
                {"role": "user", "content": BRIEFING_PROMPT_TEMPLATE.format(data=analysis)}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print("OpenAI error:", e)
        return (
            f"⚠️ OpenAI error: {str(e)}\n\n"
            "🧪 Using fallback: Your Asia tech allocation is 18%. "
            "TSMC beat expectations by 15%, while Samsung had minor losses. "
            "Overall sentiment: cautiously optimistic."
        )


