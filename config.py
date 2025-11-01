"""
Configuration module for Weather AI System
Handles environment variables and application settings
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration"""
    
    # API Keys
    WEATHERAPI_KEY = os.getenv('WEATHERAPI_KEY', '')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    
    # API Endpoints
    WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"
    
    # Application Settings
    DEFAULT_LOCATION = "London"
    FORECAST_DAYS = 7
    CACHE_TTL = 600  # Cache time-to-live in seconds (10 minutes)
    
    # Gemini AI Settings
    GEMINI_MODEL = "gemini-2.0-flash-exp"
    GEMINI_TEMPERATURE = 0.2
    GEMINI_MAX_TOKENS = 1000
    
    # Weather Alert Thresholds
    TEMP_ANOMALY_THRESHOLD = 5  # degrees Celsius
    WIND_SPEED_ALERT = 50  # km/h
    PRECIPITATION_ALERT = 50  # mm
    
    @staticmethod
    def validate():
        """Validate configuration"""
        errors = []
        
        if not Config.WEATHERAPI_KEY or Config.WEATHERAPI_KEY == 'your_weatherapi_key_here':
            errors.append("WEATHERAPI_KEY is not configured")
        
        if not Config.GEMINI_API_KEY or Config.GEMINI_API_KEY == 'your_gemini_api_key_here':
            errors.append("GEMINI_API_KEY is not configured")
        
        return errors
    
    @staticmethod
    def get_status():
        """Get configuration status"""
        return {
            "Weather API": "Configured" if Config.WEATHERAPI_KEY and Config.WEATHERAPI_KEY != 'your_weatherapi_key_here' else "Not Configured",
            "Gemini AI": "Configured" if Config.GEMINI_API_KEY and Config.GEMINI_API_KEY != 'your_gemini_api_key_here' else "Not Configured"
        }
