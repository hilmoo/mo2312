import discord
import os
from discord.ext import commands
intents = discord.Intents.all()

client = commands.Bot(command_prefix='mo.',intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#perintah ping
@client.command()
async def ping(ctx):
    await ctx.send("pong")


#perintah avatar
@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    """Displays avatar user."""
    if not member:
        member = ctx.message.author
    avatar_url = member.avatar_url
    embedAVA = discord.Embed(title="{}'s avatar".format(member), url=str(avatar_url))
    embedAVA.set_image(url=f"{avatar_url}")
    await ctx.send(embed=embedAVA)


#perintah userinfo
@client.command()
async def userinfo(ctx, user: discord.Member = None):
    """Displays user information."""
    if user == None:
        user = ctx.author

    datetime_format = "%m/%d/%Y, %H:%M:%S"
    roles = [role for role in user.roles[1:]]
  
    embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
    embed.add_field(name="Nickname",value=str(user.display_name),inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Roles", value=' '.join([role.mention for role in roles]),inline=False)
    embed.add_field(name="Joined", value=f"{user.joined_at.strftime(datetime_format)}",inline=True)
    embed.add_field(name="Created", value=f"{user.created_at.strftime(datetime_format)}",inline=True)
    embed.set_thumbnail(url=user.avatar_url)

    await ctx.send(embed=embed)

#perintah join
@client.command(pass_context = True)
async def mlebet(ctx):
  """Join Voice Channel."""
  if(ctx.author.voice):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("bakekok voice")
  else:
    await ctx.send("ra ono voice")
  
#perintah leave
@client.command(pass_context = True)
async def medal(ctx):
  """Leave Voice Channel."""
  if(ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("mutung aku, tak metu")
  else:
    await ctx.send("sepiiii")

#perintah avatar
@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    """Displays avatar user."""
    if not member:
        member = ctx.message.author
    avatar_url = member.avatar_url
    embedAVA = discord.Embed(title="{}'s avatar".format(member), url=str(avatar_url))
    embedAVA.set_image(url=f"{avatar_url}")
    await ctx.send(embed=embedAVA)


#perintah userinfo
@client.command()
async def userinfo(ctx, user: discord.Member = None):
    """Displays user information."""
    if user == None:
        user = ctx.author

    datetime_format = "%m/%d/%Y, %H:%M:%S"
    roles = [role for role in user.roles[1:]]
  
    embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
    embed.add_field(name="Nickname",value=str(user.display_name),inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Roles", value=' '.join([role.mention for role in roles]),inline=False)
    embed.add_field(name="Joined", value=f"{user.joined_at.strftime(datetime_format)}",inline=True)
    embed.add_field(name="Created", value=f"{user.created_at.strftime(datetime_format)}",inline=True)
    embed.set_thumbnail(url=user.avatar_url)

    await ctx.send(embed=embed)

client.run(os.getenv('TOKEN'))
