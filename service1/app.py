from flask import Flask, jsonify, request
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from ariadne.wsgi import GraphQL
from service1.schema import schema

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data)
    return jsonify(result), 200 if success else 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
