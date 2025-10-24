import os
from langchain_groq import ChatGroq

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='llama-3.1-8b-instant', temperature=0.3)

def ai_classify(ticket):
    prompt = f"""
    You are an AI support classifier for banking tickets.
    Decide whether the issue requires:
    1. AI_CODE_PATCH — if it involves code errors, regressions, or technical bugs.
    2. VIBE_CODED_WORKFLOW — if it's configuration, usage, or account-related.

    Ticket:
    Channel: {ticket.channel}
    Severity: {ticket.severity}
    Summary: {ticket.summary}

    Respond strictly in JSON:
    {{
      "decision": "...",
      "reasoning": "...",
      "checklist": ["...", "..."]
    }}
    """
    result = llm.invoke(prompt)
    return result.content
