from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_data():
    data = request.json
    receiver_urls = [
        'http://receiver1:5001/receive',
        'http://receiver2:5002/receive'
    ]
    responses = {}
    for url in receiver_urls:
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                responses[url] = "Data received successfully"
            else:
                responses[url] = f"Failed to send data: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            responses[url] = f"Error sending data: {str(e)}"
    return jsonify(responses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)