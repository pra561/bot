import random
import discord
from discord import client, Member
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

client = commands.Bot(command_prefix=',')


@client.event
async def on_ready():
    print('BOT IS READY.')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 10)}ms ')


@client.command(alisases=['8ball', 'test'])
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
    await ctx.send(f'qusestion : {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)


@client.command()
async def pyro(ctx):
    await ctx.send("hey this is John Marcus . Im 13 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Jollibee store, and I get home every day by 8 PM at the latest. I don’t smoke, but I occasionally drink. I’m in bed by MIDNIGHT , and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning.")


@client.command()
async def pradip(ctx):
    await ctx.send("A Op guy")


@client.command()
async def creator(ctx):
    await ctx.send("Pradip AND TarithJ")


@client.command()
async def mark(ctx):
    await ctx.send("An anime guy who flirts with other girls and a simp")


@client.command()
async def tarithj(ctx):
    await ctx.send("dm him/her idk who is he/she,his/her id is tarithj#7332")


@client.command()
async def rune(ctx):
    await ctx.send("rune guy want to be a gay but,he is too rude guy when he hart anyone he say jk at last")


@client.command()
async def nisan(ctx):
    await ctx.send("baren and error's friend who want a boy friend")


@client.command()
async def kiss(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/913996856365821952/914821672572440576/kissdofull.gif')

@client.command()
async def punch(ctx):
    await ctx.send('https://c.tenor.com/VrWzG0RWmRQAAAAM/anime-punch.gif')

@client.command()
async def slap(ctx):
    await ctx.send('https://i.imgur.com/fm49srQ.gif?noredirect')  

@client.command()
async def pillow(ctx):
    await ctx.send('https://c.tenor.com/EfhPfbG0hnMAAAAM/slap-handa-seishuu.gif')  

@client.command()
async def kill(ctx):
    await ctx.send('https://images-ext-2.discordapp.net/external/4nztNvTnX0WDlvW0n71rLjgLbQt-yHY-kD4nrBoPB0I/https/cdn.weeb.sh/images/HyXTiyKw-.gif?width=400&height=225')  


@client.command()
async def kick(ctx, user: Member, *, reason="No reason provided"):
    await user.kick(reason=reason)
    await ctx.send(f"kicked {user.mention} for {reason}")

@client.command()
async def ban(ctx, user: Member, *, reason="No reason provided"):
    await user.ban()
    await ctx.send(f"kicked {user.mention} for {reason}")


client.run('OTIzOTI2MTk2OTc3Mjc0ODkx.YcXHUw.qx6fTjHtU9BlPOfyVdOQC7kqA-Y')
