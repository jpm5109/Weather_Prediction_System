"""
Gemini AI Integration Module
Handles intelligent weather analysis using Google Gemini AI
"""

import google.generativeai as genai
from typing import Dict, List, Optional
import json
from config import Config

class GeminiWeatherAnalyst:
    """Gemini AI-powered weather analyst"""
    
    def __init__(self):
        """Initialize Gemini AI client"""
        if Config.GEMINI_API_KEY:
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel(
                model_name=Config.GEMINI_MODEL,
                generation_config={
                    "temperature": Config.GEMINI_TEMPERATURE,
                    "max_output_tokens": Config.GEMINI_MAX_TOKENS,
                }
            )
        else:
            self.model = None
    
    def analyze_current_weather(self, weather_data: Dict) -> str:
        """
        Analyze current weather conditions using Gemini AI
        
        Args:
            weather_data: Current weather data from API
            
        Returns:
            AI-generated analysis
        """
        if not self.model or not weather_data:
            return "Gemini AI not configured. Please add your API key to enable AI insights."
        
        try:
            current = weather_data.get('current', {})
            location = weather_data.get('location', {})
            
            prompt = f"""You are a professional meteorologist analyzing current weather conditions.

Location: {location.get('name')}, {location.get('country')}
Local Time: {location.get('localtime')}

Current Conditions:
- Temperature: {current.get('temp_c')}°C (Feels like: {current.get('feelslike_c')}°C)
- Condition: {current.get('condition', {}).get('text')}
- Humidity: {current.get('humidity')}%
- Wind: {current.get('wind_kph')} km/h {current.get('wind_dir')}
- Pressure: {current.get('pressure_mb')} mb
- Visibility: {current.get('vis_km')} km
- UV Index: {current.get('uv')}
- Cloud Cover: {current.get('cloud')}%

Provide a professional weather analysis covering:
1. Current conditions summary
2. Comfort level and what to expect
3. Outdoor activity recommendations
4. Any weather concerns or advisories

Keep the analysis concise, practical, and professional (3-4 paragraphs maximum)."""

            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Error generating AI analysis: {str(e)}"
    
    def analyze_forecast(self, forecast_data: Dict) -> str:
        """
        Analyze weather forecast using Gemini AI
        
        Args:
            forecast_data: Forecast data from API
            
        Returns:
            AI-generated forecast analysis
        """
        if not self.model or not forecast_data:
            return "Gemini AI not configured. Please add your API key to enable AI insights."
        
        try:
            forecast_days = forecast_data.get('forecast', {}).get('forecastday', [])
            location = forecast_data.get('location', {})
            
            # Prepare forecast summary
            forecast_summary = []
            for day in forecast_days[:7]:
                day_data = day.get('day', {})
                forecast_summary.append({
                    'date': day.get('date'),
                    'condition': day_data.get('condition', {}).get('text'),
                    'max_temp': day_data.get('maxtemp_c'),
                    'min_temp': day_data.get('mintemp_c'),
                    'precipitation': day_data.get('totalprecip_mm'),
                    'max_wind': day_data.get('maxwind_kph'),
                    'uv': day_data.get('uv')
                })
            
            prompt = f"""You are a professional meteorologist providing a comprehensive 7-day weather forecast analysis.

Location: {location.get('name')}, {location.get('country')}

7-Day Forecast:
{json.dumps(forecast_summary, indent=2)}

Provide a detailed forecast analysis covering:
1. Week overview and general weather trends
2. Key weather patterns and changes expected
3. Best days for outdoor activities
4. Days requiring weather precautions
5. Temperature trends and what they mean
6. Precipitation and wind patterns

Keep the analysis informative, actionable, and professional (4-5 paragraphs maximum)."""

            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Error generating forecast analysis: {str(e)}"
    
    def generate_weather_insights(self, weather_data: Dict, anomalies: List[Dict]) -> str:
        """
        Generate comprehensive weather insights
        
        Args:
            weather_data: Complete weather data
            anomalies: List of detected anomalies
            
        Returns:
            AI-generated insights
        """
        if not self.model:
            return "Gemini AI not configured. Please add your API key to enable AI insights."
        
        try:
            current = weather_data.get('current', {})
            location = weather_data.get('location', {})
            
            anomaly_summary = "\n".join([
                f"- {a['type']}: {a['description']} (Severity: {a['severity']})"
                for a in anomalies
            ]) if anomalies else "No significant anomalies detected"
            
            prompt = f"""You are a weather intelligence analyst providing expert insights.

Location: {location.get('name')}, {location.get('country')}
Current Temperature: {current.get('temp_c')}°C
Current Condition: {current.get('condition', {}).get('text')}

Detected Weather Anomalies:
{anomaly_summary}

Provide expert weather insights covering:
1. Significance of current conditions
2. Analysis of detected anomalies
3. Potential impacts on daily activities
4. Recommendations and precautions
5. What to expect in the coming hours

Be concise, actionable, and focus on practical guidance (3-4 paragraphs)."""

            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Error generating insights: {str(e)}"
    
    def get_activity_recommendations(self, weather_data: Dict) -> str:
        """
        Get AI-powered activity recommendations based on weather
        
        Args:
            weather_data: Current weather data
            
        Returns:
            Activity recommendations
        """
        if not self.model or not weather_data:
            return "Gemini AI not configured. Please add your API key to enable recommendations."
        
        try:
            current = weather_data.get('current', {})
            
            prompt = f"""Based on these current weather conditions, suggest 5 suitable activities:

Temperature: {current.get('temp_c')}°C
Condition: {current.get('condition', {}).get('text')}
Wind: {current.get('wind_kph')} km/h
UV Index: {current.get('uv')}
Humidity: {current.get('humidity')}%

Provide 5 specific, practical activity recommendations that are well-suited for these conditions.
Format: Brief activity name followed by 1-sentence explanation.
Mix indoor and outdoor suggestions based on conditions."""

            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Error generating recommendations: {str(e)}"
