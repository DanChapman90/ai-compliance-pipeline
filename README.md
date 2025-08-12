# 🛡️ AI Compliance Pipeline

## Overview
This project demonstrates how to automatically run compliance checks on machine learning workflows before code is merged into the main branch.  
It includes:
- **Bias detection** ✅  
- **PII (Personally Identifiable Information) scanning** 🔍  
- **Automated email notifications** 📩

---

## Why This Matters
In the real world, when multiple developers are working on a machine learning system, it’s crucial to make sure that:
- The model doesn’t **unfairly discriminate** between groups.
- No **sensitive personal data** is being exposed.
- Issues are caught **before deployment**, not after.

This project is designed to showcase exactly how that process can be automated using GitHub Actions.

---

## How It Works
Whenever someone pushes code to the repository:
1. **GitHub Actions** triggers the workflow.
2. The **Bias Check** script analyzes predictions to detect discrimination.
3. The **PII Check** script scans for sensitive data.
4. If either fails, the workflow stops and sends an **email notification** to the team.
5. If both pass, the code is allowed to merge into the main branch.

---

## Workflow Diagram

```mermaid
flowchart TD
    A[Developer pushes code]:::step1 --> B[GitHub Actions triggers workflow]:::step2
    B --> C[Run Bias Check]:::step3
    B --> D[Run PII Check]:::step3
    C --> E{Bias Check Passed?}:::decision
    D --> F{PII Check Passed?}:::decision
    E -- No --> G[❌ Fail pipeline & send email]:::fail
    F -- No --> G
    E -- Yes --> H
    F -- Yes --> H[✅ All checks passed - merge to main]:::pass

    classDef step1 fill:#4facfe,stroke:#000,color:#fff
    classDef step2 fill:#43e97b,stroke:#000,color:#fff
    classDef step3 fill:#f6d365,stroke:#000,color:#000
    classDef decision fill:#ff9a9e,stroke:#000,color:#000
    classDef fail fill:#ff4b5c,stroke:#000,color:#fff
    classDef pass fill:#38ef7d,stroke:#000,color:#000
