"""
Data Visualization Module
Professional charts and visualizations for weather data
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from typing import Dict, List
from datetime import datetime

class WeatherVisualizer:
    """Create professional weather visualizations"""
    
    # Industrial color scheme
    COLORS = {
        'primary': '#1f77b4',
        'secondary': '#ff7f0e',
        'success': '#2ca02c',
        'danger': '#d62728',
        'warning': '#ff7f0e',
        'info': '#17becf',
        'background': '#f8f9fa',
        'grid': '#e1e4e8'
    }
    
    @staticmethod
    def create_temperature_chart(forecast_data: Dict) -> go.Figure:
        """
        Create temperature forecast chart
        
        Args:
            forecast_data: Forecast data from API
            
        Returns:
            Plotly figure object
        """
        if not forecast_data or 'forecast' not in forecast_data:
            return go.Figure()
        
        forecast_days = forecast_data['forecast']['forecastday']
        
        dates = [day['date'] for day in forecast_days]
        max_temps = [day['day']['maxtemp_c'] for day in forecast_days]
        min_temps = [day['day']['mintemp_c'] for day in forecast_days]
        avg_temps = [day['day']['avgtemp_c'] for day in forecast_days]
        
        fig = go.Figure()
        
        # Add temperature traces
        fig.add_trace(go.Scatter(
            x=dates, y=max_temps,
            mode='lines+markers',
            name='Max Temperature',
            line=dict(color=WeatherVisualizer.COLORS['danger'], width=2),
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates, y=avg_temps,
            mode='lines+markers',
            name='Avg Temperature',
            line=dict(color=WeatherVisualizer.COLORS['primary'], width=2),
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates, y=min_temps,
            mode='lines+markers',
            name='Min Temperature',
            line=dict(color=WeatherVisualizer.COLORS['info'], width=2),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title='7-Day Temperature Forecast',
            xaxis_title='Date',
            yaxis_title='Temperature (°C)',
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        
        return fig
    
    @staticmethod
    def create_precipitation_chart(forecast_data: Dict) -> go.Figure:
        """
        Create precipitation forecast chart
        
        Args:
            forecast_data: Forecast data from API
            
        Returns:
            Plotly figure object
        """
        if not forecast_data or 'forecast' not in forecast_data:
            return go.Figure()
        
        forecast_days = forecast_data['forecast']['forecastday']
        
        dates = [day['date'] for day in forecast_days]
        precipitation = [day['day']['totalprecip_mm'] for day in forecast_days]
        rain_chance = [day['day']['daily_chance_of_rain'] for day in forecast_days]
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # Precipitation bars
        fig.add_trace(
            go.Bar(
                x=dates,
                y=precipitation,
                name='Precipitation (mm)',
                marker_color=WeatherVisualizer.COLORS['primary'],
                opacity=0.7
            ),
            secondary_y=False
        )
        
        # Rain chance line
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=rain_chance,
                name='Chance of Rain (%)',
                line=dict(color=WeatherVisualizer.COLORS['danger'], width=2),
                marker=dict(size=8)
            ),
            secondary_y=True
        )
        
        fig.update_layout(
            title='Precipitation Forecast',
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        fig.update_xaxes(title_text="Date", showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        fig.update_yaxes(title_text="Precipitation (mm)", secondary_y=False, showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        fig.update_yaxes(title_text="Chance of Rain (%)", secondary_y=True)
        
        return fig
    
    @staticmethod
    def create_wind_chart(forecast_data: Dict) -> go.Figure:
        """
        Create wind speed forecast chart
        
        Args:
            forecast_data: Forecast data from API
            
        Returns:
            Plotly figure object
        """
        if not forecast_data or 'forecast' not in forecast_data:
            return go.Figure()
        
        forecast_days = forecast_data['forecast']['forecastday']
        
        dates = [day['date'] for day in forecast_days]
        max_wind = [day['day']['maxwind_kph'] for day in forecast_days]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=dates,
            y=max_wind,
            name='Max Wind Speed',
            marker=dict(
                color=max_wind,
                colorscale='Blues',
                showscale=True,
                colorbar=dict(title="km/h")
            )
        ))
        
        # Add warning line at threshold
        fig.add_hline(
            y=50,
            line_dash="dash",
            line_color=WeatherVisualizer.COLORS['danger'],
            annotation_text="High Wind Alert"
        )
        
        fig.update_layout(
            title='Wind Speed Forecast',
            xaxis_title='Date',
            yaxis_title='Wind Speed (km/h)',
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        
        return fig
    
    @staticmethod
    def create_conditions_summary(forecast_data: Dict) -> go.Figure:
        """
        Create weather conditions summary visualization
        
        Args:
            forecast_data: Forecast data from API
            
        Returns:
            Plotly figure object
        """
        if not forecast_data or 'forecast' not in forecast_data:
            return go.Figure()
        
        forecast_days = forecast_data['forecast']['forecastday']
        
        # Count weather conditions
        conditions = {}
        for day in forecast_days:
            condition = day['day']['condition']['text']
            conditions[condition] = conditions.get(condition, 0) + 1
        
        fig = go.Figure(data=[go.Pie(
            labels=list(conditions.keys()),
            values=list(conditions.values()),
            hole=0.4,
            marker=dict(colors=px.colors.qualitative.Set3)
        )])
        
        fig.update_layout(
            title='Weather Conditions Distribution (7 Days)',
            annotations=[dict(text='Conditions', x=0.5, y=0.5, font_size=14, showarrow=False)],
            font=dict(size=12),
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        return fig
    
    @staticmethod
    def create_hourly_chart(forecast_data: Dict, date: str) -> go.Figure:
        """
        Create hourly forecast chart for a specific date
        
        Args:
            forecast_data: Forecast data from API
            date: Date string (YYYY-MM-DD)
            
        Returns:
            Plotly figure object
        """
        if not forecast_data or 'forecast' not in forecast_data:
            return go.Figure()
        
        # Find the day's data
        day_data = None
        for day in forecast_data['forecast']['forecastday']:
            if day['date'] == date:
                day_data = day
                break
        
        if not day_data or 'hour' not in day_data:
            return go.Figure()
        
        hours = day_data['hour']
        times = [h['time'].split(' ')[1] for h in hours]
        temps = [h['temp_c'] for h in hours]
        feels_like = [h['feelslike_c'] for h in hours]
        precip = [h['precip_mm'] for h in hours]
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # Temperature traces
        fig.add_trace(
            go.Scatter(
                x=times, y=temps,
                mode='lines+markers',
                name='Temperature',
                line=dict(color=WeatherVisualizer.COLORS['primary'], width=2)
            ),
            secondary_y=False
        )
        
        fig.add_trace(
            go.Scatter(
                x=times, y=feels_like,
                mode='lines',
                name='Feels Like',
                line=dict(color=WeatherVisualizer.COLORS['secondary'], width=1, dash='dash')
            ),
            secondary_y=False
        )
        
        # Precipitation bars
        fig.add_trace(
            go.Bar(
                x=times, y=precip,
                name='Precipitation',
                marker_color=WeatherVisualizer.COLORS['info'],
                opacity=0.3
            ),
            secondary_y=True
        )
        
        fig.update_layout(
            title=f'Hourly Forecast for {date}',
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        fig.update_xaxes(title_text="Hour", showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        fig.update_yaxes(title_text="Temperature (°C)", secondary_y=False, showgrid=True, gridwidth=1, gridcolor=WeatherVisualizer.COLORS['grid'])
        fig.update_yaxes(title_text="Precipitation (mm)", secondary_y=True)
        
        return fig
