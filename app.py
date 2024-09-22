from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define your routes as before
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get("data", [])
    file_b64 = request.json.get("file_b64", None)

    # Process data
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lower = max([ch for ch in alphabets if ch.islower()], default=None)

    # Validate file
    file_valid = file_b64 is not None
    file_mime_type = "unknown" if file_valid else None
    file_size_kb = len(file_b64) / 1024 if file_valid else 0

    # Mock user info
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lower] if highest_lower else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({
        "operation_code": 1
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
