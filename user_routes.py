from flask import Blueprint, request, jsonify
from datetime import datetime
import json

user_bp = Blueprint('user', __name__)

# Simple in-memory user storage for demo
users = {}

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        'users': list(users.values()),
        'count': len(users),
        'timestamp': datetime.now().isoformat()
    })

@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        user_id = data.get('id') or str(len(users) + 1)
        
        user = {
            'id': user_id,
            'name': data.get('name', ''),
            'email': data.get('email', ''),
            'role': data.get('role', 'user'),
            'created_at': datetime.now().isoformat(),
            'last_login': None
        }
        
        users[user_id] = user
        
        return jsonify({
            'user': user,
            'message': 'User created successfully'
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({'user': user})

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        if user_id not in users:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.json
        user = users[user_id]
        
        # Update user fields
        if 'name' in data:
            user['name'] = data['name']
        if 'email' in data:
            user['email'] = data['email']
        if 'role' in data:
            user['role'] = data['role']
        
        user['updated_at'] = datetime.now().isoformat()
        
        return jsonify({
            'user': user,
            'message': 'User updated successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    del users[user_id]
    return jsonify({'message': 'User deleted successfully'})

@user_bp.route('/users/<user_id>/login', methods=['POST'])
def user_login(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    user = users[user_id]
    user['last_login'] = datetime.now().isoformat()
    
    return jsonify({
        'user': user,
        'message': 'Login successful'
    })