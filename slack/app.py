from json import dumps
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import asyncio

from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

import os
from dotenv import load_dotenv
load_dotenv()


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
event_adapter = SlackEventAdapter(
    os.getenv("SLACK_SIGNING_SECRET"), "/slack/events", app)

# Initialize a Web API client
client = WebClient(token=os.getenv('SLACK_TOKEN'))

# Initializing RASA Model
agent = Agent.load("../chatbot/models/20200329-024355")


@event_adapter.on("message")
# @event_adapter.on("message.im")
def message(payload):
    """
    Response to message
    """
    channel = payload['event']['channel']
    query = payload['event']['text']

    if payload['event'].get('bot_id') == None:
        result = asyncio.run(agent.handle_text(query))
        response = ''
        for d in result:
            response += (d['text'] + '\n')
        client.chat_postMessage(text=response, channel=channel)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
