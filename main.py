from fastapi import FastAPI
from models import Ticket, ResponseModel
from rules import rule_based_decision
from ai_model import ai_classify
import json

app = FastAPI(title="VibeFI Ticket Classifier", version="1.0")

@app.post("/classify", response_model=ResponseModel)
def classify_ticket(ticket: Ticket):
    decision, reasoning = rule_based_decision(ticket)

    if decision == "UNCERTAIN":
        ai_response = ai_classify(ticket)
        try:
            data = json.loads(ai_response)
            return ResponseModel(**data)
        except Exception:
            return ResponseModel(
                decision="REVIEW_REQUIRED",
                reasoning="LLM returned invalid response; manual validation needed.",
                checklist=["Review ticket manually", "Refine LLM prompt", "Add rule if recurring"]
            )

    # Deterministic rule-based path
    if decision == "AI_CODE_PATCH":
        checklist = [
            "Retrieve logs and recent commits",
            "Run AI patch generator",
            "Validate patch with test suite"
        ]
    else:
        checklist = [
            "Trigger Vibe troubleshooting script",
            "Verify customer connection",
            "Confirm resolution via support channel"
        ]

    return ResponseModel(decision=decision, reasoning=reasoning, checklist=checklist)
