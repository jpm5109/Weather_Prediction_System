"""
Weather API Module
Handles all interactions with WeatherAPI.com
"""

import requests
from typing import Dict, List, Optional
from datetime import datetime
from config import Config

class WeatherAPI:
    """Weather API client for fetching real-time weather data"""
    
    def __init__(self):
        self.api_key = Config.WEATHERAPI_KEY
        self.base_url = Config.WEATHER_API_BASE_URL
        
    def search_locations(self, query: str) -> List[Dict]:
        """
        Search for locations
        
        Args:
            query: Location search query
            
        Returns:
            List of matching locations
        """
        try:
            url = f"{self.base_url}/search.json"
            params = {
                'key': self.api_key,
                'q': query
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            print(f"Error searching locations: {e}")
            return []
    
    def get_current_weather(self, location: str) -> Optional[Dict]:
        """
        Get current weather conditions
        
        Args:
            location: Location name or coordinates
            
        Returns:
            Current weather data
        """
        try:
            url = f"{self.base_url}/current.json"
            params = {
                'key': self.api_key,
                'q': location,
                'aqi': 'yes'  # Include air quality data
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            print(f"Error fetching current weather: {e}")
            return None
    
    def get_forecast(self, location: str, days: int = 7) -> Optional[Dict]:
        """
        Get weather forecast
        
        Args:
            location: Location name or coordinates
            days: Number of forecast days (1-14)
            
        Returns:
            Forecast data
        """
        try:
            url = f"{self.base_url}/forecast.json"
            params = {
                'key': self.api_key,
                'q': location,
                'days': min(days, 14),  # API supports up to 14 days
                'aqi': 'yes',
                'alerts': 'yes'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            print(f"Error fetching forecast: {e}")
            return None
    
    def get_astronomy(self, location: str, date: str = None) -> Optional[Dict]:
        """
        Get astronomy data (sunrise, sunset, moon phase, etc.)
        
        Args:
            location: Location name or coordinates
            date: Date in format YYYY-MM-DD (default: today)
            
        Returns:
            Astronomy data
        """
        try:
            url = f"{self.base_url}/astronomy.json"
            params = {
                'key': self.api_key,
                'q': location,
                'dt': date or datetime.now().strftime('%Y-%m-%d')
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            print(f"Error fetching astronomy data: {e}")
            return None
    
    def analyze_weather_anomalies(self, forecast_data: Dict) -> List[Dict]:
        """
        Analyze weather data for anomalies
        
        Args:
            forecast_data: Forecast data from API
            
        Returns:
            List of detected anomalies
        """
        anomalies = []
        
        if not forecast_data or 'forecast' not in forecast_data:
            return anomalies
        
        try:
            forecast_days = forecast_data['forecast']['forecastday']
            
            # Calculate average temperature
            temps = [day['day']['avgtemp_c'] for day in forecast_days]
            avg_temp = sum(temps) / len(temps) if temps else 0
            
            for day in forecast_days:
                day_data = day['day']
                date = day['date']
                
                # Temperature anomalies
                if abs(day_data['avgtemp_c'] - avg_temp) > Config.TEMP_ANOMALY_THRESHOLD:
                    anomalies.append({
                        'type': 'Temperature Anomaly',
                        'date': date,
                        'severity': 'medium',
                        'description': f"Temperature deviation: {day_data['avgtemp_c']:.1f}C (avg: {avg_temp:.1f}C)"
                    })
                
                # High wind speed
                if day_data['maxwind_kph'] > Config.WIND_SPEED_ALERT:
                    anomalies.append({
                        'type': 'High Wind Speed',
                        'date': date,
                        'severity': 'high',
                        'description': f"Maximum wind speed: {day_data['maxwind_kph']:.0f} km/h"
                    })
                
                # Heavy precipitation
                if day_data['totalprecip_mm'] > Config.PRECIPITATION_ALERT:
                    anomalies.append({
                        'type': 'Heavy Precipitation',
                        'date': date,
                        'severity': 'high',
                        'description': f"Total precipitation: {day_data['totalprecip_mm']:.1f} mm"
                    })
                
                # Extreme UV index
                if day_data.get('uv', 0) > 8:
                    anomalies.append({
                        'type': 'Extreme UV Index',
                        'date': date,
                        'severity': 'medium',
                        'description': f"UV Index: {day_data['uv']}"
                    })
        
        except Exception as e:
            print(f"Error analyzing anomalies: {e}")
        
        return anomalies
