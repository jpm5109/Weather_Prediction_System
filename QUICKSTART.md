# Quick Setup Guide

## Getting Started in 5 Minutes

### Step 1: Install Dependencies
```bash
cd weather_ai_system
pip install -r requirements.txt
```

### Step 2: Get Your Free API Keys

#### WeatherAPI.com (1M free calls/month)
1. Go to https://www.weatherapi.com/signup.aspx
2. Sign up with your email
3. Copy your API key from the dashboard

#### Google Gemini AI (Free tier)
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the generated key

### Step 3: Configure Environment
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys
# Use any text editor (nano, vim, vscode, etc.)
nano .env
```

Your `.env` file should look like:
```env
WEATHERAPI_KEY=1a2b3c4d5e6f7g8h9i0j
GEMINI_API_KEY=AIzaSyABC123...
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The app will automatically open in your browser at http://localhost:8501

## First Use

1. **Configuration Check**: The app will show API status in the sidebar
2. **Search Location**: Enter any city name (e.g., "London", "New York", "Tokyo")
3. **Explore Features**:
   - Current weather conditions
   - AI-powered weather analysis
   - 7-day forecasts with charts
   - Weather alerts
   - Activity recommendations

## Troubleshooting

### "API key not configured"
- Make sure `.env` file exists in the project root
- Check that API keys don't have extra spaces
- Restart the application after editing `.env`

### "Location not found"
- Try full city name with country (e.g., "Paris, France")
- Use coordinates format: "40.7128,-74.0060"

### Charts not displaying
- Check internet connection
- Refresh the page (F5)
- Clear browser cache

## Need Help?

Refer to the main README.md for detailed documentation and advanced features.
