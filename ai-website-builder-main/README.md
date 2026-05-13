# AI SiteForge — Intelligent Website Generator

## Overview

AI Website Builder is a full-stack AI-powered platform that dynamically generates professional business websites using Google Gemini AI.

Users can enter a business name and the system automatically:

* Detects business context
* Generates website content
* Creates hero/about/services/CTA sections
* Renders modern UI dynamically
* Generates different layouts for different business types

The platform is built using:

* Reflex (Python Frontend Framework)
* FastAPI Backend
* Google Gemini AI API
* MySQL Database
* SQLAlchemy ORM
* JWT Authentication

# Features

## AI Website Generation

Generate websites dynamically using Gemini AI.

### Generated Sections

* Hero Section
* About Section
* Services Section
* CTA Section
* Dynamic Business Content

---

## Dynamic Business Detection

Different business names generate different website structures.

### Example

| Business Name | Generated Website       |
| ------------- | ----------------------- |
| AIMS College  | Education Website       |
| Pizza Palace  | Restaurant Website      |
| Titan Gym     | Fitness Website         |
| TechNova AI   | SaaS/Technology Website |

---

## Modern SaaS UI

* Responsive design
* Gradient hero sections
* Modern cards
* Dynamic rendering
* Business dashboard UI
* Professional spacing and typography

---

## Authentication System

* Login
* Signup
* JWT Authentication
* Password Hashing

---

## Project Saving

* Save generated projects
* Continue editing later
* Dynamic JSON structure

---

# Tech Stack

## Frontend

* Reflex
* Python
* Reactive State Management

## Backend

* FastAPI
* SQLAlchemy
* Alembic
* JWT

## Database

* MySQL

## AI

* Google Gemini API

## Export

* ReportLab
* Markdown
* ZIP Export

---

# Project Structure

```txt
ai-website-builder/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── alembic/
│   └── requirements.txt
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── state/
│   ├── styles/
│   └── rxconfig.py
│
├── uploads/
├── exports/
├── .env
└── README.md
```

---

# Installation Guide

## 1. Clone Project

```bash
git clone <repository-url>
```

---

# Backend Setup

## 2. Navigate Backend

```bash
cd Backend
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

### CMD

```bash
venv\Scripts\activate
```

---

## 5. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Install Additional Packages

```bash
pip install google-generativeai
pip install pydantic-settings
pip install python-dotenv
```

---

# MySQL Setup

## 7. Install MySQL

Download:

* MySQL Community Server
* MySQL Workbench

---

## 8. Create Database

```sql
CREATE DATABASE ai_builder;
```

---

# Environment Variables

## 9. Create `.env`

Inside Backend folder:

```env
DATABASE_URL=mysql+pymysql://root:Sanket%406460@localhost/ai_builder

SECRET_KEY=sanket_super_secret_key_123

GEMINI_API_KEY=AIzaSyBe7ezs7w1xsEd24ukZfSDcuwnO3-qhoTU
```

---

# Gemini API Setup

## 10. Get Gemini API Key

Visit:

[https://aistudio.google.com/](https://aistudio.google.com/)

Steps:

1. Login with Google
2. Create API Key
3. Copy key
4. Paste into `.env`

---

# Run Backend

## 11. Start FastAPI

```bash
python -m uvicorn app.main:app --reload --port 8001
```

---

# Frontend Setup

## 12. Open New Terminal

```bash
cd Frontend
```

---

## 13. Install Reflex

```bash
pip install reflex
```

---

## 14. Initialize Reflex

```bash
reflex init
```

---

## 15. Run Frontend

```bash
reflex run
```

---

# Access Application

## Frontend

```txt
http://localhost:3000
```

## Backend API

```txt
http://127.0.0.1:8001/docs
```

---

# How AI Website Generation Works

## Step 1

User enters:

```txt
Business Name
```

---

## Step 2

Frontend sends request to FastAPI backend.

---

## Step 3

Backend sends prompt to Gemini AI.

---

## Step 4

Gemini generates structured JSON website sections.

Example:

```json
{
  "sections": [
    {
      "type": "hero",
      "title": "Welcome to TechNova AI"
    }
  ]
}
```

---

## Step 5

Frontend dynamically renders components.

---

# Current Features Implemented

## Completed

* Reflex frontend
* FastAPI backend
* Gemini AI integration
* Dynamic rendering
* Business-based website generation
* Responsive modern UI
* Hero/About/Services/CTA sections
* State management
* API integration

---

# Future Improvements

## Planned Features

* Drag-and-drop editor
* AI image generation
* AI logo generation
* Theme generator
* Live mobile preview
* Export HTML/CSS
* One-click deployment
* Real-time editing
* Multi-page generation
* AI chatbot assistant
* SEO generation

---

# Architecture

## Frontend Layer

Handles:

* User interaction
* Dynamic rendering
* State management
* Live preview

---

## Backend Layer

Handles:

* AI processing
* Authentication
* Database operations
* Website generation

---

## AI Layer

Handles:

* Business understanding
* Content generation
* Dynamic website structure
* Business-specific layouts


# Author

Atharv Jagtap

AI Website Builder Project

