#!/bin/bash
export PATH="/workspace/weather_ai_system/venv/bin:$PATH"
cd /workspace/weather_ai_system
streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true
