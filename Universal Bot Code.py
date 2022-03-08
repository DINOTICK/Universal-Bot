from ast import Delete
from email import message
from tkinter import N
from unicodedata import name
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import random
import time
from wikipedia import summary
import os

startinputstat = input("Status: ")
prefixvarinput = input("Choose a command symbol: 1 = amogus, 2 = $, 3 = ! ")
if prefixvarinput == "1":
    prefixvar = "amogus"
elif prefixvarinput == "2":
    prefixvar = "$"
elif prefixvarinput == "3":
    prefixvar = "!"
else:
    print("You must choose between numbers: 1, 2, and 3. (This window will close in 5 seconds.)")
    time.sleep(5)
    quit()

print("One second...")
time.sleep(3)
print("Ready to deploy!")
time.sleep(.5)
print("Deploying...")
time.sleep(2)
print("Deployed!")
print("Notice! Closing this window will turn off the bot.")
activity = discord.Game(name=startinputstat)
jokelist = ["you <:HDtroll:943715101708529767>", "Don't ask why the bot roles are a rainbow.  Our public relations department has been underfunded lately, we're doing everything we can."]
coins = ["It landed on heads!", "It landed on tails!"]
client = discord.Client()
bot = commands.Bot(command_prefix=prefixvar,
                   description="This is a Helper Bot, that fits almost any discord server. Made by DINO/PING BIT.",
                   help_command=None, activity=activity, status=discord.Status.online)

@bot.event
async def on_ready():
    print("Online.")
    print("Awaiting commands.")

@bot.command()
async def ping(ctx):
    await ctx.message.channel.send('pong')
    print("Ping command used in: " + ctx.guild.name)

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.message.channel.send(numOne + numTwo)
    print("Sum command used in: " + ctx.guild.name)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server information",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
