<div align="center">

# HAMID ALAM

### AI/ML · FULL-STACK · SOFTWARE ENGINEERING

```text
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│        BUILDING INTELLIGENT SOFTWARE SYSTEMS                 │
│                                                              │
│        AI  ×  DATA  ×  BACKEND  ×  PRODUCT                   │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=2800&pause=900&color=8B949E&center=true&vCenter=true&width=760&lines=Full-Stack+Developer;AI%2FML+Engineer;Building+data-driven+products;Learning+%E2%86%92+Building+%E2%86%92+Shipping" />

<br/>

<img src="https://img.shields.io/badge/Python-111111?style=for-the-badge&logo=python&logoColor=3776AB"/>
<img src="https://img.shields.io/badge/TypeScript-111111?style=for-the-badge&logo=typescript&logoColor=3178C6"/>
<img src="https://img.shields.io/badge/FastAPI-111111?style=for-the-badge&logo=fastapi&logoColor=009688"/>
<img src="https://img.shields.io/badge/React-111111?style=for-the-badge&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/AWS-111111?style=for-the-badge&logo=amazonaws&logoColor=FF9900"/>

</div>

---

## `01` — PROFILE

I am a **Computer Science Engineering student and full-stack software developer** focused on building applications where intelligent models, clean interfaces, and reliable backend systems work together.

My work spans from **data structures and systems programming** to **machine learning pipelines, APIs, local LLM workflows, and consumer-facing applications**.

```text
                IDEA
                  │
                  ▼
             ARCHITECTURE
                  │
                  ▼
            IMPLEMENTATION
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
      AI / ML           SOFTWARE
        │                   │
        └─────────┬─────────┘
                  ▼
                PRODUCT
```

---

# `02` — TECH STACK

### Languages

`Python` `Java` `C` `C++` `Dart` `TypeScript` `JavaScript`

### Frontend

`React` `Flutter` `Tailwind CSS v4` `Vite` `Recharts`

### Backend

`FastAPI` `REST APIs` `SQLite`

### AI / Machine Learning

`XGBoost` `Scikit-Learn` `pandas` `SMOTE` `Ollama` `BioMistral`

### Engineering

`Docker` `Git` `GitHub` `MATLAB Simulink` `Anaconda`

### Development Environments

`macOS` `Windows` `MinGW`

---

# `03` — FEATURED PROJECT

# 🌿 AlamX

### AI-Driven Wellness & Health Intelligence Platform

AlamX is a full-stack health application combining **predictive machine learning, wellness tracking, personalized scoring, and interactive data visualization**.

The system is designed around a **Premium Light Wellness** interface and a backend architecture where health data is persisted centrally and shared across the application.

---

## `04` — CORE ENGINEERING

### `01` MONOTONIC HEALTH SCORING ENGINE

An **80/20 scoring architecture** separates clinical baseline measurements from daily engagement.

```text
                    HEALTH SCORE
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        CLINICAL BASELINE      ENGAGEMENT
             80%                  20%
              │                     │
      ┌───────┼────────┐       ┌────┼─────┐
      ▼       ▼        ▼       ▼    ▼     ▼
   Vitals    BMI     Sleep   Steps Water Nutrition
              │                     │
              └──────────┬──────────┘
                         ▼
                  FINAL SCORE
```

### Clinical Baseline

Evaluates:

* Heart Rate
* Blood Pressure
* BMI
* Sleep duration
* Active symptom penalties

### Engagement Layer

Rewards:

* Steps
* Hydration
* Mindfulness
* Nutrition
* Daily wellness completion

### Additional Logic

* Macro balance modifier
* Projected end-of-day score
* Rolling 5-day consistency multiplier
* Configurable daily targets
* Monotonic, non-decreasing scoring behavior

---

# `05` — XGBOOST PREDICTIVE ENGINE

AlamX uses an **XGBoost-based prediction pipeline** over a **132-parameter symptom vector**.

### Prediction Workflow

```text
SYMPTOM INPUT
      │
      ▼
FEATURE VECTOR
      │
      ▼
PREPROCESSING
      │
      ▼
XGBOOST MODEL
      │
      ├──────────────┐
      ▼              ▼
MATCH CONFIDENCE   ALTERNATIVES
      │              │
      └───────┬──────┘
              ▼
       USER-FACING RESULT
```

### Model Layer

* XGBoost predictive engine
* `predict_proba` confidence estimation
* Alternative prediction candidates
* 132-parameter symptom space
* Mapping of 41 target conditions to readable descriptions

> **Model performance:** the project reports **99.64% accuracy** for its configured XGBoost evaluation. This figure should be interpreted in the context of the project's dataset and evaluation methodology.

---

# `06` — UNIVERSAL STATE SYNCHRONIZATION

One of the central engineering goals of AlamX is maintaining **one consistent source of truth** across the application.

```text
              ┌──────────────────┐
              │     SQLite DB    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   FastAPI API    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ React Context    │
              │  State Layer     │
              └────────┬─────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Dashboard    Wellness     Scoring
                      Plan       Engine
