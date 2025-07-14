from datetime import datetime
from typing import Dict, List, Optional
import json

class User:
    def __init__(self, user_id: str, name: str, email: str, role: str = 'user'):
        self.id = user_id
        self.name = name
        self.email = email
        self.role = role
        self.created_at = datetime.now().isoformat()
        self.updated_at = None
        self.last_login = None
        self.preferences = {}
        self.projects = []
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'last_login': self.last_login,
            'preferences': self.preferences,
            'projects': self.projects
        }
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now().isoformat()
    
    def add_project(self, project_id: str):
        if project_id not in self.projects:
            self.projects.append(project_id)
            self.updated_at = datetime.now().isoformat()
    
    def remove_project(self, project_id: str):
        if project_id in self.projects:
            self.projects.remove(project_id)
            self.updated_at = datetime.now().isoformat()
    
    def set_preference(self, key: str, value):
        self.preferences[key] = value
        self.updated_at = datetime.now().isoformat()
    
    def get_preference(self, key: str, default=None):
        return self.preferences.get(key, default)
    
    def login(self):
        self.last_login = datetime.now().isoformat()

class UserManager:
    def __init__(self):
        self.users: Dict[str, User] = {}
    
    def create_user(self, user_id: str, name: str, email: str, role: str = 'user') -> User:
        if user_id in self.users:
            raise ValueError(f"User with id {user_id} already exists")
        
        user = User(user_id, name, email, role)
        self.users[user_id] = user
        return user
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def get_all_users(self) -> List[User]:
        return list(self.users.values())
    
    def update_user(self, user_id: str, **kwargs) -> Optional[User]:
        user = self.get_user(user_id)
        if user:
            user.update(**kwargs)
        return user
    
    def delete_user(self, user_id: str) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
    
    def user_exists(self, user_id: str) -> bool:
        return user_id in self.users
    
    def get_users_by_role(self, role: str) -> List[User]:
        return [user for user in self.users.values() if user.role == role]
    
    def search_users(self, query: str) -> List[User]:
        results = []
        query_lower = query.lower()
        
        for user in self.users.values():
            if (query_lower in user.name.lower() or 
                query_lower in user.email.lower() or 
                query_lower in user.role.lower()):
                results.append(user)
        
        return results

# Global user manager instance
user_manager = UserManager()