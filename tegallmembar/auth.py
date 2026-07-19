"""Authentication module for Tegallmembar."""

import os
from datetime import datetime, timedelta
import jwt
import hashlib

class AuthManager:
    """Handle user authentication and JWT tokens."""
    
    def __init__(self, secret_key=None):
        self.secret_key = secret_key or os.environ.get('SECRET_KEY', 'default-secret-key')
        self.algorithm = 'HS256'
        self.token_expiry = 24  # hours
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password, password_hash):
        """Verify password against hash."""
        return hashlib.sha256(password.encode()).hexdigest() == password_hash
    
    def generate_token(self, user_id, username):
        """Generate JWT token for user."""
        payload = {
            'user_id': user_id,
            'username': username,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(hours=self.token_expiry)
        }
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token
    
    def verify_token(self, token):
        """Verify JWT token."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return {'error': 'Token expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
    
    def is_token_valid(self, token):
        """Check if token is valid."""
        payload = self.verify_token(token)
        return 'error' not in payload
