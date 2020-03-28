from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

import os
from dotenv import load_dotenv
load_dotenv()

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
event_adapter = SlackEventAdapter(
    os.getenv("SLACK_SIGNING_SECRET"), "/slack/events", app)

# Initialize a Web API client
client = WebClient(token=os.getenv('SLACK_TOKEN'))


@event_adapter.on("message")
@event_adapter.on("message.im")
def message(payload):
    """
    Display 
    """
    channel = payload['event']['channel']
    text = "Hello, World!"
    client.chat_postMessage(text=text, channel=channel)
    print(text)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
