Discord Meme Bot

A simple Discord bot that responds with a random meme when the $meme command is used. The bot fetches memes using the Meme API and sends a meme link in the chat.

Features

Responds to the $meme command with a random meme link.
Fetches memes from the Meme API.
Built using discord.py and requests.
Prerequisites

Before running the bot, make sure you have the following:

Python 3.6+ installed on your machine.
A Discord bot token (see Discord Developer Portal to create one).
Libraries required for the project:
discord.py
requests
python-dotenv
Installation

Clone the repository or download the files to your local machine.

git clone <repository-url>
cd <project-folder>

Install required libraries:

You can install the necessary libraries using pip:

py -3 -m pip install discord.py requests python-dotenv

Create a .env file in the project directory to store your bot token securely.

.env

DISCORD_TOKEN=your-bot-token-here

Replace your-bot-token-here with your actual Discord bot token.

Running the Bot

Ensure your terminal or command prompt is inside the project directory.

Run the bot using the following command:

python bot.py

The bot should log in and output something like:

Logged on as <your-bot-name>!

Usage

In any Discord text channel where the bot is present, type:

$meme

The bot will reply with a random meme link.
