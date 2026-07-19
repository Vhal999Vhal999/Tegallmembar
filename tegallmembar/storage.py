"""Data storage utilities."""

import json
import os
from datetime import datetime

class DataStore:
    """Simple JSON-based data storage."""
    
    def __init__(self, data_dir='./data'):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.users_file = os.path.join(data_dir, 'users.json')
        self.alarms_file = os.path.join(data_dir, 'alarms.json')
        self.favorites_file = os.path.join(data_dir, 'favorites.json')
        self._init_files()
    
    def _init_files(self):
        """Initialize data files if they don't exist."""
        for file_path in [self.users_file, self.alarms_file, self.favorites_file]:
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    json.dump({}, f)
    
    def save_user(self, user_data):
        """Save user data."""
        users = self._load_json(self.users_file)
        users[user_data['user_id']] = user_data
        self._save_json(self.users_file, users)
    
    def get_user(self, user_id):
        """Get user by ID."""
        users = self._load_json(self.users_file)
        return users.get(user_id)
    
    def get_user_by_email(self, email):
        """Get user by email."""
        users = self._load_json(self.users_file)
        for user in users.values():
            if user.get('email') == email:
                return user
        return None
    
    def save_alarm(self, alarm_data):
        """Save alarm data."""
        alarms = self._load_json(self.alarms_file)
        alarms[alarm_data['alarm_id']] = alarm_data
        self._save_json(self.alarms_file, alarms)
    
    def get_user_alarms(self, user_id):
        """Get all alarms for a user."""
        alarms = self._load_json(self.alarms_file)
        return [a for a in alarms.values() if a.get('user_id') == user_id]
    
    def delete_alarm(self, alarm_id):
        """Delete an alarm."""
        alarms = self._load_json(self.alarms_file)
        if alarm_id in alarms:
            del alarms[alarm_id]
            self._save_json(self.alarms_file, alarms)
            return True
        return False
    
    def save_favorite(self, favorite_data):
        """Save favorite timezone."""
        favorites = self._load_json(self.favorites_file)
        favorites[favorite_data['favorite_id']] = favorite_data
        self._save_json(self.favorites_file, favorites)
    
    def get_user_favorites(self, user_id):
        """Get all favorite timezones for a user."""
        favorites = self._load_json(self.favorites_file)
        return [f for f in favorites.values() if f.get('user_id') == user_id]
    
    def delete_favorite(self, favorite_id):
        """Delete a favorite."""
        favorites = self._load_json(self.favorites_file)
        if favorite_id in favorites:
            del favorites[favorite_id]
            self._save_json(self.favorites_file, favorites)
            return True
        return False
    
    @staticmethod
    def _load_json(file_path):
        """Load JSON file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    
    @staticmethod
    def _save_json(file_path, data):
        """Save JSON file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
