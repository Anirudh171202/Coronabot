# from flask import Flask
# from slackeventsapi import SlackEventAdapter


# import os
# from dotenv import load_dotenv
# load_dotenv()

# SLACK_TOKEN = os.getenv('SLACK_TOKEN')
# SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
# print(SLACK_SIGNING_SECRET)

# # This `app` represents your existing Flask app
# app = Flask(__name__)


# # An example of one of your Flask app's routes
# @app.route("/")
# def hello():
#     return "Hello there!"


# # Bind the Events API route to your existing Flask app by passing the server
# # instance as the last param, or with `server=app`.
# slack_events_adapter = SlackEventAdapter(
#     SLACK_SIGNING_SECRET, "/slack/events")


# # Create an event listener
# @slack_events_adapter.on("message")
# def reaction_added(event_data):
#     print('Hi')


# # Start the server on port 3000
# if __name__ == "__main__":
#     app.run(port=3000, debug=True)

import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi

import os
from dotenv import load_dotenv
load_dotenv()

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    os.getenv("SLACK_SIGNING_SECRET"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.getenv('SLACK_TOKEN'))


# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
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
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000, debug=True)
