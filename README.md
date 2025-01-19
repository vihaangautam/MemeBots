# Discord Meme Bot

A simple Discord bot that responds with a random meme when the $meme command is used. The bot fetches memes using the Meme API and sends a meme link in the chat.

##Features
Responds to the $meme command with a random meme link.
Fetches memes from the Meme API.
Built using discord.py and requests.

##Prerequisites
Before running the bot, make sure you have the following:
Python 3.6+ installed on your machine.
A Discord bot token (see Discord Developer Portal to create one).

##Libraries required for the project:
discord.py
requests
python-dotenv

##Install required libraries:
You can install the necessary libraries using pip:
py -3 -m pip install discord.py requests python-dotenv

##Create a .env file in the project directory to store your bot token securely:
DISCORD_TOKEN=your-bot-token-here

##Usage
In any Discord text channel where the bot is present, type:
$meme
The bot will reply with a random meme link.
