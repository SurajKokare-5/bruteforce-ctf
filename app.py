from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "michel"  # Weak password for the challenge

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == USERNAME and password == PASSWORD:
        return jsonify({"message": "Login successful! Flag: CTF{You Got The Flag}"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
