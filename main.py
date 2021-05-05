from __future__ import print_function
import discord
import sys

ADMIN_ID = 213341816324489217

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_env(name):
    f = open(f".env/{name}", "r")
    val = f.read()
    f.close()
    return val


BOT_TOKEN = get_env("bot_token")

client = discord.Client()


@client.event
async def on_ready():
    print(f"logged in as {client}")


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        if message.content.startswith("./hello"):
            await message.channel.send(message.author.id == ADMIN_ID)
        if message.content.startswith("./restart_tiko"):
            exit(0)
        if message.content.startswith("./test_err"):
            tmp = 0 / 0

    except Exception as e:
        eprint(e)
        exit(1)


client.run(BOT_TOKEN)
