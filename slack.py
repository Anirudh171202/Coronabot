import os
import slack
slack_token = os.environ["xoxb-1021109435873-1032579478213-LfqXw0tPhWZuvqrsXVtMF0Ea"]
client = slack.WebClient(token=slack_token)

client.chat_postMessage(
  channel="U010WV4JH0C",
  text="Hello from your app! :tada:"
)