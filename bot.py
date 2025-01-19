import discord
import requests
import json

# update the url to https://meme-api.com/gimme
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# create intents keyword argument
intents = discord.Intents.default()
intents.message_content = True

# update the call here by passing the 'intents' keyword argument
client = MyClient(intents=intents)
client.run('MTMzMDEwODQ2MDY4MzEwMDE4MA.GkfHrH.wVehY2vWzQsTdjsYUNpcAvApWh7WWGGVY9-jUE')