AI SiteForge — Intelligent Website Generator
Overview

AI SiteForge is a full-stack AI-powered platform that automatically generates modern business websites using Google Gemini AI.

Users simply enter a business name, and the system intelligently:

Detects the business category
Generates website content dynamically
Creates Hero, About, Services, and CTA sections
Builds responsive UI layouts
Adapts designs for different industries

The platform is developed using:

Reflex (Frontend Framework)
FastAPI
Google Gemini AI
MySQL
SQLAlchemy ORM
JWT Authentication
Features
AI Website Generation

Generate complete business websites dynamically using Gemini AI.

Dynamic Website Sections
Hero Section
About Section
Services Section
Call-To-Action Section
Smart Business Detection

Different business names automatically generate different website styles and content.

Examples
Business Name	Generated Website Type
Bright Future Academy	Education Website
Spice Garden	Restaurant Website
IronCore Fitness	Gym/Fitness Website
NovaTech Solutions	SaaS/Technology Website
Modern UI Features
Fully responsive layout
Modern gradients and cards
Dynamic rendering
Professional typography
Dashboard-style interface
Smooth spacing and alignment
Authentication System
User Signup
User Login
JWT Authentication
Password Hashing & Security
Project Management
Save generated projects
Continue editing later
JSON-based dynamic storage
Tech Stack
Frontend
Reflex
Python
Reactive State Management
Backend
FastAPI
SQLAlchemy
Alembic
JWT Authentication
Database
MySQL
AI Integration
Google Gemini API
Export Features
Markdown Export
ZIP Export
ReportLab PDF Export
Project Structure
ai-siteforge/
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
Installation Guide
1. Clone Repository
git clone <repository-url>
Backend Setup
2. Navigate to Backend
cd backend
3. Create Virtual Environment
python -m venv venv
4. Activate Virtual Environment
PowerShell
.\venv\Scripts\Activate.ps1
CMD
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Install Additional Packages
pip install google-generativeai
pip install pydantic-settings
pip install python-dotenv
MySQL Configuration
7. Install MySQL

Required:

MySQL Community Server
MySQL Workbench
8. Create Database
CREATE DATABASE siteforge_db;
Environment Variables
9. Create .env File
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/siteforge_db

SECRET_KEY=your_secret_key_here

GEMINI_API_KEY=your_gemini_api_key
Gemini API Setup
10. Generate API Key

Visit:

Google AI Studio

Steps
Login with Google Account
Create API Key
Copy API Key
Paste into .env
Run Backend Server
11. Start FastAPI
python -m uvicorn app.main:app --reload --port 8001
Frontend Setup
12. Open New Terminal
cd frontend
13. Install Reflex
pip install reflex
14. Initialize Reflex
reflex init
15. Run Frontend
reflex run
Access Application
Frontend
http://localhost:3000
Backend API Docs
http://127.0.0.1:8001/docs
AI Workflow
Step 1

User enters business name.

Step 2

Frontend sends request to FastAPI backend.

Step 3

Backend sends prompt to Gemini AI.

Step 4

Gemini AI generates structured website JSON.

Example
{
  "sections": [
    {
      "type": "hero",
      "title": "Welcome to NovaTech Solutions"
    }
  ]
}
Step 5

Frontend dynamically renders website components.

Implemented Features

✅ Reflex Frontend
✅ FastAPI Backend
✅ Gemini AI Integration
✅ Dynamic Website Rendering
✅ Business-Type Detection
✅ Responsive UI
✅ Hero/About/Services/CTA Sections
✅ State Management
✅ API Integration

Future Enhancements
Drag & Drop Website Editor
AI Logo Generator
AI Image Generator
Theme Customizer
Live Mobile Preview
HTML/CSS Export
One-click Deployment
Real-time Editing
Multi-page Website Generation
AI Chat Assistant
SEO Content Generator
System Architecture
Frontend Layer

Handles:

User Interaction
Dynamic Rendering
State Management
Live Website Preview
Backend Layer

Handles:

AI Processing
Authentication
Database Operations
Website Generation Logic
AI Layer

Handles:

Business Understanding
Content Generation
Layout Personalization
Website Structure Generation
Author

Atharv Jagtap
Cloud Technology & Information Security Student

License

This project is developed for educational and learning purposes.
