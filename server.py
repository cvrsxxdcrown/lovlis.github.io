from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/run-code', methods=['GET'])
def run_code():
    try:
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True, check=True)
        return result.stdout 
    except subprocess.CalledProcessError as e:
        return f"Ошибка при выполнении кода: {e.stderr}", 400

@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
