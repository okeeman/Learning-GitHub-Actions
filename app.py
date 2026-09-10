from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """Simple home route."""
    return jsonify(message="Hello, Flask!")

@app.route("/add", methods=["GET"])
def add_numbers():
    """
    Adds two numbers passed as query parameters: /add?a=5&b=3
    Returns JSON with the result.
    """
    try:
        a = request.args.get("a", type=float)
        b = request.args.get("b", type=float)

        if a is None or b is None:
            return jsonify(error="Both 'a' and 'b' query parameters are required."), 400

        return jsonify(result=a + b)
    except ValueError:
        return jsonify(error="Invalid number format."), 400


if __name__ == "__main__":
    app.run(debug=True)
