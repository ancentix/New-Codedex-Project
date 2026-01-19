import discord
import requests
import json

def send_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self,message):
        if message.author == self.user:
            return
        
        if message.content.startswith('!meme'):
            await message.channel.send(send_meme())

        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello! {message.author.mention}')
    
    async def on_member_join(self,member):
        channel = discord.utils.get(member.guild.text_channels, name = 'general')

        if channel:
            await channel.send(
                f"Welcome {member.mention}!"
            )



            
            
    
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents = intents)
client.run('My Token ')

    
