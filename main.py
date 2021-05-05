from __future__ import print_function
import discord
import sys
from random import choice
import re

ADMIN_ID = 213341816324489217
KEYWORDS = {"pipi", "pampers", "պիպի", "պամպերս"}
SHORT_KEYWORDS = {"tiko", "tigran", "petrosian", "petrosyan", "տիկո", "տիգրան", "պետրոսյան", "keepo"}
DONT_COMMENT_KEYWORD = "!nopipi"
HOME_URL = "http://tiny.cc/petrosyan"
PASTA = """Are you kidding ??? What the \*\*\*\* are you talking about man ? You are a biggest looser i ever seen in my life ! You was doing PIPI in your pampers when i was beating players much more stronger then you! You are not proffesional, because proffesionals knew how to lose and congratulate opponents, you are like a girl crying after i beat you! Be brave, be honest to yourself and stop this trush talkings!!! Everybody know that i am very good blitz player, i can win anyone in the world in single game! And "w"esley "s"o is nobody for me, just a player who are crying every single time when loosing, ( remember what you say about Firouzja ) !!! Stop playing with my name, i deserve to have a good name during whole my chess carrier, I am Officially inviting you to OTB blitz match with the Prize fund! Both of us will invest 5000$ and winner takes it all!
\nI suggest all other people who's intrested in this situation, just take a look at my results in 2016 and 2017 Blitz World championships, and that should be enough... No need to listen for every crying babe, Tigran Petrosyan is always play Fair ! And if someone will continue Officially talk about me like that, we will meet in Court! God bless with true! True will never die ! Liers will kicked off...\n\n"""

SHORTENED_PHRASES = [
    "Are you kidding ??? What the \*\*\*\* are you talking about man ?",
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


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("always fair ! /help_tiko"))
    print(f"logged in as {client}")


def numberize(text):
    nums = re.search(r"\d+", text)
    if nums:
        return int(nums.group())
    else:
        return None


@client.event
async def on_message(message):
    try:
        handled = False
        if message.author == client.user:
            return
        elif message.content.startswith("/restart_tiko") and message.author.id == ADMIN_ID:
            await message.reply("ok")
            exit(0)
        elif message.content.startswith("/test_err") and message.author.id == ADMIN_ID:
            tmp = 0 / 0
        elif message.content.startswith("/help_tiko") and message.author.id == ADMIN_ID:
            handled = True
            await message.reply(HOME_URL)
        if message.reference is not None:
            ref_message = await message.channel.fetch_message(message.reference.message_id)
            await message.reply("```" + str(client.user.id) + "```")
            if ref_message.author.id == client.user.id:
                await message.reply("```" + message.content + "```")

        content = message.content
        mentions = re.findall(r"<@!\d+>", content)
        for user_id in mentions:
            id = numberize(user_id)
            if id:
                user = await client.fetch_user(id)
                if user:
                    content = content.replace(user_id, str(user))

        content = content.lower()

        # if message.author.id == ADMIN_ID:
        #    await message.reply("```" + content + "```")

        if not handled:
            for keyword in KEYWORDS:
                if keyword in content:
                    await message.reply(PASTA)
                    handled = True
                    break

        if not handled:
            for keyword in SHORT_KEYWORDS:
                if keyword in content:
                    await message.reply(choice(SHORTENED_PHRASES))
                    break

    except Exception as e:
        eprint(e)
        exit(1)


client.run(BOT_TOKEN)
