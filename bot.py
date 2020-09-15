import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)} ')

@client.command()
async def benji(ctx):
    benjis = ['https://cdn.discordapp.com/attachments/697587669051637760/755291515571404830/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755291085118504960/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755290782314790952/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755290436452483183/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755290135737794620/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755289698863153272/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755289554805588068/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755287161452101662/video0.mov']
    await ctx.send(f'{random.choice(benjis)} ')

client.run('')
