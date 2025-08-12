# AI Compliance Pipeline

This project implements basic AI compliance checks, including:

- **Bias Check:** Detects bias in model predictions across sensitive groups using Fairlearn.
- **PII Check:** Scans data inputs for potential Personally Identifiable Information (PII).

## How to Run

1. Clone the repo.
2. Create and activate a Python virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the checks:

```bash
python checks/bias_check.py
python checks/pii_check.py
