import os
from discord_easy_commands import EasyBot

bot = EasyBot()

bot.setCommand("!linktree", "https://linktr.ee/emapeire")
bot.setCommand("!twitter", "https://twitter.com/emapeire")
bot.setCommand("!telegram", "https://t.me/emapeire")
bot.setCommand("!welook", "https://welook.io/emapeire.eth")
bot.setCommand("!mirror", "https://mirror.xyz/emapeire.eth")

bot.run(os.environ['TOKEN'])
