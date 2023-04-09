# Simple_Discord_Webhook-Bot
This Python code is designed to send a message to a Discord webhook. A webhook is a way to post messages to channels in Discord through an automated program.

The code first prompts the user to enter the Discord webhook URL, message type (either "giveaway" or "announcement"), title of the message, and description of the message.

After the user inputs the necessary information, the code formats the message with Markdown and Emoji based on the message type. If the message type is "giveaway", the title will be formatted with bold text and a tada emoji, while the description will be formatted with a gift emoji. If the message type is "announcement", the title will be formatted with bold text and a loudspeaker emoji, while the description will be formatted as is.

The formatted message is then sent to the Discord webhook using the requests.post() method. The message is sent as a JSON payload with a "content" key containing the formatted message.

Finally, the code checks if the message was sent successfully by checking the status code of the response. If the status code is 204, the message was sent successfully, and the code prints "Message sent successfully!" to the console. If the status code is anything else, the code prints "Error sending message. Status code:" followed by the status code returned by the webhook.
