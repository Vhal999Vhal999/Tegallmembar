"""Database models for Tegallmembar."""

from datetime import datetime
import json

# Simple JSON-based storage (no database required)
class User:
    """User model for storing preferences."""
    
    def __init__(self, user_id, username, email, password_hash):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.favorites = []
        self.alarms = []
        self.preferences = {
            'theme': 'dark',
            'time_format': '24h',
            'notifications': True
        }
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'favorites': self.favorites,
            'alarms': self.alarms,
            'preferences': self.preferences,
            'created_at': self.created_at
        }


class Alarm:
    """Alarm model."""
    
    def __init__(self, alarm_id, user_id, time, timezone, label, enabled=True):
        self.alarm_id = alarm_id
        self.user_id = user_id
        self.time = time  # HH:MM format
        self.timezone = timezone
        self.label = label
        self.enabled = enabled
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert alarm to dictionary."""
        return {
            'alarm_id': self.alarm_id,
            'user_id': self.user_id,
            'time': self.time,
            'timezone': self.timezone,
            'label': self.label,
            'enabled': self.enabled,
            'created_at': self.created_at
        }


class Favorite:
    """Favorite timezone model."""
    
    def __init__(self, favorite_id, user_id, timezone_code, timezone_name):
        self.favorite_id = favorite_id
        self.user_id = user_id
        self.timezone_code = timezone_code
        self.timezone_name = timezone_name
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert favorite to dictionary."""
        return {
            'favorite_id': self.favorite_id,
            'user_id': self.user_id,
            'timezone_code': self.timezone_code,
            'timezone_name': self.timezone_name,
            'created_at': self.created_at
        }
