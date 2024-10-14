from flask import Blueprint, request, jsonify
from flasgger import swag_from
from middleware.auth import auth_token

todos_bp = Blueprint('todos', __name__)

todos = []

@todos_bp.before_request
def before_request():
    return auth_token()

@todos_bp.route('/todos', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of todos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'task': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_todos():
    """Get all todos
    ---
    tags:
      - Todos
    """
    return jsonify(todos)

@todos_bp.route('/todos', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'description': 'Todo to add',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'task': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Todo created',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'task': {'type': 'string'}
                }
            }
        }
    }
})
def add_todo():
    """Add a new todo
    ---
    tags:
      - Todos
    """
    todo = request.json
    todos.append(todo)
    return jsonify(todo), 201

@todos_bp.route('/todos/<int:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'description': 'ID of the todo to update',
            'in': 'path',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'body',
            'description': 'Updated todo',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'task': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Todo updated',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'task': {'type': 'string'}
                }
            }
        }
    }
})
def update_todo(id):
    """Update a todo by ID
    ---
    tags:
      - Todos
    """
    todo = request.json
    todos[id] = todo
    return jsonify(todo)

@todos_bp.route('/todos/<int:id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'description': 'ID of the todo to delete',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Todo deleted',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'task': {'type': 'string'}
                }
            }
        }
    }
})
def delete_todo(id):
    """Delete a todo by ID
    ---
    tags:
      - Todos
    """
    todo = todos.pop(id)
    return jsonify(todo)
