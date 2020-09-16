import discord
import random
from discord.ext import commands
from gblists import gblists

bot = commands.Bot(command_prefix = '.')

benjis = gblists.benjis
responses = gblists.responses
dogs = gblists.dogs


@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def hi(ctx):
    await ctx.send(':middle_finger:'*random.randint(7,20))

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)} ')

@bot.command()
async def goat(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/463790920190394368/755286630964920361/video0.mp4')

@bot.command()
async def benji(ctx):
    await ctx.send(random.choice(benjis))

@bot.command(aliases=['dogs', 'dog'])
async def doggies(ctx):
    await ctx.send(random.choice(dogs))

bot.run('')
