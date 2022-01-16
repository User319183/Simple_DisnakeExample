

import disnake
from disnake.ext import commands



intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.slash_command() # create a slash command
async def ping(inter):
    await inter.response.send_message("Pong!")


@bot.command()
async def ping(ctx):
    """ping + pong command.""" #description needed when doing `!help`
    await ctx.reply("Pong!")



bot.run("INSERT_BOT_TOKEN_HERE")