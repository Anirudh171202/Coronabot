from json import dumps
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import asyncio

from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

from googletrans import Translator

import os
from dotenv import load_dotenv
load_dotenv()


def translate(text, lang='en'):
    trans = Translator()
    t = trans.translate(text, lang)
    res = t.text
    src = t.src
    return res, src


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
event_adapter = SlackEventAdapter(
    os.getenv("SLACK_SIGNING_SECRET"), "/slack/events", app)

# Initialize a Web API client
client = WebClient(token=os.getenv('SLACK_TOKEN'))

# Initializing RASA Model
agent = Agent.load("../chatbot/models/20200329-144319")

# Store most recent event ids
event_ids = set()


@event_adapter.on("message")
# @event_adapter.on("message.im")
def message(payload):
    """
    Response to message
    """
    channel = payload['event']['channel']
    query = payload['event']['text']

    res, src = translate(query)

    if payload['event'].get('bot_id') == None:
        if payload['event_id'] not in event_ids:
            event_ids.add(payload['event_id'])
            print(dumps(payload, indent=True))
            result = asyncio.run(agent.handle_text(res))
            response = ''
            for d in result:
                response += translate(d['text'], src)[0] + '\n'
            client.chat_postMessage(text=response, channel=channel)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
