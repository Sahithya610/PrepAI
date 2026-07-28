import httpx
from app.config import settings
from fastapi import HTTPException

async def get_ai_feedback(question: str, answer:str)->dict:
    prompt = f"""Evaluate this interview answer.
    Question: {question}
    Answer: {answer}

    Return ONLY a JSON object with these fields:
    {{"score": <1-10>, "feedback": "<overall feedback>", "improvements": "<what to improve>"}}
    Return ONLY the JSON, no other text."""
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.GROQ_API_KEY}"},
                json={
                    "model": "llama-3.1-8b-instant",
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=30.0
            )
            content = r.json()["choices"][0]["message"]["content"]
            return content
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"AI service unavailable: {str(e)}"
        )