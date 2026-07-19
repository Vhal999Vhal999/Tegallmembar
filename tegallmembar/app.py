"""Updated Flask app with config integration."""

from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz
import os
from tegallmembar.config import get_config

# Initialize Flask app
app = Flask(__name__, template_folder='../templates')

# Load configuration
config = get_config()
app.config.from_object(config)

# Get timezones from config
TIME_ZONES = app.config.get('TIMEZONES', {
    'UTC': 'UTC',
    'EST': 'America/New_York',
    'CST': 'America/Chicago',
    'MST': 'America/Denver',
    'PST': 'America/Los_Angeles',
    'GMT': 'Europe/London',
    'CET': 'Europe/Paris',
    'IST': 'Asia/Kolkata',
    'JST': 'Asia/Tokyo',
    'AEST': 'Australia/Sydney',
})

@app.route('/')
def index():
    """Display digital clock with all time zones."""
    times = {}
    for name, tz_string in TIME_ZONES.items():
        tz = pytz.timezone(tz_string)
        current_time = datetime.now(tz)
        times[name] = {
            'time': current_time.strftime('%H:%M:%S'),
            'date': current_time.strftime('%Y-%m-%d'),
            'timezone': tz_string
        }
    
    return render_template('clock.html', times=times)

@app.route('/api/time')
def api_time():
    """API endpoint for getting all times in JSON format."""
    times = {}
    for name, tz_string in TIME_ZONES.items():
        tz = pytz.timezone(tz_string)
        current_time = datetime.now(tz)
        times[name] = {
            'time': current_time.strftime('%H:%M:%S'),
            'date': current_time.strftime('%Y-%m-%d'),
            'timezone': tz_string
        }
    
    return jsonify(times)

@app.route('/api/time/<timezone>')
def get_timezone_time(timezone):
    """API endpoint for getting time in a specific timezone."""
    tz_upper = timezone.upper()
    
    if tz_upper not in TIME_ZONES:
        return jsonify({'error': f'Timezone {timezone} not found'}), 404
    
    tz_string = TIME_ZONES[tz_upper]
    tz = pytz.timezone(tz_string)
    current_time = datetime.now(tz)
    
    return jsonify({
        tz_upper: {
            'time': current_time.strftime('%H:%M:%S'),
            'date': current_time.strftime('%Y-%m-%d'),
            'timezone': tz_string
        }
    })

@app.route('/api/timezones')
def get_timezones():
    """API endpoint for getting list of available timezones."""
    return jsonify(TIME_ZONES)

@app.route('/health')
def health():
    """Health check endpoint for Heroku."""
    return jsonify({
        'status': 'ok',
        'service': 'Tegallmembar Digital Clock',
        'environment': os.environ.get('FLASK_ENV', 'development')
    }), 200

@app.route('/config')
def get_app_config():
    """Get app configuration info (non-sensitive)."""
    return jsonify({
        'app_name': app.config.get('SECRET_KEY', 'N/A')[:10],
        'debug': app.config.get('DEBUG', False),
        'environment': os.environ.get('FLASK_ENV', 'development'),
        'timezones_count': len(TIME_ZONES)
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Get port from environment variable or config
    port = app.config.get('PORT', 5000)
    host = app.config.get('HOST', '0.0.0.0')
    debug = app.config.get('DEBUG', False)
    
    app.run(host=host, port=port, debug=debug)
