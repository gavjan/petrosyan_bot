import discord


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
    if message.author == client.user:
        return
    if message.content.startswith("./hello"):
        await message.channel.send("Hello!")
    if message.content.startswith("./restart_tiko"):
        exit(0)
    if message.content.startswith("./test_err"):
        exit(0/0)


client.run(BOT_TOKEN)
