# API Contracts – LINA (Agentic Lending Assistant)

This document defines the request/response formats for all backend endpoints.  
Frontend, backend, and AI agent developers must follow these contracts for integration.

------------------------------
1. POST /chat

Request:
{
  "session_id": "string",
  "message": "User message text"
}

Response:
{
  "response": "AI reply message",
  "session_id": "string",
  "metadata": {
    "stage": "collecting_details | verification | underwriting | approval | conditional | rejection",
    "loan_application": {
      "amount": 200000,
      "tenure_months": 24,
      "purpose": "Travel",
      "income": 50000
    },
    "decision": {
      "status": "APPROVED | CONDITIONAL | REJECTED | PENDING",
      "max_amount": 250000,
      "interest_rate": 14.5,
      "reason": null,
      "conditions": []
    },
    "sanction_letter_url": null
  }
}
---
2. POST /crm/verify

Request:
{
  "name": "string",
  "phone": "string",
  "pan": "string"
}

Response:
{
  "customer_id": "C1234",
  "kyc_status": "VERIFIED",
  "income": 50000,
  "existing_emi": 5000,
  "preapproved_limit": 250000
}

Failure Repsonse:
{
  "kyc_status": "NOT_FOUND"
}

--
3. POST /credit-score

Request :
{
  "customer_id": "C1234",
  "pan": "ABCDE1234F"
}

Response:
{
  "score": 735
}


--
4. POST /underwrite

Request:
{
  "customer_id": "C1234",
  "amount": 200000,
  "tenure_months": 24,
  "income": 50000,
  "existing_emi": 5000,
  "credit_score": 735
}

Response:
{
  "status": "APPROVED | CONDITIONAL | REJECTED",
  "max_amount": 250000,
  "interest_rate": 14.5,
  "reason": null,
  "conditions": []
}


----
5. POST /sanction-letter

Request:
{
  "customer_id": "C1234",
  "amount": 200000,
  "tenure_months": 24,
  "interest_rate": 14.5
}


Reponse
{
  "pdf_url": "http://localhost:8000/static/sanction_letters/C1234_loan.pdf"
}

--
6. POST /upload-salary-slip

Request:
{
  "customer_id": "C1234",
  "file_name": "salary_slip.pdf"
}

Response:
{
  "uploaded": true
}
s