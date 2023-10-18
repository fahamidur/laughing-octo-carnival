from flask import Flask, render_template, request, jsonify
import requests
import time
import json
from config import API_URL, HEADERS  # Import API URL and headers from config file

app = Flask(__name__)

def query(payload):
    max_retries = 5
    retries = 0

    while retries < max_retries:
        response = requests.post(API_URL, headers=HEADERS, json=payload)  # Use imported values
        
        if response.status_code == 200:
            return response.json()
        
        retries += 1
        time.sleep(10)  # Wait for a while before retrying

    return {"error": "Failed to get a valid response after multiple retries"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def process_query():
    input_text = request.form['input_text']
    output = query({
        "inputs": input_text,
    })
    response_data = output[0]['generated_text']
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
