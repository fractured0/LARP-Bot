from typing import Optional
import discord
from discord.ext import commands, tasks
import random
from discord import app_commands
from datetime import datetime

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

@tasks.loop(seconds=25)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Los Angeles Roleplay"))

@client.event
async def on_ready():
    await client.tree.sync()
    print("Success: The bot is connected to discord")
    change_status.start()

@client.tree.command(name="promotion", description="Used to promote a member to a new rank")
async def promotion(interaction: discord.Interaction):
    embed_promotion = discord.Embed(title="Promotion", description="", color=discord.Color.gold())




@client.tree.command(name="sessionpanel", description="Sends panel to manage sessions")
@commands.has_role(1176244055148073151)
async def sessionpanel(interaction: discord.Interaction):
    embed_panel = discord.Embed(title="Session Panel", description="", color=discord.Color.gold())
    embed_panel.add_field(name="<:larp11:1173076367613636669> SSU", value="<:Bulletin:1173084676441788416>`Sends SSU embed`", inline=False)
    embed_panel.add_field(name="<:larp11:1173076367613636669> SSD", value="<:Bulletin:1173084676441788416>`Sends SSD embed`", inline=False)
    embed_panel.add_field(name="<:larp11:1173076367613636669> Poll", value="<:Bulletin:1173084676441788416>`Sends Session poll embed`", inline=False)
    embed_panel.add_field(name="<:larp11:1173076367613636669> Server Full", value="<:Bulletin:1173084676441788416>`Sends Session full embed`", inline=False)
    embed_panel.add_field(name="<:larp11:1173076367613636669> Low Player Count", value="<:Bulletin:1173084676441788416>`Sends Low player count embed`", inline=False)
    embed_panel.set_footer(text="Once button is clicked it will send to sessions channel!")
    embed_panel.set_thumbnail(url=interaction.guild.icon)
    embed_panel.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
    view = sessionpanel()
    await interaction.response.send_message(embed=embed_panel, view=view)

class sessionpanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="SSU", style=discord.ButtonStyle.green)
    async def ssu(self, interaction:discord.Interaction, button: discord.ui.Button):
        target_channel = client.get_channel(1173012394235138198)
        embed_ssu = discord.Embed(title="<:larp11:1173076367613636669> LARP SSU <:larp11:1173076367613636669>", description="**We are starting our server**", color=discord.Color.green())
        embed_ssu.add_field(name="", value="<:Bulletin:1173084676441788416>**Name:** `Los Angeles City Roleplay | Strict | Fun`", inline=False)
        embed_ssu.add_field(name="", value="<:Bulletin:1173084676441788416>**In-game owner:** `DiamondCharger27`", inline=False)
        embed_ssu.add_field(name="", value="<:Bulletin:1173084676441788416>**Code:** `LARRRP`", inline=False)
        embed_ssu.add_field(name="", value="<:Bulletin:1173084676441788416>**Requirements:** `None`", inline=False)
        embed_ssu.add_field(name="", value=f"<:Bulletin:1173084676441788416>**Session host:**{interaction.user.mention}", inline=False)
        embed_ssu.add_field(name="", value="<:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801>", inline=False)
        embed_ssu.add_field(name="", value="<:Arrow:1173084704795279400> *Please read our <#1172792333771751494> before joining!*", inline=False)
        embed_ssu.set_thumbnail(url=interaction.guild.icon)
        embed_ssu.set_image(url="https://media.discordapp.net/attachments/1172787855760834602/1175989171475714078/LARP_SSU_Banner.png?ex=656d3c43&is=655ac743&hm=2bf34a4bd7d91954989cb2b404f861deb8d5541c5ca8faeb2f05a4f6490cc88e&=&width=1025&height=277")
        embed_ssu.set_footer(text="Have fun LARP!")
        guild = client.get_guild(1172787777167953962)
        role = guild.get_role(1172791347908980758)
        await target_channel.send(content=role.mention + "@here", embed=embed_ssu)
        
    @discord.ui.button(label="SSU Poll", style=discord.ButtonStyle.blurple)
    async def poll(self, interaction:discord.Interaction, button: discord.ui.Button):
        target_channel = client.get_channel(1173012394235138198)
        embed_poll = discord.Embed(title="<:larp11:1173076367613636669> LARP Session Poll <:larp11:1173076367613636669>", description="", color=discord.Color.gold())
        embed_poll.add_field(name="", value="<:Bulletin:1173084676441788416>**This is to determine if we should start the server or not**", inline=False)
        embed_poll.add_field(name="", value="", inline=False)
        embed_poll.add_field(name="", value="", inline=False)
        embed_poll.add_field(name="", value="Reactions required `7+`", inline=False)
        embed_poll.add_field(name="", value=f"<:Bulletin:1173084676441788416>**Poll host:**{interaction.user.mention}", inline=False)
        embed_poll.add_field(name="", value="<:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801>", inline=False)
        embed_poll.set_footer(text="If you react you must join, if you don't moderation actions will be taken.")
        embed_poll.set_thumbnail(url=interaction.guild.icon)
        embed_poll.set_image(url="https://media.discordapp.net/attachments/1172787855760834602/1176006742937718834/LARP_SSU_Poll_Banner.png?ex=656d4ca0&is=655ad7a0&hm=e53b3c93f12ddea27c2404389c3d34c74a27e704c8a3be01bbe6f6f66d6cbfe4&=&width=1025&height=277")
        guild = client.get_guild(1172787777167953962)
        role = guild.get_role(1172791347908980758)
        message = await target_channel.send(content=role.mention + "@here", embed=embed_poll)
        await message.add_reaction("<:larp11:1173076367613636669>")
        
    @discord.ui.button(label="SSD", style=discord.ButtonStyle.red)
    async def ssd(self, interaction:discord.Interaction, button: discord.ui.Button):
        target_channel = client.get_channel(1173012394235138198)
        embed_ssd = discord.Embed(title="<:larp11:1173076367613636669> LARP SSD <:larp11:1173076367613636669>", description="", color=discord.Color.red())
        embed_ssd.add_field(name="", value="<:Bulletin:1173084676441788416>**The server has been shutdown.**", inline=False)
        embed_ssd.add_field(name="", value="<:Bulletin:1173084676441788416>**This could have been because of a low player count, session got to chaotic, etc.**", inline=False)
        embed_ssd.add_field(name="", value="", inline=False)
        embed_ssd.add_field(name="", value=f"<:Bulletin:1173084676441788416>**Shutdown by:**{interaction.user.mention}", inline=False)
        embed_ssd.add_field(name="", value="<:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801><:f_line:1173088159182110801>", inline=False)
        embed_ssd.set_footer(text="Please do not join the server at this time!")
        embed_ssd.set_thumbnail(url=interaction.guild.icon)
        embed_ssd.set_image(url="https://cdn.discordapp.com/attachments/1172787855760834602/1176006534250102964/LARP_SSD_Banner.png?ex=656d4c6e&is=655ad76e&hm=986c5f28e7ca70628f3c6a949547f6a5e32e1444b68b08c046f4a7e5ac8ebfe2&")
        guild = client.get_guild(1172787777167953962)
        role = guild.get_role(1172791347908980758)
        message = await target_channel.send(content=role.mention, embed=embed_ssd)
        
    @discord.ui.button(label="Server Full", style=discord.ButtonStyle.grey)
    async def full(self, interaction:discord.Interaction, button: discord.ui.Button):
        target_channel = client.get_channel(1173012394235138198)
        embed_full = discord.Embed(title="<:larp11:1173076367613636669> In-game server is full! <:larp11:1173076367613636669>", description="", color=discord.Color.gold())
        embed_full.add_field(name="", value="<:Arrow:1173084704795279400>**The server is now full! The queue may be long.**", inline=False)
        embed_full.add_field(name="", value="<:Bulletin:1173084676441788416>**Thank you! You can  still join by clicking [here](https://policeroleplay.community/join/LARRRP)**", inline=False)
        embed_full.set_thumbnail(url=interaction.guild.icon)
        embed_full.set_footer(text="This full session way come with a giveaway, no promises tho.")
        await target_channel.send(embed=embed_full)

    @discord.ui.button(label="Low Player Count", style=discord.ButtonStyle.grey)
    async def low(self, interaction:discord.Interaction, button: discord.ui.Button):
        target_channel = client.get_channel(1173012394235138198)
        embed_low = discord.Embed(title="<:larp11:1173076367613636669> Low Player count <:larp11:1173076367613636669>", description="", color=discord.Color.red())
        embed_low.add_field(name="", value="<:Arrow:1173084704795279400>**We are currently low on players!**", inline=False)
        embed_low.add_field(name="", value="<:Bulletin:1173084676441788416>**Join up by using code LARRRP or [click here](https://policeroleplay.community/join/LARRRP)!**")
        embed_low.set_thumbnail(url=interaction.guild.icon)
        await target_channel.send(content="@here", embed=embed_low)

@client.tree.command(name="chatrevive", description="Send's engaging questions to revive the chat.")
async def chatrevive(interaction: discord.interactions):
    with open("responses.txt", "r")as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        guild = client.get_guild(1172787777167953962)
        role = guild.get_role(1172791429588861008)
    chatrevive = discord.Embed(title="Chat Revive", description=f"<:Arrow:1173084704795279400>{response}", color=discord.Color.gold())
    chatrevive.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
    await interaction.channel.send(content=role.mention, embed=chatrevive)

client.run("MTE3Mzc1NTE3MTcwMTAxNDU1OA.GBLH5D.NrBjgIUIIT8QL0vKSMsFc7WpT8XJzhvoBAbZuE")