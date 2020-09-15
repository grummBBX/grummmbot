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

@client.command
async def hi(ctx):
    eli = ':middle_finger:'*random.randint(7,20)
    await ctx.send(f':{eli}')

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
async def goat(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/463790920190394368/755286630964920361/video0.mp4')

@client.command()
async def benji(ctx):
    benjis = ['https://cdn.discordapp.com/attachments/697587669051637760/755291515571404830/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755291085118504960/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755290782314790952/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755290436452483183/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755290135737794620/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755289698863153272/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755289554805588068/video0.mov',
            'https://cdn.discordapp.com/attachments/697587669051637760/755287161452101662/video0.mov'
            'https://cdn.discordapp.com/attachments/697587669051637760/755420114182078484/video0.mov']
    await ctx.send(f'{random.choice(benjis)} ')

@client.command(aliases=['dogs'])
async def doggies(ctx):
    dogs = ['https://cdn.discordapp.com/attachments/700013635824779324/755421561074352260/20200915_102822.jpg',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421561313558538/The_Tiananmen_Square_protests_or_the_Tiananmen_Square_Incident_commonly_known_as_the_June_Fourth_Inc.png',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421633761640488/20200913_033908.jpg',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421634013298688/image0-95.jpg',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421634281603223/20200910_204636.jpg',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421936854499378/thisrtypup.png',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421937156620359/missile.png',
            'https://cdn.discordapp.com/attachments/700013635824779324/755421937383112745/image0-23.jpg',
            'https://cdn.discordapp.com/attachments/700013635824779324/755422106426277988/IMG_20200731_015903.jpg',
            'https://cdn.discordapp.com/attachments/700013635824779324/755422107185447012/IMG_20200802_100917_431.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755424812935020564/20180323_075133.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755424813358514206/20180326_104822.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755424813723549756/20180326_115317.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755425141885894737/20180327_075603.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755425142342942930/20180327_114839.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755425142771024031/20180403_075404.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755425294449377300/20180403_144804.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755425295292563486/20180405_082722.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755425475156770950/image0.jpg',
            'https://cdn.discordapp.com/attachments/754148718667890698/755424990467194900/image0.jpg',
            'https://cdn.discordapp.com/attachments/754148718667890698/755425715221954600/image0.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755428266101309450/20200907_135631.jpg',
            'https://cdn.discordapp.com/attachments/473348357826281474/755426985316057128/20200915_085624.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755454969003376700/WIN_20200127_22_32_34_Pro.jpg',
            'https://cdn.discordapp.com/attachments/697587669051637760/755455160393793656/WIN_20200629_14_23_50_Pro_2.jpg']
    await ctx.send(f'{random.choice(dogs)} ')

client.run('')
