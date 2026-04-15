import os
from typing import Optional

# Example using OpenAI-compatible API
# Works with OpenAI or Azure OpenAI
from openai import OpenAI

def get_llm_client():
    """
    Reads API key from environment variable.
    NEVER hardcode keys.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    return OpenAI(api_key=api_key)


def generate_text(prompt: str, temperature: float = 0.4) -> str:
    client = get_llm_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # cost-efficient, high quality
        messages=[
            {"role": "system", "content": "You are a professional career assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=600
    )

    return response.choices[0].message.content.strip()