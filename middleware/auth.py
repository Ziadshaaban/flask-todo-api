from flask import Flask, request, jsonify

Token = "my_secret_token"

def auth_token():
    token = request.headers.get('Authorization')
    if not token or token != Token:
        return jsonify({'error': 'Unauthorized'}), 401