```

### Dynamic Targets

Users can configure targets such as:

```text
Steps       → 8,000 / day
Water       → 2.5 L / day
Sleep       → Custom target
Nutrition   → Personalized target
```

These targets propagate through the scoring system instead of being hard-coded into individual UI components.

---

# `07` — SECURITY & AUTHENTICATION

### JWT Authentication

AlamX uses stateless JWT authentication with:

* `python-jose`
* `passlib`
* `bcrypt`

### Token Invalidation

A database-backed `token_version` mechanism enables:

```text
LOGIN
  ↓
JWT CREATED
  ↓
TOKEN VERSION STORED
  ↓
MULTI-DEVICE SESSION
  ↓
"LOG OUT EVERYWHERE"
  ↓
TOKEN VERSION CHANGED
  ↓
PREVIOUS TOKENS INVALID
```

### Data Isolation

API routes enforce **per-user data boundaries**, supported by client-side route protection.

---

# `08` — FRONTEND ARCHITECTURE

### Stack

```text
React
  │
  ├── TypeScript
  ├── Vite
  ├── Tailwind CSS v4
  ├── Recharts
  └── Custom SVG UI
```

### UI Principles

```text
Clean
   ↓
Consistent
   ↓
Interactive
   ↓
Data-driven
   ↓
User-centered
```

The application uses custom SVG-based interface elements to minimize dependency on external icon/font systems.

---

# `09` — BACKEND ARCHITECTURE

```text
                    CLIENT
                      │
                      ▼
              ┌───────────────┐
              │   FastAPI     │
              │   REST API    │
              └───────┬───────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Auth Layer   ML Engine   Health Data
          │           │           │
          └───────────┼───────────┘
                      ▼
                  SQLite DB
```

### Database Separation

The backend maintains distinct concepts for:

```text
User_Profile
       +
Daily_Health_Log
```

This keeps persistent user baselines separate from longitudinal health records.

---

# `10` — ML / DATA PIPELINE

```text
Raw Data
   │
   ▼
Cleaning
   │
   ▼
Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
SMOTE / Balancing
   │
   ▼
Model Training
   │
   ▼
Evaluation
   │
   ▼
Inference
   │
   ▼
Application
```

---

# `11` — LOCAL AI

I also experiment with **local LLM workflows** using:

```text
Ollama
   │
   └── BioMistral
```

The goal is to explore how useful AI-assisted workflows can be built with **local inference and reduced dependence on external APIs**.

---

# `12` — SELECTED PROJECTS

| Project         | Focus                                            |
| --------------- | ------------------------------------------------ |
| 🌿 **AlamX**    | AI-driven wellness & health intelligence         |
| 🏥 **CarePath** | Evidence-linked healthcare recovery architecture |
| 🧠 **NirogX**   | AI-powered symptom analysis                      |
| 🔐 **SAJAG**    | Privacy-oriented intelligent health architecture |

---

# `13` — DEVELOPMENT PHILOSOPHY

```text
┌──────────────────────────────────────────────────────┐
│                                                      │
│  UNDERSTAND  →  DESIGN  →  BUILD  →  TEST           │
│                                                      │
│  SIMPLE SYSTEMS > UNNECESSARY COMPLEXITY             │
│                                                      │
│  DATA SHOULD INFORM THE PRODUCT                      │
│                                                      │
│  AI SHOULD SOLVE A REAL PROBLEM                      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

# `14` — GITHUB ACTIVITY

<div align="center">

<img height="165"
src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&hide_border=true&bg_color=00000000&title_color=8B949E&text_color=8B949E&icon_color=8B949E&rank_icon=github"/>

<img height="165"
src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&hide_border=true&bg_color=00000000&title_color=8B949E&text_color=8B949E"/>

</div>

---

# `15` — CONTRIBUTION GRAPH

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&bg_color=00000000&color=8B949E&line=8B949E&point=FFFFFF&area=true&hide_border=true"/>

</div>

---

# `16` — LOCAL DEVELOPMENT

## Backend

```bash
cd SukhiX_backend

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install "pydantic[email]"

# Configure environment
echo 'JWT_SECRET_KEY="your_generated_32_byte_secret"' > .env

# Start FastAPI
uvicorn main:app --port 8000
```

---

# `17` — CONNECT

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-111111?style=for-the-badge\&logo=linkedin\&logoColor=0A66C2)](https://www.linkedin.com/feed/)

[![Email](https://img.shields.io/badge/Email-111111?style=for-the-badge\&logo=gmail\&logoColor=EA4335)](mailto:hamidalam763@gmail.com)

<br><br>

### BUILD · LEARN · EXPERIMENT · SHIP

<img src="https://komarev.com/ghpvc/?username=YOUR_USERNAME&style=flat-square&color=8B949E"/>

</div>
