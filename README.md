# Hi there! 👋

I'm a computer science student and full-stack software engineer. I specialize in bridging the gap between clean, intuitive user interfaces and complex data-driven backends. My work spans everything from fundamental data structures in C++ to deploying machine learning pipelines and local LLMs for consumer-facing applications. 

## 🛠 Tech Stack & Tools

**Languages:** Python, Java, C, C++, Dart, TypeScript/JavaScript  
**Frontend:** React, Flutter (Web & Mobile), Tailwind CSS (v4/CSS-first)  
**Backend & Databases:** FastAPI, SQLite  
**Machine Learning & Data Science:** XGBoost, Scikit-Learn, pandas, SMOTE, Ollama (Local LLMs like BioMistral)  
**Engineering & Environments:** MATLAB Simulink, macOS (Anaconda workflows), Windows (MinGW)  

## 🚀 Featured Projects

# 🌿 AlamX: AI-Driven Wellness & Diagnostic Platform

AlamX is a premium, full-stack health application that bridges predictive machine learning with daily habit tracking. It features a custom monotonic scoring algorithm, real-time universal state synchronization, and a predictive diagnostic engine built on XGBoost. 

Designed with a "Premium Light Wellness" CSS-first architecture, AlamX moves beyond static dashboards to provide a highly interactive, clinically grounded user experience.

## 🚀 Key Engineering Features

### 1. Monotonic Health Scoring Engine (80/20 Architecture)
A mathematically rigorous scoring engine designed to ensure that logging healthy behavior strictly rewards the user without breaking consistency.
*   **Clinical Baseline (80 Points):** Evaluates strictly graded vitals (Heart Rate, Blood Pressure), BMI, Sleep duration, and active symptom penalties.
*   **Engagement Bonus (20 Points):** A dynamic pool rewarding daily habits (Steps, Hydration, Mindfulness, Nutrition). 
*   **Macro Balance Algorithm:** Nutrition scoring splits into per-macro attainment (capped at user targets) plus a balance modifier, penalizing lopsided diets (e.g., 200% carbs, 10% protein) without violating monotonic, non-decreasing principles.
*   **Predictive Trajectory:** Calculates a projected End-Of-Day score based on the clinical baseline and remaining scheduled wellness targets.
*   **Rolling Consistency Multiplier:** Awards a +2 point buffer for maintaining >80% habit completion over a rolling 5-day streak.

### 2. XGBoost Diagnostic AI
*   **Predictive Engine:** Transitioned from Random Forest to XGBoost (99.64% accuracy) evaluating a 132-parameter symptom vector space.
*   **Confidence & Explainability:** Utilizes `predict_proba` to deliver distinct percentage-based match confidences and alternative condition runners-up.
*   **Clinical Descriptions:** Maps 41 target diseases to localized, readable clinical descriptions for immediate user context.

### 3. Universal State Synchronization & Dynamic UI
*   **On-Demand Targets:** Users can dynamically configure precise daily targets (e.g., 8,000 steps, 2.5L water) which instantly dictate the math across the Dashboard, Wellness Plan, and Scoring Engine.
*   **Real-Time Data Flow:** Eliminates client-side state illusions. Vitals and habits are directly persisted to the SQLite backend and instantly reflected across all UI components via a centralized React context.

### 4. Robust Security & Auth
*   **JWT Architecture:** Implements stateless JWT authentication via `python-jose` and `passlib/bcrypt` password hashing.
*   **Stateless Invalidation:** Engineered a database-backed `token_version` system to successfully implement "Log Out Everywhere" functionality, allowing immediate invalidation of stateless tokens across all devices.
*   **Route Protection:** Enforces strict per-user data isolation at the API boundary and client-side route guarding.

## 🛠 Tech Stack

**Frontend**
*   React, Vite, TypeScript
*   Tailwind CSS (v4 CSS-first architecture)
*   Recharts (Dual-axis historical data visualization)
*   Custom SVG vector implementations (Zero-font-dependency icons)

**Backend & ML Engine**
*   FastAPI (Asynchronous Python REST API)
*   SQLite (Strict separation of `User_Profile` baselines and `Daily_Health_Log` timeseries)
*   Scikit-Learn & XGBoost

## ⚙️ Local Development Setup

### Backend (FastAPI)
```bash
# Navigate to backend directory
cd SukhiX_backend

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install "pydantic[email]"

# Setup environment variables
echo 'JWT_SECRET_KEY="your_generated_32_byte_secret"' > .env

# Run the server
uvicorn main:app --port 8000

## 📫 Let's Connect

* **LinkedIn:** [https://www.linkedin.com/feed/]
* **Email:** [hamidalam763@gmail.com]
---
⭐️ *Always building, learning, and refining.*
