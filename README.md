# flask-webhook
This is a simple Flask application that listens for incoming webhook requests (from twilio) and returns the payload.

To run the app on development server, run the following
```
flask --app twilio-webhook run
```
To expose the local development server on a certain port, run the following
```
ngrok http 5000
```
