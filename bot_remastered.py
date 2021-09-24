#Matty bot 2.0
import discord

client = discord.Client()

# token from https://discordapp.com/developers
token = ''

# bot is ready
@client.event
async def on_ready():
    try:
        # print bot information
        print(client.user.name)
        print(client.user.id)
        print('Discord.py Version: {}'.format(discord.__version__))

    except Exception as e:
        print(e)



# start bot
client.run(token)