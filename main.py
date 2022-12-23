#as always FUCK NEIL
#MTA0OTkzMjY5OTM0OTAyNDgxOQ.G8SDPQ.r_hmW1YmgTsHMa9ADXXFF5pwt85XafhP4Vgftk

#other files
import os
import json
from os import walk
import random



import discord

intents = discord.Intents.all()
intents.members = True

#client = commands.Bot(intents=intents, prefix_and_other_things_go_here)

bot = discord.Bot(intents=intents)
guild_ids=[1024800030558789652,799510008881610802]
#
print("LAUNCHING...")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print("LAUNCHED!")

#defer(*, ephemeral=False, thinking=False)


@bot.command(description="Let me tell you about myself") # 
async def about(ctx):
    #await interaction.response.send_message("test", ephemeral=True)
    await ctx.respond("Hello im the dicebot. \nIf appear to have developed a fault please report this using /reporterror", ephemeral=True)

@bot.slash_command(guild_ids=guild_ids)
async def reporterror(ctx, report: str):
    await ctx.respond("Thank you for reporting this error we apologize that this has occurred your receipt is being printed:", ephemeral=True)
    error = ("Error Report: \n"+str(report))
    await ctx.respond("Error receipt generated:\n"+error, ephemeral=True)
    with open('err.txt', 'a') as f:
        f.write("\n\nUser:"+str(ctx.author.id)+"\n"+error)
    print("error reported")

@bot.slash_command(description="I'll roll a d20 for you")
async def roll(ctx):
    #await interaction.response.send_message("test", ephemeral=True)
    roll = random.randrange(1, 21)
    await ctx.respond("you rolled a: "+str(roll))

@bot.slash_command(description="I'll roll a die with 'x' number of sides")
async def rollnum(ctx,diesides):
    roll = random.randrange(0, diesides)+1
    await ctx.respond("you rolled a: "+str(roll)+" on a d"+str(diesides))


@bot.command(description="test")
async def test(ctx):
    await ctx.respond("Test!", ephemeral=True)

#@bot.slash_command(description="Hello World") # 슬래시 커맨드 등록
#async def helloworld(ctx): # 슬래시 커맨드 이름
#    await ctx.respond("Hello World!", ephemeral=True) # 인터렉션 응답; ephemeral = True

print("Jaimie did you save?")
print("Running...")


with open("token.txt",mode="r") as f:
    token = f.read()
    print(token)
print(token)
bot.run(token)