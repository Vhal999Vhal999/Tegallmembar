"""Flask web app for digital clock with timezone support."""

from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz
import os

app = Flask(__name__, template_folder='../templates')

# Define time zones
TIME_ZONES = {
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
}

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
    return jsonify({'status': 'ok', 'service': 'Tegallmembar Digital Clock'}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
