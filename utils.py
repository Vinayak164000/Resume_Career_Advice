from dataclasses import dataclass
from langchain_google_genai import ChatGoogleGenerativeAI

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

@dataclass
class CareerAdvice:
    """Response schema for the agent."""
    punny_response: str
    career_advice: str | None = None

def create_bot():
    bot = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )
    return bot