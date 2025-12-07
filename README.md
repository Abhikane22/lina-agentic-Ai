# LINA – Lending Intelligence & Negotiation Assistant

LINA is an **agentic AI–powered digital lending assistant** designed for NBFCs like Tata Capital.  
It guides users from **first enquiry to loan sanction letter** in a single conversational journey.

This repository contains:

- 🧠 **AI Agent Orchestration** (Master + Worker agents)
- 🧮 **Underwriting Rule Engine** (FOIR, credit score–based decisions)
- 🧾 **Sanction Letter Generator** (PDF)
- 🌐 **React Frontend** (chat UI)
- 🔧 **Mock Backend APIs** (CRM, credit bureau, offer config)

> ⚠️ This is a **prototype for EY Techathon 6.0** – all data and APIs are synthetic and for demo purposes only.

---

## 🔍 Problem Statement (Short)

Traditional personal loan journeys are:

- Slow: multiple handoffs, 48–72 hr TAT
- Expensive: call-centre + manual processing
- Leaky: high drop-offs between enquiry → document upload → sanction
- Inconsistent: human decisions can be biased or error-prone

**LINA** turns this into a **single agentic AI conversation** that can:

1. Qualify the user
2. Verify basic details via mock CRM
3. Run a rule-based underwriting engine
4. Explain decisions in natural language
5. Generate a sanction letter PDF on approval

---

## ✨ Key Features

- **End-to-End Loan Flow in Chat**
  - From “I need a ₹X loan” to sanction letter download.
- **Multi-Agent Design**
  - Master Agent orchestrates:
    - Sales / Conversation Agent
    - Verification Agent
    - Underwriting Agent
    - Sanctioning Agent
- **Rule Engine for Decisions**
  - Uses credit score, income, FOIR, and simple policies:
    - Instant Approval
    - Conditional Approval (salary slip)
    - Rejection with reasons
- **Mock Enterprise Integration**
  - CRM (KYC + profile)
  - Credit Bureau (score)
- **Modern Web UI**
  - React chat interface
  - Sanction letter preview/download

---

## 🏗️ High-Level Architecture

```text
User (Web Browser)
       |
       v
React Frontend (Chat UI)
       |
       v
Backend API (FastAPI / Flask)
       |
       +--> Master Agent (LLM Orchestrator)
       |       |
       |       +--> Sales Agent         (collects requirements & details)
       |       +--> Verification Agent  (calls mock CRM)
       |       +--> Underwriting Agent  (rule engine + mock credit score)
       |       +--> Sanctioning Agent   (PDF generator)
       |
       +--> Mock Services & DB
               - CRM Service (synthetic customer data)
               - Credit Score Service
               - Offer / Config Data
               - Interaction Logs


--------------------------------------------------
Repository Structure
lina-agentic-lending-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI entrypoint
│   │   ├── config.py                # settings, env handling
│   │   ├── models.py                # Pydantic models
│   │   ├── agents/
│   │   │   ├── master_agent.py
│   │   │   ├── sales_agent.py
│   │   │   ├── verification_agent.py
│   │   │   ├── underwriting_agent.py
│   │   │   └── sanctioning_agent.py
│   │   ├── services/
│   │   │   ├── crm_service.py       # mock CRM API logic
│   │   │   ├── credit_service.py    # mock credit score logic
│   │   │   └── pdf_service.py       # sanction letter generator
│   │   ├── engine/
│   │   │   └── decision_engine.py   # FOIR + rules
│   │   └── utils/
│   │       └── logging_utils.py
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   └── LoanSummaryPanel.jsx
│   │   ├── pages/
│   │   │   └── ChatPage.jsx
│   │   ├── api/
│   │   │   └── apiClient.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js or similar
│
├── docs/
│   ├── architecture-diagram.png
│   ├── api-contracts.md
│   └── prompts.md
│
├── .gitignore
├── .env.example
└── README.md
