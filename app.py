"""
Advanced Industrial-Grade AI Weather Prediction System
Professional weather forecasting with Gemini AI integration
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from config import Config
from weather_api import WeatherAPI
from gemini_ai import GeminiWeatherAnalyst
from visualizations import WeatherVisualizer

# Page configuration
st.set_page_config(
    page_title="AI Weather Prediction System",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for industrial design
st.markdown("""
<style>
    /* Main theme colors - Industrial blues and grays */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #2c3e50;
        --background-color: #f8f9fa;
        --card-background: #ffffff;
        --text-color: #2c3e50;
        --border-color: #e1e4e8;
    }
    
    /* Header styling */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary-color);
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
        border-bottom: 3px solid var(--primary-color);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: white;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Alert boxes */
    .alert-box {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid;
    }
    
    .alert-high {
        background-color: #fee;
        border-color: #dc3545;
        color: #721c24;
    }
    
    .alert-medium {
        background-color: #fff3cd;
        border-color: #ffc107;
        color: #856404;
    }
    
    .alert-low {
        background-color: #d1ecf1;
        border-color: #17a2b8;
        color: #0c5460;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--secondary-color);
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--border-color);
    }
    
    /* Info box */
    .info-box {
        background: linear-gradient(to right, #e3f2fd, #f5f5f5);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
    
    /* Status indicator */
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-ok {
        background-color: #28a745;
    }
    
    .status-error {
        background-color: #dc3545;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'location' not in st.session_state:
    st.session_state.location = Config.DEFAULT_LOCATION
if 'weather_data' not in st.session_state:
    st.session_state.weather_data = None
if 'forecast_data' not in st.session_state:
    st.session_state.forecast_data = None

# Initialize API clients
@st.cache_resource
def get_weather_api():
    return WeatherAPI()

@st.cache_resource
def get_ai_analyst():
    return GeminiWeatherAnalyst()

weather_api = get_weather_api()
ai_analyst = get_ai_analyst()

# Main header
st.markdown('<h1 class="main-header">🌦️ Advanced AI Weather Prediction System</h1>', unsafe_allow_html=True)

# Sidebar - Configuration and Controls
with st.sidebar:
    st.markdown("### System Configuration")
    
    # Configuration status
    config_status = Config.get_status()
    st.markdown("#### API Status")
    for service, status in config_status.items():
        status_class = "status-ok" if status == "Configured" else "status-error"
        st.markdown(
            f'<div><span class="{status_class} status-indicator"></span>{service}: {status}</div>',
            unsafe_allow_html=True
        )
    
    # Display configuration warnings if needed
    config_errors = Config.validate()
    if config_errors:
        st.warning("⚠️ Configuration Required")
        st.markdown("**Missing API Keys:**")
        for error in config_errors:
            st.markdown(f"- {error}")
        st.info("""
        To configure API keys:
        1. Copy `.env.example` to `.env`
        2. Add your API keys
        3. Restart the application
        
        **Get API Keys:**
        - [WeatherAPI.com](https://www.weatherapi.com/signup.aspx)
        - [Gemini AI](https://aistudio.google.com/app/apikey)
        """)
    
    st.markdown("---")
    
    # Location search
    st.markdown("### Location Search")
    search_query = st.text_input(
        "Search for a location",
        value=st.session_state.location,
        placeholder="Enter city name..."
    )
    
    if st.button("🔍 Search Weather", use_container_width=True):
        if search_query:
            st.session_state.location = search_query
            # Clear cached data
            st.session_state.weather_data = None
            st.session_state.forecast_data = None
            st.rerun()
    
    st.markdown("---")
    
    # Forecast settings
    st.markdown("### Forecast Settings")
    forecast_days = st.slider(
        "Forecast Days",
        min_value=3,
        max_value=7,
        value=7,
        help="Number of days to forecast"
    )
    
    st.markdown("---")
    
    # About section
    st.markdown("### About")
    st.info("""
    **Industrial-Grade Weather System**
    
    - Real-time weather data via WeatherAPI.com
    - AI-powered analysis with Gemini
    - Professional data visualization
    - Weather anomaly detection
    - Global location support
    """)

# Main content area
if not config_errors:
    # Fetch weather data
    with st.spinner(f"Fetching weather data for {st.session_state.location}..."):
        if st.session_state.weather_data is None:
            st.session_state.weather_data = weather_api.get_current_weather(st.session_state.location)
        if st.session_state.forecast_data is None:
            st.session_state.forecast_data = weather_api.get_forecast(st.session_state.location, forecast_days)
    
    if st.session_state.weather_data and st.session_state.forecast_data:
        current = st.session_state.weather_data['current']
        location = st.session_state.weather_data['location']
        
        # Location header
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"## 📍 {location['name']}, {location['country']}")
            st.caption(f"Coordinates: {location['lat']}, {location['lon']} | Local time: {location['localtime']}")
        with col2:
            st.metric("Timezone", location['tz_id'])
        with col3:
            st.metric("Last Updated", datetime.now().strftime("%H:%M"))
        
        # Current weather metrics
        st.markdown('<div class="section-header">Current Conditions</div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric(
                label="Temperature",
                value=f"{current['temp_c']}°C",
                delta=f"Feels like {current['feelslike_c']}°C"
            )
        
        with col2:
            st.metric(
                label="Condition",
                value=current['condition']['text']
            )
        
        with col3:
            st.metric(
                label="Humidity",
                value=f"{current['humidity']}%"
            )
        
        with col4:
            st.metric(
                label="Wind",
                value=f"{current['wind_kph']} km/h",
                delta=current['wind_dir']
            )
        
        with col5:
            st.metric(
                label="Pressure",
                value=f"{current['pressure_mb']} mb"
            )
        
        # Additional metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("UV Index", current['uv'])
        with col2:
            st.metric("Visibility", f"{current['vis_km']} km")
        with col3:
            st.metric("Cloud Cover", f"{current['cloud']}%")
        with col4:
            st.metric("Precipitation", f"{current['precip_mm']} mm")
        
        # AI Analysis Section
        st.markdown('<div class="section-header">🤖 Gemini AI Weather Analysis</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["Current Analysis", "7-Day Forecast", "Activity Recommendations"])
        
        with tab1:
            with st.spinner("Generating AI analysis..."):
                analysis = ai_analyst.analyze_current_weather(st.session_state.weather_data)
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.markdown(analysis)
                st.markdown('</div>', unsafe_allow_html=True)
        
        with tab2:
            with st.spinner("Analyzing forecast patterns..."):
                forecast_analysis = ai_analyst.analyze_forecast(st.session_state.forecast_data)
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.markdown(forecast_analysis)
                st.markdown('</div>', unsafe_allow_html=True)
        
        with tab3:
            with st.spinner("Generating activity recommendations..."):
                recommendations = ai_analyst.get_activity_recommendations(st.session_state.weather_data)
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.markdown(recommendations)
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Weather Anomalies
        anomalies = weather_api.analyze_weather_anomalies(st.session_state.forecast_data)
        
        if anomalies:
            st.markdown('<div class="section-header">⚠️ Weather Alerts & Anomalies</div>', unsafe_allow_html=True)
            
            for anomaly in anomalies:
                severity_class = f"alert-{anomaly['severity']}"
                st.markdown(f"""
                <div class="alert-box {severity_class}">
                    <strong>{anomaly['type']}</strong> ({anomaly['date']})<br>
                    {anomaly['description']}
                </div>
                """, unsafe_allow_html=True)
            
            # AI insights on anomalies
            with st.expander("🤖 AI Insights on Detected Anomalies"):
                with st.spinner("Analyzing weather anomalies..."):
                    insights = ai_analyst.generate_weather_insights(st.session_state.weather_data, anomalies)
                    st.markdown(insights)
        
        # Data Visualizations
        st.markdown('<div class="section-header">📊 Weather Forecast Visualizations</div>', unsafe_allow_html=True)
        
        # Temperature chart
        st.plotly_chart(
            WeatherVisualizer.create_temperature_chart(st.session_state.forecast_data),
            use_container_width=True,
            key="temp_chart"
        )
        
        # Precipitation and Wind charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(
                WeatherVisualizer.create_precipitation_chart(st.session_state.forecast_data),
                use_container_width=True,
                key="precip_chart"
            )
        
        with col2:
            st.plotly_chart(
                WeatherVisualizer.create_wind_chart(st.session_state.forecast_data),
                use_container_width=True,
                key="wind_chart"
            )
        
        # Weather conditions distribution
        st.plotly_chart(
            WeatherVisualizer.create_conditions_summary(st.session_state.forecast_data),
            use_container_width=True,
            key="conditions_chart"
        )
        
        # Hourly forecast
        st.markdown('<div class="section-header">⏰ Hourly Forecast</div>', unsafe_allow_html=True)
        
        forecast_dates = [day['date'] for day in st.session_state.forecast_data['forecast']['forecastday']]
        selected_date = st.selectbox("Select Date for Hourly Forecast", forecast_dates)
        
        st.plotly_chart(
            WeatherVisualizer.create_hourly_chart(st.session_state.forecast_data, selected_date),
            use_container_width=True,
            key="hourly_chart"
        )
        
        # Detailed forecast table
        with st.expander("📋 Detailed 7-Day Forecast Table"):
            forecast_table = []
            for day in st.session_state.forecast_data['forecast']['forecastday']:
                forecast_table.append({
                    'Date': day['date'],
                    'Condition': day['day']['condition']['text'],
                    'Max Temp (°C)': day['day']['maxtemp_c'],
                    'Min Temp (°C)': day['day']['mintemp_c'],
                    'Precipitation (mm)': day['day']['totalprecip_mm'],
                    'Rain Chance (%)': day['day']['daily_chance_of_rain'],
                    'Max Wind (km/h)': day['day']['maxwind_kph'],
                    'UV Index': day['day']['uv'],
                    'Sunrise': day['astro']['sunrise'],
                    'Sunset': day['astro']['sunset']
                })
            
            df = pd.DataFrame(forecast_table)
            st.dataframe(df, use_container_width=True, hide_index=True)
    
    else:
        st.error(f"Unable to fetch weather data for '{st.session_state.location}'. Please check the location name and try again.")
        st.info("Try searching for a different location using the sidebar.")

else:
    # Show configuration help
    st.warning("### ⚙️ Configuration Required")
    st.markdown("""
    This application requires API keys to function. Please configure the following:
    
    #### Steps to Configure:
    
    1. **Create `.env` file** in the project directory
    2. **Copy contents** from `.env.example`
    3. **Add your API keys:**
       - Get WeatherAPI key from [weatherapi.com](https://www.weatherapi.com/signup.aspx)
       - Get Gemini AI key from [Google AI Studio](https://aistudio.google.com/app/apikey)
    4. **Restart the application**
    
    #### Example `.env` file:
    ```
    WEATHERAPI_KEY=your_actual_weatherapi_key
    GEMINI_API_KEY=your_actual_gemini_key
    ```
    """)
    
    st.info("""
    **Both services offer free tiers:**
    - WeatherAPI.com: 1,000,000 calls/month free
    - Google Gemini: Generous free tier available
    """)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; padding: 1rem;">'
    'Powered by WeatherAPI.com & Google Gemini AI | Built with Streamlit'
    '</div>',
    unsafe_allow_html=True
)
