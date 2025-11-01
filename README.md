# Advanced Industrial-Grade AI Weather Prediction System

![Weather AI System](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

A professional, industrial-level AI weather prediction system that provides real-world weather forecasts with Gemini AI integration and a sophisticated Streamlit interface. This system delivers enterprise-grade functionality with advanced ML-powered weather analysis.

## Features

### Core Functionality
- **Real-Time Weather Data**: Integration with WeatherAPI.com for accurate global weather data
- **AI-Powered Analysis**: Google Gemini AI for intelligent weather pattern analysis and insights
- **7-Day Forecasts**: Comprehensive weather predictions with hourly breakdowns
- **Weather Anomaly Detection**: Automatic detection of unusual weather patterns
- **Global Location Support**: Search and track weather for any location worldwide

### Advanced Features
- **Professional Data Visualization**: Interactive charts using Plotly
  - Temperature trends (max/min/average)
  - Precipitation forecasts
  - Wind speed analysis
  - Weather conditions distribution
  - Hourly forecasts
- **AI Insights**:
  - Current weather analysis
  - 7-day forecast interpretation
  - Activity recommendations
  - Anomaly impact analysis
- **Weather Alerts**: Automatic alerts for:
  - Extreme temperatures
  - High wind speeds
  - Heavy precipitation
  - High UV index

### Professional Design
- Industrial-grade color scheme (blues and grays)
- Responsive layout for desktop and mobile
- Professional data visualization components
- Clean, modern typography
- Accessible design (WCAG compliant)

## Screenshots

### Main Dashboard
![Dashboard](docs/images/dashboard_preview.png)

### AI Analysis
![AI Analysis](docs/images/ai_analysis_preview.png)

## Technology Stack

- **Frontend**: Streamlit 1.51.0
- **Visualization**: Plotly 6.3.1
- **Data Processing**: Pandas 2.3.3
- **Weather API**: WeatherAPI.com
- **AI Engine**: Google Gemini AI
- **Language**: Python 3.12+

## Prerequisites

- Python 3.12 or higher
- WeatherAPI.com API key (free tier: 1M calls/month)
- Google Gemini AI API key (free tier available)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd weather_ai_system
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
```env
WEATHERAPI_KEY=your_weatherapi_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

#### Getting API Keys

**WeatherAPI.com**:
1. Visit [https://www.weatherapi.com/signup.aspx](https://www.weatherapi.com/signup.aspx)
2. Sign up for a free account
3. Copy your API key from the dashboard
4. Free tier includes: 1,000,000 calls/month, global coverage, 14-day forecasts

**Google Gemini AI**:
1. Visit [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key
5. Free tier includes: Generous request limits for testing and development

## Running the Application

### Local Development

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Production Deployment

```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

## Usage Guide

### Basic Usage

1. **Search Location**: Enter a city name in the sidebar and click "Search Weather"
2. **View Current Conditions**: See real-time weather data in the main dashboard
3. **Explore AI Analysis**: Navigate through AI-powered insights in the tabs
4. **Check Forecasts**: View 7-day forecasts with interactive visualizations
5. **Monitor Alerts**: Review detected weather anomalies and warnings

### Advanced Features

**Hourly Forecast**:
- Select a date from the dropdown to view hourly weather predictions
- Interactive charts show temperature, precipitation, and feels-like temperature

**Weather Anomalies**:
- System automatically detects unusual weather patterns
- AI provides context and recommendations for anomalies

**Activity Recommendations**:
- AI generates personalized activity suggestions based on current conditions
- Recommendations consider temperature, precipitation, UV index, and more

## Project Structure

```
weather_ai_system/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration and settings
├── weather_api.py         # WeatherAPI.com integration
├── gemini_ai.py           # Gemini AI integration
├── visualizations.py      # Plotly charts and visualizations
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
├── .env                   # Your actual environment configuration (gitignored)
├── .streamlit/
│   └── config.toml        # Streamlit theme configuration
└── README.md              # This file
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `WEATHERAPI_KEY` | WeatherAPI.com API key | Yes | - |
| `GEMINI_API_KEY` | Google Gemini AI API key | Yes | - |

### Application Settings

Edit `config.py` to customize:
- Default location
- Forecast days (3-14)
- Cache TTL
- Weather alert thresholds
- Gemini AI parameters

## API Rate Limits

### WeatherAPI.com (Free Tier)
- **Calls**: 1,000,000 per month
- **Rate**: No specific limit
- **Features**: Current weather, 14-day forecast, historical data, alerts

### Google Gemini AI (Free Tier)
- **Requests**: Generous free tier
- **Rate**: 60 requests per minute
- **Context**: Up to 2M tokens

## Troubleshooting

### Common Issues

**API Keys Not Working**:
- Ensure `.env` file is in the project root directory
- Verify API keys are copied correctly (no extra spaces)
- Restart the application after modifying `.env`

**Location Not Found**:
- Try different location formats (city name, coordinates, postal code)
- Use full location names (e.g., "New York, USA" instead of "NY")

**Slow AI Responses**:
- This is normal for complex analyses
- Gemini AI may take 2-5 seconds for detailed insights
- Consider reducing Gemini temperature for faster responses

**Charts Not Loading**:
- Check internet connection (Plotly requires external resources)
- Clear browser cache
- Restart the Streamlit application

### Error Messages

```
Error: WEATHERAPI_KEY is not configured
```
**Solution**: Add your WeatherAPI key to the `.env` file

```
Error: GEMINI_API_KEY is not configured
```
**Solution**: Add your Gemini AI key to the `.env` file

```
Error fetching weather data
```
**Solution**: Check API key validity and internet connection

## Performance Optimization

- **Caching**: Weather data is cached for 10 minutes by default
- **Lazy Loading**: AI analysis is generated on-demand
- **Efficient API Calls**: Minimal API requests with smart data reuse

## Security

- API keys are stored in `.env` file (never commit to version control)
- `.env` is included in `.gitignore`
- XSRF protection enabled
- No sensitive data stored in browser

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Acknowledgments

- **WeatherAPI.com** for providing comprehensive weather data
- **Google Gemini AI** for powerful AI analysis capabilities
- **Streamlit** for the excellent web framework
- **Plotly** for professional data visualizations

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [Your Contact Information]

## Roadmap

### Future Enhancements
- [ ] Historical weather data analysis
- [ ] Weather comparison between locations
- [ ] Custom alert configuration
- [ ] Export forecast data (PDF/CSV)
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Weather widgets for embedding
- [ ] Advanced ML models for prediction

## Version History

### v1.0.0 (2025-11-01)
- Initial release
- Real-time weather data integration
- Gemini AI analysis
- Professional data visualizations
- Weather anomaly detection
- 7-day forecasts with hourly breakdowns

---

**Built with ❤️ for professional weather forecasting**
