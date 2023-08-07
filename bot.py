import discord
import time

TOKEN = "token"
channel_id = channel_id

client = discord.Client(intents=discord.Intents.all())
pings = 0

async def ping():
    channel = client.get_channel(channel_id)
    await channel.send(f"<@&role_id>, PINGEBIS RAODENOBA: {pings}")

@client.event
async def on_ready():
    global pings
    print(f"Logged in.")
    while True:
        await ping()
        pings = pings + 1

        print(f"SAHIRA MOIPINGA {pings}-JER")
        time.sleep(2)

client.run(TOKEN)
