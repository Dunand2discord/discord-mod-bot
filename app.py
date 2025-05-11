import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} est en ligne')

@bot.tree.command(name="ban", description="Ban un membre du srv")
@app_commands.describe(member="Le membre à ban", reason="Raison du ban")
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    if interaction.user.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await interaction.response.send_message(f'{member} a été banni.', ephemeral=True)
    else:
        await interaction.response.send_message("Essaie pas de bannir des membres alors que tu n'as pas la perm :)", ephemeral=True)

@bot.tree.command(name="kick", description="Kick un membre du srv.")
@app_commands.describe(member="Le membre à expulser", reason="Raison de l'expulsion")
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    if interaction.user.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await interaction.response.send_message(f'{member} a été expulsé.', ephemeral=True)
    else:
        await interaction.response.send_message("Essaie pas de kick des membres alors que tu n'as pas la perm :)", ephemeral=True)

@bot.tree.command(name="lock", description="Lock le salon.")
async def lock(interaction: discord.Interaction):
    if interaction.user.guild_permissions.manage_channels:
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
        await interaction.response.send_message("Le salon est maintenant verrouillé.", ephemeral=True)
    else:
        await interaction.response.send_message("Tu n'as pas la perm de lock le salon :)", ephemeral=True)

@bot.tree.command(name="unlock", description="Unlock le salon")
async def unlock(interaction: discord.Interaction):
    if interaction.user.guild_permissions.manage_channels:
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
        await interaction.response.send_message("Le canal est maintenant déverrouillé.", ephemeral=True)
    else:
        await interaction.response.send_message("BAH RIEN LE SALON EST LOCK :()", ephemeral=True)

bot.run('le token de votre bot')
