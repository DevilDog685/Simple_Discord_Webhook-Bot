import requests

webhook_url = input("Enter Discord webhook URL: ")
message_type = input("Is this a giveaway or an announcement? ")
title = input("Enter the title of the message: ")
description = input("Enter the description of the message: ")

# Format the message with Markdown and Emoji based on the message type
if message_type.lower() == "giveaway":
    formatted_title = f"**{title}** :tada:\n"
    formatted_description = f"\n:gift: {description}"
else:
    formatted_title = f"**{title}** :loudspeaker:\n"
    formatted_description = f"\n{description}"

formatted_message = formatted_title + formatted_description

payload = {"content": formatted_message}
response = requests.post(webhook_url, json=payload)

if response.status_code == 204:
    print("Message sent successfully!")
else:
    print("Error sending message. Status code:", response.status_code)

