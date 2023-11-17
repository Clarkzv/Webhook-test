from flask import Flask, request
import requests

app = Flask(__name__)

# Endpoint to receive data
@app.route('/receive', methods=['POST'])
def receive():
    body = request.get_data()  # Get the body
    headers = dict(request.headers)  # Get the headers

    # Send the received data to the Discord webhook
    webhook_url = 'http://discord.com/api/webhooks/1118554895058997380/l7QmCpUQB8ss0984bDEIvM1ef1hkTvYJG31H2prbTkZGA9vtZ9qdlRjkW3_KzRJBvk0p'
    response = requests.post(webhook_url, data=body, headers=headers)

    if response.status_code == 200:
        return "Data sent to webhook successfully"
    else:
        return "Failed to send data to webhook"

if __name__ == '__main__':
    app.run(debug=True, port=8082)
