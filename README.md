# Tegallmembar - Digital Clock with Timezone Support

A beautiful digital clock web application that displays the current time in different time zones around the world. Fully deployed on Heroku!

## 🌟 Features

✨ **Features:**
- 🌍 Display time in 10+ different time zones
- 🎨 Modern, responsive UI with gradient background and glassmorphism
- ⚡ Real-time updates every second
- 📱 Mobile-friendly design
- 🔌 REST API endpoints for time data
- 🚀 Ready for Heroku deployment
- 💚 Health check endpoint for monitoring
- 🎯 Easy timezone management

## 📍 Supported Time Zones

- **UTC** - Coordinated Universal Time
- **EST** - Eastern Standard Time (New York)
- **CST** - Central Standard Time (Chicago)
- **MST** - Mountain Standard Time (Denver)
- **PST** - Pacific Standard Time (Los Angeles)
- **GMT** - Greenwich Mean Time (London)
- **CET** - Central European Time (Paris)
- **IST** - Indian Standard Time (India)
- **JST** - Japan Standard Time (Tokyo)
- **AEST** - Australian Eastern Standard Time (Sydney)

## 🚀 Quick Start - Local Development

### 1. Clone the repository
```bash
git clone https://github.com/Vhal999Vhal999/Tegallmembar.git
cd Tegallmembar
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run locally
```bash
python tegallmembar/app.py
```

### 5. Open in browser
```
http://localhost:5000
```

## 🌐 Heroku Deployment

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git repository initialized

### Step 1: Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Create Heroku App
```bash
heroku create your-app-name
```

### Step 4: Deploy from Git
```bash
git push heroku main
```

Or if your branch is named `master`:
```bash
git push heroku master
```

### Step 5: View Live App
```bash
heroku open
```

Your app will be live at: `https://your-app-name.herokuapp.com`

### Monitor Logs
```bash
heroku logs --tail
```

## 📡 API Endpoints

### Get all times
```
GET /api/time
```

**Response:**
```json
{
  "UTC": {
    "time": "14:30:45",
    "date": "2026-07-19",
    "timezone": "UTC"
  },
  "EST": {
    "time": "10:30:45",
    "date": "2026-07-19",
    "timezone": "America/New_York"
  }
}
```

### Get time for specific timezone
```
GET /api/time/<TIMEZONE>
```

**Example:**
```
GET /api/time/EST
```

**Response:**
```json
{
  "EST": {
    "time": "10:30:45",
    "date": "2026-07-19",
    "timezone": "America/New_York"
  }
}
```

### Get available timezones
```
GET /api/timezones
```

### Health check
```
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "service": "Tegallmembar Digital Clock"
}
```

## 📁 Project Structure

```
Tegallmembar/
├── README.md                    # Documentation
├── Procfile                      # Heroku configuration
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
├── tegallmembar/
│   ├── __init__.py              # Main package
│   ├── app.py                   # Flask web application
│   ├── clock.py                 # Digital clock logic
│   └── template.py              # HTML templates
└── templates/
    └── clock.html               # Web UI template
```

## 🛠️ Configuration

### Add Custom Time Zone
Edit `TIME_ZONES` dictionary in `tegallmembar/app.py`:

```python
TIME_ZONES = {
    'YourTZ': 'Continent/City',
    'UTC': 'UTC',
    # ... more timezones
}
```

Find all available timezone strings: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

## 🎨 UI Features

- **Gradient Background**: Beautiful blue gradient
- **Glassmorphism Design**: Frosted glass effect on cards
- **Responsive Grid**: Auto-fits to screen size
- **Hover Effects**: Cards lift on hover
- **Real-time Updates**: Updates every second
- **Mobile Optimized**: Looks great on all devices

## 🔧 Technologies Used

- **Python 3.6+** - Programming language
- **Flask 2.0+** - Web framework
- **Pytz** - Timezone support
- **Gunicorn** - WSGI HTTP Server
- **Heroku** - Cloud platform
- **HTML5/CSS3** - Frontend
- **JavaScript** - Real-time updates

## 📊 Environment Variables

Heroku automatically provides:
- `PORT` - The port to run on

## 🚨 Troubleshooting

### App Crashes on Heroku
```bash
heroku logs --tail
```

### Port Issues
The app automatically uses the `PORT` environment variable from Heroku.

### Timezone Not Found
Verify the timezone string is in the pytz database.

## 🌟 Future Enhancements

- [ ] User customizable timezone list
- [ ] 12-hour/24-hour format toggle
- [ ] Sound alerts for specific times
- [ ] Multiple clock themes
- [ ] Add/remove timezones via web UI
- [ ] Save preferences to local storage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created by **Vhal999Vhal999**

---

**Made with ❤️ by Vhal999Vhal999**

Happy timekeeping! ⏰
