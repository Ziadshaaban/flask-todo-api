from flask import Flask, request, jsonify
from routes.todos import todos_bp
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app) 

app.register_blueprint(todos_bp)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(port=5000)