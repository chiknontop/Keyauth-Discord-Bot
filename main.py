import discord
import requests
import json
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

embedcolor = 0x0070ff
embedthumb = "https://cdn.dribbble.com/users/5242374/screenshots/16641455/media/0a74ea6b1d505b316ced8be139175fc3.gif"

api_key = ""
keyauthrole = ""

@bot.slash_command(name='ping', description='Whats my ping?')
async def ping(interaction: discord.Interaction):
    latency = bot.latency * 1000
    try:
        response = requests.head(f'https://keyauth.win/api/seller/?sellerkey={api_key}&type=fetchallkeys&format=json')
        ping = round(response.elapsed.total_seconds() * 1000, 2)
        embed = discord.Embed(title="Ping Info:", color=embedcolor)
        embed.add_field(name="Bot Ping:", value=f"```{latency}ms```", inline=True)
        embed.add_field(name="Keyauth Api Ping:", value=f"```{ping}ms```", inline=True)
        embed.set_thumbnail(url=embedthumb)
        embed.set_footer(text=f"Slash Bot Example - Made By chikn")
        await interaction.send(embed=embed)
    except requests.exceptions.RequestException:
        embed = discord.Embed(title="Ping Info:", color=embedcolor)
        embed.add_field(name="Bot Ping:", value=f"```{latency}```", inline=True)
        embed.add_field(name="Keyauth Api Ping:", value=f"```ERROR```", inline=True)
        embed.set_thumbnail(url=embedthumb)
        embed.set_footer(text=f"Slash Bot Example - Made By chikn")
        await interaction.send(embed=embed)

@bot.slash_command(name='resethwid', description='Reset a users HWID!')
async def resethwid(interaction: discord.Interaction, user=None):
    if user is None:
        embed = discord.Embed(title=f"ERROR", description=f'Missing argument `user`:\n Usage: `.resethwid [user]`', color=0xFF0000)
        embed.set_footer(text=f"Keyauth Bot - Made By chikn")
        await interaction.send(embed=embed)
    else:
        role = discord.utils.get(interaction.guild.roles, name=keyauthrole)
        if role in interaction.user.roles:
            url = f"https://keyauth.win/api/seller/?sellerkey={api_key}&type=resetuser&user={user}"
            response = requests.get(url)
            data = json.loads(response.text)
            if data["success"] == True:
                embed = discord.Embed(title=f"Successfully Reset User's HWID", description=f'**Username ->** `{user}`', color=embedcolor)
                embed.set_thumbnail(url=embedthumb)
                embed.set_footer(text=f"Keyauth Bot - Made By chikn")
                await interaction.send(embed=embed)
            else:
                embed = discord.Embed(title=f"ERROR", description=f"```{data['message']}```", color=0xFF0000)
                embed.set_footer(text=f"Keyauth Bot - Made By chikn")
                await interaction.send(embed=embed)
        else:
            embed = discord.Embed(title=f"ERROR", description=f"```You do not have permission to use this command!```", color=0xFF0000)
            embed.set_footer(text=f"Keyauth Bot - Made By chikn")
            await interaction.send(embed=embed)

@bot.slash_command(name='userinfo', description='Fetch Info About a User!')
async def userinfo(interaction: discord.Interaction, user=None):
    if user is None:
        embed = discord.Embed(title=f"ERROR", description=f'Missing argument `user`:\n Usage: `.userinfo [user]`', color=0xFF0000)
        embed.set_footer(text=f"Keyauth Bot - Made By chikn")
        await interaction.send(embed=embed)
    else:
        role = discord.utils.get(interaction.guild.roles, name=keyauthrole)
        if role in interaction.user.roles:
            url = f"https://keyauth.win/api/seller/?sellerkey={api_key}&type=userdata&user={user}"
            response = requests.get(url)
            data = json.loads(response.text)
            if data["success"] == True:
                embed = discord.Embed(title=f"Successfully Fetched User's Info", color=embedcolor)
                embed.add_field(name="IP ADDRESS:", value=f"```{data['ip']}```", inline=True)
                embed.add_field(name="HWID:", value=f"```{data['hwid']}```", inline=True)
                embed.add_field(name="Creation Date:", value=f"```{data['createdate']}```", inline=True)
                embed.add_field(name="Last Login:", value=f"```{data['lastlogin']}```", inline=True)
                embed.add_field(name="Cooldown?:", value=f"```{data['cooldown']}```", inline=True)
                embed.add_field(name="Banned?:", value=f"```{data['banned']}```", inline=True)
                embed.add_field(name="Password:", value=f"```{data['password']}```", inline=False)
                embed.add_field(name="Token:", value=f"```{data['token']}```", inline=False)
                embed.set_thumbnail(url=embedthumb)
                embed.set_footer(text=f"Keyauth Bot - Made By chikn")
                await interaction.send(embed=embed)
            else:
                embed = discord.Embed(title=f"ERROR", description=f"```{data['message']}```", color=0xFF0000)
                embed.set_footer(text=f"Keyauth Bot - Made By chikn")
                await interaction.send(embed=embed)
        else:
            embed = discord.Embed(title=f"ERROR", description=f"```You do not have permission to use this command!```", color=0xFF0000)
            embed.set_footer(text=f"Keyauth Bot - Made By chikn")
            await interaction.send(embed=embed)



bot.run('')