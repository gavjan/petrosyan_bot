from __future__ import print_function
import discord
import sys
from random import randint

ADMIN_ID = 213341816324489217
KEYWORDS = {"pipi", "pampers", "tigran", "petrosian", "petrosyan"}
DONT_COMMENT_KEYWORD = "!nopipi"

PASTA = """Are you kidding ??? What the **** are you talking about man ? You are a biggest looser i ever seen in my life ! You was doing PIPI in your pampers when i was beating players much more stronger then you! You are not proffesional, because proffesionals knew how to lose and congratulate opponents, you are like a girl crying after i beat you! Be brave, be honest to yourself and stop this trush talkings!!! Everybody know that i am very good blitz player, i can win anyone in the world in single game! And "w"esley "s"o is nobody for me, just a player who are crying every single time when loosing, ( remember what you say about Firouzja ) !!! Stop playing with my name, i deserve to have a good name during whole my chess carrier, I am Officially inviting you to OTB blitz match with the Prize fund! Both of us will invest 5000$ and winner takes it all!
\nI suggest all other people who's intrested in this situation, just take a look at my results in 2016 and 2017 Blitz World championships, and that should be enough... No need to listen for every crying babe, Tigran Petrosyan is always play Fair ! And if someone will continue Officially talk about me like that, we will meet in Court! God bless with true! True will never die ! Liers will kicked off...\n\n"""

SHORTENED_PHRASES = [
    "Are you kidding ??? What the **** are you talking about man ?",
    "You was doing PIPI in your pampers when i was beating players much more stronger then you!",
    "Be brave, be honest to yourself and stop this trush talkings!!!",
    "Everybody know that i am very good blitz player, i can win anyone in the world in single game!",
    '"w"esley "s"o is nobody for me',
    "Tigran Petrosyan is always play Fair !",
    "God bless with true! True will never die ! Liers will kicked off...",
]


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_env(name):
    f = open(f".env/{name}", "r")
    val = f.read()
    f.close()
    return val


BOT_TOKEN = get_env("bot_token")
client = discord.Client()
client.Activity(name="always fair !", type=5)


@client.event
async def on_ready():
    print(f"logged in as {client}")


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        if message.content.startswith("/restart_tiko") and message.author.id == ADMIN_ID:
            exit(0)
        if message.content.startswith("./test_err") and message.author.id == ADMIN_ID:
            tmp = 0 / 0

        content = message.content.lower()

        if "!petrosyan" in content or "!petrosian" in content:
            await message.reply(SHORTENED_PHRASES[randint(0, len(SHORTENED_PHRASES))])
        else:
            for keyword in KEYWORDS:
                if keyword in content:
                    await message.reply(PASTA)

    except Exception as e:
        eprint(e)
        exit(1)


client.run(BOT_TOKEN)
