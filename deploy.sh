#!/bin/bash
# Deployment script for Weather AI System

echo "======================================"
echo "Weather AI System - Deployment"
echo "======================================"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found"
    echo "Creating .env from template..."
    cp .env.example .env
    echo "✓ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys before running"
    echo "   1. Get WeatherAPI key from: https://www.weatherapi.com/signup.aspx"
    echo "   2. Get Gemini AI key from: https://aistudio.google.com/app/apikey"
    echo ""
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install -q -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Run the application
echo "======================================"
echo "Starting Weather AI System..."
echo "======================================"
echo ""
echo "The application will be available at:"
echo "  → http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

streamlit run app.py