#nice
    await ctx.message.channel.send(embed=embed)
    print("Info was sent in: " + ctx.guild.name)

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        embed = discord.Embed(title="user kicked", description="kicked user " + str(member),
            timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Reason", value=str(reason))
        await ctx.message.channel.send(embed=embed)
        await ctx.message.delete()
        print("Kicked member: " + str(member) + ". Report from: " + ctx.guild.name)
    else:
        await ctx.message.channel.send("You do not have permission to kick.")
        print(
            "Member attempted to kick. Did not have admin, or bot's role was obstructed. Report from: " + ctx.guild.name)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        embed = discord.Embed(title="user banned", description="banned user " + str(member),
            timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Reason", value=str(reason))
        await ctx.message.channel.send(embed=embed)
        await ctx.message.delete()
        print("Banned member: " + str(member) + ". Report from: " + ctx.guild.name)
    else:
        await ctx.message.channel.send("You do not have permissions to ban.")
        print(
            "Member attempted to ban. Did not have admin, or bot's role was obstructed. Report from: " + ctx.guild.name)

@bot.command()
async def fban(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.ban_members:
        embed = discord.Embed(title="user banned", description="banned user " + str(member),
            timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Reason", value=str(reason))
        await ctx.message.channel.send(embed=embed)
        await ctx.message.delete()
        print("FakeBanned member: " + str(member) + ". Report from: " + ctx.guild.name)
    else:
        await ctx.message.channel.send("You do not have permissions to ban.")
        print(
            "Member attempted to fakeban. Did not have admin, or bot's role was obstructed. Report from: " + ctx.guild.name)

@bot.command()
async def changenick(ctx, member: discord.Member, *, nick):
    if ctx.message.author.guild_permissions.administrator:
        await member.edit(nick=nick)
        await ctx.message.channel.send(f"Nickname was changed for {member.mention} ")
        print("Nickname was changed for user: " + str(
            member) + " Their new nickname is: " + nick + ". Report from: " + ctx.guild.name)
    else:
        await ctx.message.channel.send("You do not have the permissions to change usernames.")
        print(
            "Member attempted to change a nickname. Did not have admin, or bot's role was obstructed. Report from: " + ctx.guild.name)

@bot.command()
async def test(ctx):
    if ctx.message.author.guild_permissions.send_messages:
        await ctx.message.channel.send("Hello testing")
        print("Testing")

@bot.command()
async def report(ctx, *, problem):
    await ctx.message.channel.send("Your bug report/suggestion was sent.")
    print("Report from " + ctx.guild.name + " Report: " + problem)

@bot.command()
async def coinflip(ctx):
    await ctx.message.channel.send(random.choice(coins))
    print("Coin flip used in: " + ctx.guild.name)

@bot.command()
async def joke(ctx):
    await ctx.message.channel.send(random.choice(jokelist))
    print("Joke sent in: " + ctx.guild.name)

@bot.command()
async def jokerep(ctx, *, jrep):
    await ctx.message.channel.send(
        "Your joke was recorded. It will be added if the developer aporoves it. (Could be a few hours.)")
    #jokefile = open("jokes.txt", "a")
    #jokefile.write("\n" + jrep + "\n")
    #jokefile.close
    print("Incoming joke from: " + ctx.guild.name + " Joke sent: " + jrep)

@bot.command()
async def membercount(ctx):
    await ctx.message.channel.send("There are " + str(ctx.guild.member_count) + " members in this server.")
    print("Member count command used in server: " + ctx.guild.name)

@bot.command()
async def servercount(ctx):
    servers = list(bot.guilds)
    await ctx.channel.send(f"I am currently in {str(len(servers))} servers.")
    print("servercount command used in server: " + ctx.guild.name)

@bot.command()
async def setdelay(ctx, seconds: int):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.channel.send(f"Set the slowmode delay in this channel to {seconds} seconds.")
        print("Slowmode was set to: " + str(seconds) + " seconds. Command used in: " + ctx.guild.name)
    else:
        await ctx.channel.send("You do not have admin permissions.")
        print(
            "Member attempted to set slowmode. Did not have admin, or bot's role was obstructed. Report from: " + ctx.guild.name)

@bot.command()
async def wikisearch(ctx, *, search):
    try:
        searchresults = summary(str(search), sentences=15)
        await ctx.channel.send(searchresults)
        print("Wikipedia command used. Search term used: " + str(search) + ". Report from: " + ctx.guild.name)
    except:
        print("Wikisearch error from: " + ctx.guild.name)
        await ctx.channel.send("Uh-oh, something went wrong! An automatic report was sent to the bot owner.")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Command Help", description="Help for all current commands this discord bot supports.",
                          color=0xf084c8)
    embed.add_field(name=f"{prefixvar}ping", value="Replies with pong.", inline=False)
    embed.add_field(name=f"{prefixvar}info", value="Gives info about the server.", inline=False)
    embed.add_field(name=f"{prefixvar}ban [member]", value="Bans a user.", inline=False)
    embed.add_field(name=f"{prefixvar}kick [member]", value="Kicks a user.", inline=False)
    embed.add_field(name=f"{prefixvar}test", value="A test command, that replies with: Hello testing.", inline=False)
    embed.add_field(name=f"{prefixvar}changenick [member] [new name]", value="changes a user's nick-name.",
                    inline=False)
    embed.add_field(name=f"{prefixvar}coinflip", value="Randomly picks between heads, and tails.", inline=False)
    embed.add_field(name=f"{prefixvar}joke",
                    value="Randomly picks a joke from my joke database. You can add a joke using the jokeadd command.",
                    inline=False)
    embed.add_field(name=f"{prefixvar}jokerep [joke]",
                    value="Adds a joke to the bot's database, to be used for the joke command.", inline=False)
    embed.add_field(name=f"{prefixvar}membercount", value="Tells you the amount of members in a server.", inline=False)
    embed.add_field(name=f"{prefixvar}servercount", value="Tells you the amount of servers the bot is in.",
                    inline=False)
    embed.add_field(name=f"{prefixvar}report [error/suggestion]",
                    value="Allows you to suggest a feature, or report a bug.", inline=False)
    embed.add_field(name=f"{prefixvar}setdelay [time in seconds]",
                    value="Changes the current channel's slowmode. (Setting it to 0 removes slowmode)")
    embed.add_field(name=f"{prefixvar}wikisearch [Search term]",
                    value="Searchs Wikipedia for information, and displays it.", inline=False)
    embed.set_footer(
        text=f"Command missing? message PING BIT#9644 for help or go to bot help. Made by Dino/PING BIT. (Command prefix: {prefixvar})")
    await ctx.send(embed=embed)
    print("Help command used in: " + ctx.guild.name)

# Events and stuff

@bot.event
async def on_guild_join(guild):
    servers = list(bot.guilds)
    print("We are in a new server! I am in a total of: " + str(len(servers)) + " servers!")

bot.run('XXXXX-XXXXX-XXXXX-XXXXX')
