from flask import Flask, request, jsonify
from urllib.parse import parse_qs


app = Flask(__name__)


# Test Route
@app.route('/', methods=['GET'])
def get_method():
    return jsonify({"Status": "OK", "Message": "Server is OK"})

# Route to handle incoming webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get body of the incoming WA message
    body = dict(request.values)
    body["id"] = body.get("SmsSid")
    print(body)

    # Get the details of the message
    message_body = request.values.get('Body', '')
    sender = request.values.get('From', '')
    recipient = request.values.get('To', '')

    # Print the message details to the console
    print(f"Received a WhatsApp message from {sender} to {recipient}: {message_body}")

    return body

