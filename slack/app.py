from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

import os
from dotenv import load_dotenv
load_dotenv()

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    os.getenv("SLACK_SIGNING_SECRET"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.getenv('SLACK_TOKEN'))


@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    print(payload)


@slack_events_adapter.on("message.im")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    print(payload)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
