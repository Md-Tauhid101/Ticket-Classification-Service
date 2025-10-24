# 🧠 VibeFI AI – Hybrid Ticket Classification Service

## 🚀 Overview
This project implements a lightweight **AI-assisted ticket classification microservice** for banking support tickets.

The service receives a JSON ticket and decides whether it requires:
- **`AI_CODE_PATCH`** → for code-level or regression issues  
- **`VIBE_CODED_WORKFLOW`** → for configuration, onboarding, or usage issues  

It blends:
- **Rule-based logic** → fast, deterministic responses  
- **LLM fallback** → semantic understanding for ambiguous or mixed cases  

Built using **FastAPI**, **Pydantic**, and **LangChain** for clarity, modularity, and AI integration.

---

## 🧩 Architecture

Request (JSON)

│

▼

[FastAPI] → [Rule-Based Classifier] ──► if "UNCERTAIN"

│

▼

[LLM Classifier]

│

▼

Structured JSON Response


### Key Components
| File | Purpose |
|------|----------|
| `main.py` | FastAPI entry point — combines rules + LLM fallback |
| `models.py` | Defines Pydantic schemas for request/response |
| `rules.py` | Contains deterministic keyword-based decision logic |
| `ai_model.py` | Invokes LLM via LangChain for ambiguous tickets |
| `test_tickets.json` | Example inputs for quick testing |
| `requirements.txt` | Python dependencies |

---

## 🧰 Tech Stack
- **Python 3.10+**
- **FastAPI** – REST API framework  
- **Pydantic** – data validation & type enforcement  
- **LangChain + GroqAI** – LLM integration  
- **Uvicorn** – ASGI server  
- **dotenv** – environment variable management  

---

## ⚙️ Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Md-Tauhid101/Ticket-Classification-Service.git
   cd Ticket-Classification-Service
   ```
2. **Install Dependencies**
  ```bash
    pip install -r requirements.txt
  ```
3. **Add Groq API Key**
  ```bash
    GROQ_API_KEY = 'Your Groq Api here'
  ```
4. **Run the Service**
  ```bash
    uvicorn main:app --reload
  ```

## 🧪 Testing the API
  ```bash
    http://127.0.0.1:8000/docs
  ```
  **Click POST /classify, hit Try it out, and paste a JSON body by your test tickets.**
